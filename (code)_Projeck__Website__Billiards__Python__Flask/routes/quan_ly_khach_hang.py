from flask import Blueprint, render_template, redirect, url_for
from flask import request
from flask import flash
from database import get_db_connection
khachhang_blueprint = Blueprint('quan_ly_khach_hang', __name__)

@khachhang_blueprint.route('/quanlykhachang')





#----------------QUẢN LÝ KHÁCH HÀNG----------------------
@khachhang_blueprint.route('/quanlykhachhang')
def quanlykhachhang():
    
    keyword = request.args.get('keyword', '')

    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)

    if keyword:
        cursor.execute("SELECT * FROM member WHERE (TenMember LIKE %s OR SoDienThoai LIKE %s)", ('%' + keyword + '%', '%' + keyword + '%'))
    else:
        cursor.execute("SELECT * FROM member")

    khachhangs = cursor.fetchall()

    cursor.close()
    connection.close()

    return render_template('quan_li_khach_hang/khachhang.html', khachhangs=khachhangs) 
#THÊM KHÁCH HÀNG
@khachhang_blueprint.route('/quan_ly_khach_hang.themkhachhang', methods=['GET', 'POST'])
def them_khach_hang():
    
    
    if request.method == 'POST':
  
        TenMember = request.form['TenMember']
        DiaChi = request.form['DiaChi']
        SoDienThoai = request.form['SoDienThoai']
        Email = request.form['Email']
        
        connection = get_db_connection()
        cursor = connection.cursor()

        insert_query = "INSERT INTO member (TenMember, DiaChi, SoDienThoai,Email) VALUES (%s, %s, %s, %s)"
        cursor.execute(insert_query, (TenMember, DiaChi, SoDienThoai,Email))
        connection.commit()

        cursor.close()
        connection.close()

        flash('Khách Hàng mới đã được thêm thành công!', 'success')
        return redirect(url_for('quan_ly_khach_hang.quanlykhachhang'))
    return render_template('quan_li_khach_hang/them_khach_hang.html')


#SỬA KHÁCH HÀNG
@khachhang_blueprint.route('/sua_khach_hang/<int:MaMember>', methods=['GET', 'POST'])
def sua_khach_hang(MaMember):
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    
    if request.method == 'POST':
        TenMember = request.form['TenMember']
        DiaChi = request.form['DiaChi']
        SoDienThoai = request.form['SoDienThoai']
        Email = request.form['Email']
        update_query = "UPDATE member SET TenMember = %s, DiaChi = %s, SoDienThoai = %s, Email = %s WHERE MaMember = %s"
        cursor.execute(update_query, (TenMember, DiaChi, SoDienThoai,Email, MaMember))
        connection.commit()
        
        flash('Thông tin khách hàng đã được cập nhật!', 'success')
        return redirect(url_for('quan_ly_khach_hang.quanlykhachhang'))
    
    cursor.execute("SELECT * FROM member WHERE MaMember = %s", (MaMember,))
    khachhangs = cursor.fetchone()
    
    cursor.close()
    connection.close()
    
    return render_template('quan_li_khach_hang/sua_khach_hang.html', khachhang=khachhangs)

#XÓA KHÁCH HÀNG
@khachhang_blueprint.route('/quan_ly_khach_hang.xoakhachhang/<int:MaMember>', methods=['GET', 'POST'])
def xoa_khach_hang(MaMember):
    connection = get_db_connection()
    cursor = connection.cursor()


    cursor.execute("SELECT * FROM member WHERE MaMember = %s", (MaMember,))
    khachhang = cursor.fetchone()

    if khachhang:
        delete_query = "DELETE FROM member WHERE MaMember = %s"
        cursor.execute(delete_query, (MaMember,))
        connection.commit()

        flash(f'Khách Hàng có ID {MaMember} đã được xóa thành công!', 'success')
    else:
        flash(f'Khách Hàng có ID {MaMember} không tồn tại.', 'error')

    cursor.close()
    connection.close()

    return redirect(url_for('quan_ly_khach_hang.quanlykhachhang'))
