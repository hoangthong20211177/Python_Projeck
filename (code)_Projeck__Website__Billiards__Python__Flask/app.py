from flask import Flask, render_template, request, redirect, session, url_for, flash
from routes.quan_ly_ban import ban_blueprint
from routes.quan_ly_nhan_vien import nhanvien_blueprint
from routes.quan_ly_san_pham import sanpham_blueprint
from routes.quan_ly_khach_hang import khachhang_blueprint
from routes.thong_ke import thongke_blueprint
from database import get_db_connection
from flask import request
import mysql.connector  # Import the MySQL connector package

app = Flask(__name__)
app.secret_key = 'your_secret_key'


app.register_blueprint(ban_blueprint)
app.register_blueprint(nhanvien_blueprint)
app.register_blueprint(sanpham_blueprint)
app.register_blueprint(khachhang_blueprint)
app.register_blueprint(thongke_blueprint)

# ĐĂNG KÝ TÀI KHOẢN
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        full_name = request.form['full_name']
        phone_number = request.form['phone_number']
        address = request.form['address']
        role_id = request.form['role_id']  # role_id là một số nguyên

        conn = get_db_connection()
        if conn.is_connected():
            try:
                # Kiểm tra xem tên đăng nhập đã tồn tại chưa
                cur = conn.cursor()
                cur.execute("SELECT id FROM account WHERE username = %s", (username,))
                account = cur.fetchone()

                if account:
                    flash('Tên đăng nhập đã tồn tại, vui lòng chọn tên đăng nhập khác.', 'error')
                else:
                    # Thêm tài khoản mới vào cơ sở dữ liệu
                    cur.execute("INSERT INTO account (username, password, full_name,phone_number,address  , role_id) VALUES (%s, %s, %s, %s,%s,%s)",
                                (username, password, full_name,phone_number,address  , role_id))
                    conn.commit()
                    flash('Đăng ký tài khoản thành công!', 'success')
                    return redirect(url_for('login'))
            except mysql.connector.Error as e: # type: ignore
                print(e)
                flash('Đã xảy ra lỗi khi đăng ký tài khoản.', 'error')
            finally:
                cur.close()
                conn.close()
        else:
            flash('Không thể kết nối đến cơ sở dữ liệu.', 'error')

    return render_template('register.html')


@app.route('/')
def index():
    return render_template('index.html')

# ĐĂNG NHẬP


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        conn = get_db_connection()
        if conn.is_connected():
            try:
                cur = conn.cursor()
                cur.execute("SELECT a.id, a.username, a.role_id, r.name FROM account a JOIN role r ON a.role_id = r.id WHERE username = %s AND password = %s", (username, password))
                account = cur.fetchone()

                if account:
                    role_id = account[2]
                    session['loggedin'] = True
                    session['id'] = account[0]
                    session['username'] = account[1]
                    session['role_id'] = role_id
                    session['role_name'] = account[3]

                    if role_id == 1:  # Admin role_id
                        session['loggedin_admin'] = True
                        session.pop('loggedin_nhanvien', None)  # Xóa nếu có
                        flash('Đăng nhập thành công admin!', 'success')
                        return redirect(url_for('admin'))
                    elif role_id == 2:  # Nhân viên role_id
                        session['loggedin_nhanvien'] = True
                        session.pop('loggedin_admin', None)  # Xóa nếu có
                        flash('Đăng nhập thành công nhân viên!', 'success')
                        return redirect(url_for('nhanvien'))
                    else:
                        flash('Không có quyền truy cập.', 'error')

                else:
                    flash('Tên đăng nhập hoặc mật khẩu không đúng.', 'error')
            except mysql.connector.Error as e: # type: ignore
                print(e)
                flash('Đã xảy ra lỗi khi đăng nhập.', 'error')
            finally:
                cur.close()
                conn.close()
        else:
            flash('Không thể kết nối đến cơ sở dữ liệu.', 'error')

    return render_template('login.html')



# ADMIN từ ĐĂNG NHẬP
@app.route('/admin')
def admin():
    if 'loggedin_admin' in session:
        conn = get_db_connection()
        if conn.is_connected():
            try:
                cur = conn.cursor()
                cur.execute("SELECT * FROM account WHERE id = %s", (session['id'],))
                account = cur.fetchone()
                return render_template('admin.html', account=account)
            except mysql.connector.Error as e: # type: ignore
                print(e)
            finally:
                cur.close()
                conn.close()

        return render_template('admin.html')
    else:
        return redirect(url_for('login'))

# NHÂN VIÊN từ ĐĂNG NHẬP
@app.route('/quanlybillards')
def nhanvien():
    if 'loggedin_nhanvien' in session:
        conn = get_db_connection()
        if conn.is_connected():
            try:
                cur = conn.cursor()
                cur.execute("SELECT * FROM account WHERE id = %s", (session['id'],))
                account = cur.fetchone()
                return render_template('nhanvien.html', account=account)
            except mysql.connector.Error as e: # type: ignore
                print(e)
            finally:
                cur.close()
                conn.close()

        return render_template('nhanvien.html')
    else:
        return redirect(url_for('login'))
    

# ĐĂNG XUẤT
@app.route('/logout')
def logout():
    session.pop('loggedin_nhanvien', None)
    session.pop('loggedin_admin', None)
    session.pop('id', None)
    session.pop('username', None)
    session.pop('role_id', None)
    flash('Bạn đã đăng xuất thành công!', 'success')
    return redirect(url_for('login'))



# MAIN
if __name__ == '__main__':
    app.run(debug=True)
