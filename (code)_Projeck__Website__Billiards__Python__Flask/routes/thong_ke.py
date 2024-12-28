import io
import json
from flask import Blueprint, jsonify, render_template, send_file, request, flash, redirect, url_for
from openpyxl import Workbook
from database import get_db_connection
thongke_blueprint = Blueprint('thong_ke', __name__)

#----------------QUẢN LÝ KHÁCH HÀNG----------------------
@thongke_blueprint.route('/quanlykhachhang')
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

#DOANH THU VÀ HÓA ĐƠN
def get_revenue_data(period):
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    if period == 'week':
        cursor.execute("""
            SELECT DATE(NgayTao) as date, SUM(TongTien) as revenue 
            FROM hoadon 
            WHERE NgayTao >= CURDATE() - INTERVAL 7 DAY 
            GROUP BY DATE(NgayTao)
        """)
    elif period == 'month':
        cursor.execute("""
            SELECT DATE_FORMAT(NgayTao, '%Y-%m-%d') as date, SUM(TongTien) as revenue 
            FROM hoadon 
            WHERE NgayTao >= CURDATE() - INTERVAL 1 MONTH 
            GROUP BY DATE_FORMAT(NgayTao, '%Y-%m-%d')
        """)
    elif period == 'year':
        cursor.execute("""
            SELECT DATE_FORMAT(NgayTao, '%Y-%m') as date, SUM(TongTien) as revenue 
            FROM hoadon 
            WHERE NgayTao >= CURDATE() - INTERVAL 1 YEAR 
            GROUP BY DATE_FORMAT(NgayTao, '%Y-%m')
        """)
    data = cursor.fetchall()
    cursor.close()
    connection.close()
    return data

def get_invoices():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("""
        SELECT h.*, m.TenMember 
        FROM hoadon h 
        LEFT JOIN member m ON h.MaMember = m.MaMember
    """)
    invoices = cursor.fetchall()
    cursor.close()
    connection.close()
    return invoices


@thongke_blueprint.route('/doanhthu')
def doanhthu():
    return render_template('quan_li_doanh_thu/doanhthu.html')

@thongke_blueprint.route('/revenue/<period>')
def revenue(period):
    data = get_revenue_data(period)
    return jsonify(data)

@thongke_blueprint.route('/invoices')
def invoices():
    invoices = get_invoices()
    return render_template('quan_li_doanh_thu/invoices.html', invoices=invoices)
#xem hóa đơn
@thongke_blueprint.route('/xemhoadon/<int:invoice_id>')
def xem_hoa_don(invoice_id):
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    

    cursor.execute("SELECT * FROM hoadon WHERE MaHoaDon = %s", (invoice_id,))
    hoadon = cursor.fetchone()
    
    if not hoadon:
        cursor.close()
        connection.close()
        return redirect(url_for('error_page'))
    

    if hoadon.get('MaMember'):
        cursor.execute("SELECT * FROM member WHERE MaMember = %s", (hoadon['MaMember'],))
        member = cursor.fetchone()
        hoadon['member'] = member  

    cursor.execute("""
        SELECT sp.TenSP, cto.SoLuong, sp.Gia 
        FROM chitietorder cto
        JOIN sanpham sp ON cto.MaSP = sp.MaSP
        WHERE cto.MaHoaDon = %s
    """, (invoice_id,))
    ordered_products = cursor.fetchall()
    
    cursor.close()
    connection.close()
    
    return render_template('quan_li_doanh_thu/xemhoadon.html', invoice=hoadon, ordered_products=ordered_products)


# Xuất hóa đơn
def get_invoice_details(invoice_id):
    connection = get_db_connection()  # Hàm này phải được cài đặt để kết nối với database của bạn
    cursor = connection.cursor(dictionary=True)
    cursor.execute("""
        SELECT h.MaHoaDon, h.MaBan, m.TenMember, h.TongTien, h.NgayTao
        FROM hoadon h
        LEFT JOIN member m ON h.MaMember = m.MaMember
        WHERE h.MaHoaDon = %s
    """, (invoice_id,))
    invoice = cursor.fetchone()
    cursor.close()
    connection.close()
    return invoice

# Route to export selected invoices to Excel
def get_invoice_details(invoice_id):
    connection = get_db_connection()  # Hàm này phải được cài đặt để kết nối với database của bạn
    cursor = connection.cursor(dictionary=True)
    cursor.execute("""
        SELECT h.MaHoaDon, h.MaBan, m.TenMember, h.TongTien, h.NgayTao
        FROM hoadon h
        LEFT JOIN member m ON h.MaMember = m.MaMember
        WHERE h.MaHoaDon = %s
    """, (invoice_id,))
    invoice = cursor.fetchone()
    cursor.close()
    connection.close()
    return invoice


@thongke_blueprint.route('/export_excel', methods=['GET'])
def export_excel():
    selected_invoices = json.loads(request.args.get('invoices'))

    if not selected_invoices:
        flash('Bạn chưa chọn hóa đơn nào để xuất Excel!', 'error')
        return redirect(url_for('thong_ke.invoices'))

    # Create a new Workbook and select the active worksheet
    wb = Workbook()
    ws = wb.active
    ws.title = 'DanhSachHoaDon'

    # Header row
    ws.append(['Mã Hóa Đơn', 'Mã Bàn', 'Tên Thành Viên', 'Tổng Tiền', 'Ngày Tạo'])

    # Data rows
    connection = get_db_connection()  # Assuming you have implemented this function correctly
    cursor = connection.cursor(dictionary=True)

    for invoice_id in selected_invoices:
        invoice = get_invoice_details(invoice_id)
        if invoice:
            ws.append([invoice['MaHoaDon'], invoice['MaBan'], invoice['TenMember'], invoice['TongTien'], invoice['NgayTao']])

    cursor.close()
    connection.close()

    # Create a BytesIO stream to save the workbook
    excel_io = io.BytesIO()
    wb.save(excel_io)
    excel_io.seek(0)

    # Set up the response to send the Excel file
    return send_file(
        excel_io,
        mimetype='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
        as_attachment=True,
        download_name='danh_sach_hoa_don.xlsx'  # Corrected argument name here
    )