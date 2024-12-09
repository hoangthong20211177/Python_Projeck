from flask import Blueprint, jsonify, render_template, redirect, url_for
from flask import request
from flask import flash
from db import get_db_connection
ban_blueprint = Blueprint('quan_ly_ban', __name__)

@ban_blueprint.route('/quanlybillards')
def quanlybillards():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM banbida1")
    tables = cursor.fetchall()
    cursor.close()
    connection.close()
    return render_template('quan_li_ban_bia/banbia.html', tables=tables)



@ban_blueprint.route('/chitiethoadon/<int:ma_ban>')
def chitiethoadon(ma_ban):
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    


    cursor.execute("""
    SELECT h.*, b.TenBan 
    FROM hoadon h
    JOIN banbida1 b ON h.MaBan = b.MaBan
    WHERE h.MaBan = %s 
    ORDER BY h.NgayTao DESC 
    LIMIT 1
    """, (ma_ban,))
    hoadon = cursor.fetchone()

    
    if not hoadon:
        cursor.close()
        connection.close()
        return redirect(url_for('quan_ly_ban.quanlybillards'))
    

    cursor.execute("""
        SELECT sp.TenSP, cto.SoLuong, sp.Gia 
        FROM chitietorder cto
        JOIN sanpham sp ON cto.MaSP = sp.MaSP
        WHERE cto.MaHoaDon = %s
    """, (hoadon['MaHoaDon'],))
    ordered_products = cursor.fetchall()
    
    
    cursor.execute("SELECT * FROM sanpham")
    products = cursor.fetchall()
    
    cursor.close()
    connection.close()
    
    return render_template('quan_li_ban_bia/invoice_details.html', hoadon=hoadon, ordered_products=ordered_products, products=products)

@ban_blueprint.route('/add_to_order', methods=['POST'])
def add_to_order():
    ma_hoa_don = request.form['MaHoaDon']
    ma_sp = request.form['MaSP']
    so_luong = int(request.form['SoLuong'])

    connection = get_db_connection()
    cursor = connection.cursor()

    try:

        cursor.execute("SELECT * FROM chitietorder WHERE MaHoaDon = %s AND MaSP = %s", (ma_hoa_don, ma_sp))
        order_item = cursor.fetchone()

        if order_item:

            cursor.execute("UPDATE chitietorder SET SoLuong = SoLuong + %s WHERE MaHoaDon = %s AND MaSP = %s", (so_luong, ma_hoa_don, ma_sp))
        else:

            cursor.execute("INSERT INTO chitietorder (MaHoaDon, MaSP, SoLuong) VALUES (%s, %s, %s)", (ma_hoa_don, ma_sp, so_luong))


        cursor.execute("UPDATE sanpham SET SoLuong = SoLuong - %s WHERE MaSP = %s", (so_luong, ma_sp))

        connection.commit()
        cursor.close()
        connection.close()

        return redirect(url_for('quan_ly_ban.chitiethoadon', ma_ban=request.form['MaBan']))

    except Exception as e:
        print(f"Error: {e}")
        cursor.close()
        connection.close()
        return redirect(url_for('error_page'))

@ban_blueprint.route('/tao_hoadon', methods=['POST'])
def tao_hoadon():
    MaBan = request.form.get('MaBan')
    

    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM banbida1 WHERE MaBan = %s AND TinhTrang = 'Trống'", (MaBan,))
    table = cursor.fetchone()
    
    if table:

        cursor.execute(
            "INSERT INTO hoadon (MaBan, ThoiGianBatDau) VALUES (%s, NOW())",
            (MaBan,)
        )
        connection.commit()
        

        new_invoice_id = cursor.lastrowid
        

        cursor.execute(
            "UPDATE banbida1 SET TinhTrang = 'Có khách' WHERE MaBan = %s",
            (MaBan,)
        )
        connection.commit()
        
        cursor.close()
        connection.close()
        

        return redirect(url_for('quan_ly_ban.chitiethoadon', ma_ban=MaBan))
    
    cursor.close()
    connection.close()
    
    return redirect(url_for('quan_ly_ban.quanlybillards'))

@ban_blueprint.route('/ket_thuc_hoadon', methods=['POST'])
def ket_thuc_hoadon():
    MaHoaDon = request.form.get('MaHoaDon')
    
    connection = get_db_connection()
    cursor = connection.cursor()
    
    try:

        cursor.execute("UPDATE hoadon SET ThoiGianKetThuc = NOW() WHERE MaHoaDon = %s", (MaHoaDon,))
        

        cursor.execute("UPDATE hoadon SET ThanhTienThoigianchoi = TIMESTAMPDIFF(SECOND, ThoiGianBatDau, NOW()) * 100 WHERE MaHoaDon = %s", (MaHoaDon,))

        cursor.execute("SELECT SUM(chitietorder.SoLuong * sanpham.Gia) AS TongTien FROM chitietorder JOIN sanpham ON chitietorder.MaSP = sanpham.MaSP WHERE chitietorder.MaHoaDon = %s", (MaHoaDon,))
        tong_tien = cursor.fetchone()[0]
        
        cursor.execute("UPDATE hoadon SET ThanhTienOrder = %s, TongTien = ThanhTienThoigianchoi + ThanhTienOrder WHERE MaHoaDon = %s", (tong_tien, MaHoaDon,))
        

        cursor.execute("UPDATE banbida1 SET TinhTrang = 'Trống' WHERE MaBan IN (SELECT MaBan FROM hoadon WHERE MaHoaDon = %s)", (MaHoaDon,))
        
        connection.commit()
        cursor.close()
        connection.close()
        

        return redirect(url_for('quan_ly_ban.select_member', invoice_id=MaHoaDon))
    
    except Exception as e:

        print(f"Error: {e}")
        cursor.close()
        connection.close()

        return redirect(url_for('error_page'))

@ban_blueprint.route('/select_member/<int:invoice_id>')
def select_member(invoice_id):
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    

    cursor.execute("SELECT * FROM hoadon WHERE MaHoaDon = %s", (invoice_id,))
    hoadon = cursor.fetchone()
    
    if not hoadon:
        cursor.close()
        connection.close()
        return redirect(url_for('index'))

    cursor.execute("SELECT * FROM member")
    members = cursor.fetchall()
    
    cursor.close()
    connection.close()
    
    return render_template('select_member.html', hoadon=hoadon, members=members)

@ban_blueprint.route('/update_invoice_member', methods=['POST'])
def update_invoice_member():
    MaHoaDon = request.form.get('MaHoaDon')
    MaMember = request.form.get('MaMember')
    
    connection = get_db_connection()
    cursor = connection.cursor()
    
    cursor.execute("UPDATE hoadon SET MaMember = %s WHERE MaHoaDon = %s", (MaMember, MaHoaDon))
    
    connection.commit()
    cursor.close()
    connection.close()
    return redirect(url_for('quan_ly_ban.quanlybillards'))
@ban_blueprint.route('/search_member')
def search_member():
    search_query = request.args.get('q', '')
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    
    cursor.execute("SELECT * FROM member WHERE TenMember LIKE %s", ('%' + search_query + '%',))
    members = cursor.fetchall()
    
    cursor.close()
    connection.close()

    return jsonify(members)

#THÊM BÀN
@ban_blueprint.route('/themban', methods=['GET', 'POST'])
def them_ban():
    if request.method == 'POST':
        ten_ban = request.form['ten_ban']
        loai_bida = request.form['loai_bida']
        tinh_trang = request.form['tinh_trang']
        
        connection = get_db_connection()
        cursor = connection.cursor()

        insert_query = "INSERT INTO banbida1 (TenBan, LoaiBida, TinhTrang) VALUES (%s, %s, %s)"
        cursor.execute(insert_query, (ten_ban, loai_bida, tinh_trang))
        connection.commit()

        cursor.close()
        connection.close()

        flash('Bàn mới đã được thêm thành công!', 'success')
        return redirect(url_for('quan_ly_ban.quanlybillards'))

    return render_template('quan_li_ban_bia/them_ban.html')

#XÓA BÀN
@ban_blueprint.route('/xoaban/<int:ma_ban>', methods=['GET', 'POST'])
def xoa_ban(ma_ban):
    connection = get_db_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM banbida1 WHERE MaBan = %s", (ma_ban,))
    table = cursor.fetchone()

    if table:
        delete_query = "DELETE FROM banbida1 WHERE MaBan = %s"
        cursor.execute(delete_query, (ma_ban,))
        connection.commit()

        flash(f'Bàn có ID {ma_ban} đã được xóa thành công!', 'success')
    else:
        flash(f'Bàn có ID {ma_ban} không tồn tại.', 'error')

    cursor.close()
    connection.close()

    return redirect(url_for('quan_ly_ban.quanlybillards'))
