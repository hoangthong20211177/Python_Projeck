from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask import request
from flask import flash
from db import get_db_connection

sanpham_blueprint = Blueprint('quan_ly_san_pham', __name__)

@sanpham_blueprint.route('/quanlysanpham')






#----------------QUẢN LÝ SẢN PHẨM----------------------
@sanpham_blueprint.route('/quanlysanpham')
def quanlysanpham():
    
    keyword = request.args.get('keyword', '')

    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)

    if keyword:
        cursor.execute("SELECT * FROM sanpham WHERE (TenSP LIKE %s)", ('%' + keyword + '%',))
    else:
        cursor.execute("SELECT * FROM sanpham")

    sanphams = cursor.fetchall()

    cursor.close()
    connection.close()

    return render_template('quan_li_san_pham/sanpham.html', sanphams=sanphams)

#THÊM SẢN PHẨM
@sanpham_blueprint.route('/themsanpham', methods=['GET', 'POST'])
def them_san_pham():
    
    
    if request.method == 'POST':
  
        TenSP = request.form['TenSP']
        Gia = request.form['Gia']
        SoLuong = request.form['SoLuong']
        
        connection = get_db_connection()
        cursor = connection.cursor()

        insert_query = "INSERT INTO sanpham (TenSP, Gia, SoLuong) VALUES (%s, %s, %s)"
        cursor.execute(insert_query, (TenSP, Gia, SoLuong))
        connection.commit()

        cursor.close()
        connection.close()

        flash('Sản phẩm mới đã được thêm thành công!', 'success')
        return redirect(url_for('quan_ly_san_pham.quanlysanpham'))
    return render_template('quan_li_san_pham/them_san_pham.html')

#SỬA SẢN PHẨM
@sanpham_blueprint.route('/suasanpham/<int:MaSP>', methods=['GET', 'POST'])
def sua_san_pham(MaSP):
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    
    if request.method == 'POST':
        TenSP = request.form['TenSP']
        Gia = request.form['Gia']
        SoLuong = request.form['SoLuong']
        update_query = "UPDATE sanpham SET TenSP = %s, Gia = %s, SoLuong = %s WHERE MaSP = %s"
        cursor.execute(update_query, (TenSP, Gia, SoLuong, MaSP))
        connection.commit()
        
        flash('Thông tin sản phẩm đã được cập nhật!', 'success')
        return redirect(url_for('quan_ly_san_pham.quanlysanpham'))
    
    cursor.execute("SELECT * FROM sanpham WHERE MaSP = %s", (MaSP,))
    sanpham = cursor.fetchone()
    
    cursor.close()
    connection.close()
    
    return render_template('quan_li_san_pham/sua_san_pham.html', sanpham=sanpham)
@sanpham_blueprint.route('/xoasanpham/<int:MaSP>', methods=['GET', 'POST'])
def xoa_san_pham(MaSP):
    connection = get_db_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM sanpham WHERE MaSP = %s", (MaSP,))
    sanpham = cursor.fetchone()

    if sanpham:
        delete_query = "DELETE FROM sanpham WHERE MaSP = %s"
        cursor.execute(delete_query, (MaSP,))
        connection.commit()

        flash(f'Sản phẩm có ID {MaSP} đã được xóa thành công!', 'success')
    else:
        flash(f'Sản phẩm có ID {MaSP} không tồn tại.', 'error')

    cursor.close()
    connection.close()

    return redirect(url_for('quan_ly_san_pham.quanlysanpham'))
