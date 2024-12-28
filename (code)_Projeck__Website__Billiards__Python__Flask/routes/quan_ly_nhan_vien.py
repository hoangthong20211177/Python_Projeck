from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask import request
from flask import flash
from database import get_db_connection

nhanvien_blueprint = Blueprint('quan_ly_nhan_vien', __name__)

@nhanvien_blueprint.route('/quanlynhanvien')



#----------------QUẢN LÝ NHÂN VIÊN----------------------
@nhanvien_blueprint.route('/quanlynhanvien')
def quanlynhanvien():
    
    keyword = request.args.get('keyword', '')

    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)

    if keyword:
        cursor.execute("SELECT a.* FROM account a JOIN role r ON a.role_id = r.id WHERE r.id = 2 AND (a.full_name LIKE %s OR a.phone_number LIKE %s)", ('%' + keyword + '%', '%' + keyword + '%'))
    else:
        cursor.execute("SELECT a.* FROM account a JOIN role r ON a.role_id = r.id WHERE r.id = 2 ")

    nhanviens = cursor.fetchall()

    cursor.close()
    connection.close()

    return render_template('quan_li_nhan_vien/nhanvien.html', nhanviens=nhanviens)
#THÊM NHÂN VIÊN
@nhanvien_blueprint.route('/themnhanvien', methods=['GET', 'POST'])
def them_nhan_vien():
    
    
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        full_name = request.form['full_name']
        phone_number = request.form['phone_number']
        address = request.form['address']
        role_id = 2
        
        connection = get_db_connection()
        cursor = connection.cursor()

        insert_query = "INSERT INTO account (username, password,full_name,phone_number,address,role_id) VALUES (%s, %s, %s, %s, %s, %s)"
        cursor.execute(insert_query, (username, password,full_name,phone_number,address,role_id))
        connection.commit()

        cursor.close()
        connection.close()

        flash('Nhân viên mới đã được thêm thành công!', 'success')
        return redirect(url_for('quan_ly_nhan_vien.quanlynhanvien'))
    return render_template('quan_li_nhan_vien/them_nhan_vien.html')

#SỬA NHÂN VIÊN
@nhanvien_blueprint.route('/sua_nhan_vien/<int:id>', methods=['GET', 'POST'])
def sua_nhan_vien(id):
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        full_name = request.form['full_name']
        phone_number = request.form['phone_number']
        address = request.form['address']
        
        update_query = """
            UPDATE account 
            SET username = %s, password = %s, full_name = %s, phone_number = %s, address = %s 
            WHERE id = %s
        """
        cursor.execute(update_query, (username, password, full_name, phone_number, address, id))
        
        # Nếu có bảng lương, cập nhật thông tin lương của nhân viên tại đây
        # Ví dụ: update_salary(id, salary_info)
        
        connection.commit()
        
        flash('Thông tin nhân viên đã được cập nhật!', 'success')
        return redirect(url_for('quan_ly_nhan_vien.quanlynhanvien'))
    
    cursor.execute("SELECT * FROM account WHERE id = %s", (id,))
    nhanvien = cursor.fetchone()
    
    cursor.close()
    connection.close()
    
    return render_template('quan_li_nhan_vien/sua_nhan_vien.html', nhanvien=nhanvien)
# XÓA NHÂN VIÊN
@nhanvien_blueprint.route('/quan_ly_nhan_vien.xoanhanvien/<int:id>', methods=['GET', 'POST'])
def xoa_nhan_vien(id):
    connection = get_db_connection()
    cursor = connection.cursor()

    try:
        # Kiểm tra và xóa các bản ghi liên quan trong bảng salary
        delete_salary_query = "DELETE FROM luong WHERE account_id = %s"
        cursor.execute(delete_salary_query, (id,))
        ## Kiểm tra và xóa các bản ghi liên quan trong bảng penalty
        delete_penalty_query = "DELETE FROM ca_lam_viec WHERE account_id = %s"
        cursor.execute(delete_penalty_query, (id,))
        
     
        # Tiếp tục xóa nhân viên từ bảng account
        delete_query_account = "DELETE FROM account WHERE id = %s"
        cursor.execute(delete_query_account, (id,))
        
        connection.commit()

        flash(f'Nhân Viên có ID {id} đã được xóa thành công!', 'success')
    except Exception as e:
        flash(f'Đã xảy ra lỗi khi xóa nhân viên: {str(e)}', 'error')
        connection.rollback()
    finally:
        cursor.close()
        connection.close()

    return redirect(url_for('quan_ly_nhan_vien.quanlynhanvien'))



#----------------------------
@nhanvien_blueprint.route('/phan_cong_viec')
def phan_cong_viec():
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute("""
        SELECT 
            clv.id,
            a.full_name, 
            clv.cong_viec, 
            clv.ngay_ca_lam, 
            clv.gio_bat_dau, 
            clv.gio_ket_thuc, 
            p.ly_do, 
            p.so_tien_phat
        FROM ca_lam_viec clv
        JOIN account a ON clv.account_id = a.id
        LEFT JOIN phat p ON clv.phat_id = p.id
    """)
    
    thong_tin = cursor.fetchall()
    
    cursor.close()
    conn.close()
    
    return render_template('quan_li_nhan_vien/phan_cong_viec.html', thong_tin=thong_tin)
@nhanvien_blueprint.route('/them_cong_viec', methods=['GET', 'POST'])
def them_cong_viec():
    if request.method == 'POST':
        account_id = request.form['account_id']
        cong_viec = request.form['cong_viec']
        ngay_ca_lam = request.form['ngay_ca_lam']
        gio_bat_dau = request.form['gio_bat_dau']
        gio_ket_thuc = request.form['gio_ket_thuc']
        
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            
            # Thực hiện INSERT vào bảng ca_lam_viec
            query = "INSERT INTO ca_lam_viec (account_id, cong_viec, ngay_ca_lam, gio_bat_dau, gio_ket_thuc) VALUES (%s, %s, %s, %s, %s)"
            cursor.execute(query, (account_id, cong_viec, ngay_ca_lam, gio_bat_dau, gio_ket_thuc))
            
            conn.commit()
            flash('Thêm công việc mới thành công', 'success')
            
        except mysql.connector.Error as e: # type: ignore
            print(f'Error: {e}')
            flash('Thêm công việc mới thất bại', 'error')
            
        finally:
            cursor.close()
            conn.close()
            
        return redirect(url_for('quan_ly_nhan_vien.phan_cong_viec'))
    
    # Lấy danh sách tài khoản để hiển thị trong dropdown
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, full_name FROM account")
    accounts = cursor.fetchall()
    cursor.close()
    conn.close()
    
    return render_template('quan_li_nhan_vien/them_cong_viec.html', accounts=accounts)
@nhanvien_blueprint.route('/sua_cong_viec/<int:id>', methods=['GET', 'POST'])
def sua_cong_viec(id):
    if request.method == 'POST':
        account_id = request.form['account_id']
        cong_viec = request.form['cong_viec']
        ngay_ca_lam = request.form['ngay_ca_lam']
        gio_bat_dau = request.form['gio_bat_dau']
        gio_ket_thuc = request.form['gio_ket_thuc']
        phat_id = request.form['phat_id'] if request.form['phat_id'] else None

        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            # Thực hiện UPDATE vào bảng ca_lam_viec
            query = """
                UPDATE ca_lam_viec 
                SET account_id = %s, cong_viec = %s, ngay_ca_lam = %s, gio_bat_dau = %s, gio_ket_thuc = %s, phat_id = %s 
                WHERE id = %s
            """
            cursor.execute(query, (account_id, cong_viec, ngay_ca_lam, gio_bat_dau, gio_ket_thuc, phat_id, id))

            conn.commit()
            flash('Cập nhật công việc thành công', 'success')

        except mysql.connector.Error as e: # type: ignore
            print(f'Error: {e}')
            flash('Cập nhật công việc thất bại', 'error')

        finally:
            cursor.close()
            conn.close()

        return redirect(url_for('quan_ly_nhan_vien.phan_cong_viec'))

    # Lấy thông tin công việc để hiển thị trong form
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT account_id, cong_viec, ngay_ca_lam, gio_bat_dau, gio_ket_thuc, phat_id FROM ca_lam_viec WHERE id = %s", (id,))
    cong_viec = cursor.fetchone()

    cursor.execute("SELECT id, full_name FROM account")
    accounts = cursor.fetchall()

    cursor.execute("SELECT id, ly_do FROM phat")
    phat = cursor.fetchall()

    cursor.close()
    conn.close()

    return render_template('quan_li_nhan_vien/sua_cong_viec.html', id=id, cong_viec=cong_viec, accounts=accounts, phat=phat)


@nhanvien_blueprint.route('/quan_ly_nhan_vien.xoa_cong_viec/<int:id>', methods=['POST'])
def xoa_cong_viec(id):
    
    if request.method == 'POST':
        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            # Thực hiện DELETE từ bảng ca_lam_viec
            query = "DELETE FROM ca_lam_viec WHERE id = %s"
            cursor.execute(query, (id,))

            conn.commit()
            flash('Xóa công việc thành công', 'success')

        except mysql.connector.Error as e: # type: ignore
            print(f'Error: {e}')
            flash('Xóa công việc thất bại', 'error')

        finally:
            cursor.close()
            conn.close()

        return redirect(url_for('quan_ly_nhan_vien.phan_cong_viec'))

    # Các xử lý khác khi request.method là GET hoặc những phương thức khác
    return redirect(url_for('quan_ly_nhan_vien.phan_cong_viec'))


@nhanvien_blueprint.route('/tim_kiem_cong_viec', methods=['GET', 'POST'])
def tim_kiem_cong_viec():
    if request.method == 'POST':
        search_term = request.form['search_term']
        conn = get_db_connection()
        cursor = conn.cursor()

        # Tìm kiếm các bản ghi trong bảng ca_lam_viec
        query = """
            SELECT a.full_name, clv.cong_viec, clv.ngay_ca_lam, clv.gio_bat_dau, clv.gio_ket_thuc, p.ly_do, p.so_tien_phat, clv.id
            FROM ca_lam_viec clv
            JOIN account a ON clv.account_id = a.id
            LEFT JOIN phat p ON clv.phat_id = p.id
            WHERE a.full_name LIKE %s OR clv.cong_viec LIKE %s OR p.ly_do LIKE %s
        """
        cursor.execute(query, (f"%{search_term}%", f"%{search_term}%", f"%{search_term}%"))
        thong_tin = cursor.fetchall()

        cursor.close()
        conn.close()

        return render_template('quan_li_nhan_vien/tim_kiem_cong_viec.html', thong_tin=thong_tin)

    return render_template('quan_li_nhan_vien/tim_kiem_cong_viec.html')


# Route để tính tổng lương và tổng số tiền phạt theo tháng/năm
@nhanvien_blueprint.route('/tong_luong_thang')
def tong_luong_thang():
    conn = get_db_connection()
    cur = conn.cursor()
    
    cur.execute("""
        SELECT 
            l.id,
            l.account_id,
            l.thang,
            l.nam,
            l.luong_co_ban,
            l.thuong,
            (l.luong_co_ban + IFNULL(l.thuong, 0) - IFNULL(p.so_tien_phat, 0)) AS tong_luong,
            IFNULL(SUM(p.so_tien_phat), 0) AS tong_so_tien_phat_thang
        FROM luong l
        JOIN ca_lam_viec clv ON l.account_id = clv.account_id
        LEFT JOIN phat p ON clv.phat_id = p.id AND MONTH(clv.ngay_ca_lam) = l.thang AND YEAR(clv.ngay_ca_lam) = l.nam
        GROUP BY l.id, l.account_id, l.thang, l.nam, l.luong_co_ban, l.thuong;
    """)
    
    tong_luong_thang = cur.fetchall()
    
    cur.close()
    conn.close()
    
    return render_template('quan_li_nhan_vien/tong_luong_thang.html', tong_luong_thang=tong_luong_thang)



# Route để tính tổng lương và tổng số tiền phạt theo năm
@nhanvien_blueprint.route('/tong_luong_nam')
def tong_luong_nam():
    conn = get_db_connection()
    cur = conn.cursor()
    
    cur.execute("""
SELECT 
    l.account_id,
    a.full_name,
    
    l.nam,
    SUM(DISTINCT l.luong_co_ban) AS tong_luong_co_ban,
    SUM(DISTINCT IFNULL(l.thuong, 0)) AS tong_thuong,
    SUM(DISTINCT IFNULL(p.so_tien_phat, 0)) AS tong_so_tien_phat_nam,
    SUM(DISTINCT l.luong_co_ban + IFNULL(l.thuong, 0) - IFNULL(p.so_tien_phat, 0)) AS tong_luong
FROM luong l
JOIN account a ON l.account_id = a.id
LEFT JOIN (
    SELECT 
        clv.account_id,
        YEAR(clv.ngay_ca_lam) AS nam,
        SUM(p.so_tien_phat) AS so_tien_phat
    FROM ca_lam_viec clv
    LEFT JOIN phat p ON clv.phat_id = p.id
    GROUP BY clv.account_id, YEAR(clv.ngay_ca_lam)
) p ON l.account_id = p.account_id AND l.nam = p.nam
GROUP BY l.account_id, l.nam
ORDER BY l.account_id, l.nam;

    """)
    
    tong_luong_nam = cur.fetchall()
    
    cur.close()
    conn.close()
    
    return render_template('quan_li_nhan_vien/tong_luong_nam.html', tong_luong_nam=tong_luong_nam)
