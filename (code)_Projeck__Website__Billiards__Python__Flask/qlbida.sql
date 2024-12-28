-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Máy chủ: localhost:3307
-- Thời gian đã tạo: Th12 28, 2024 lúc 04:57 AM
-- Phiên bản máy phục vụ: 10.4.32-MariaDB
-- Phiên bản PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Cơ sở dữ liệu: `qlbida`
--

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `account`
--

CREATE TABLE `account` (
  `id` int(11) NOT NULL,
  `username` varchar(50) NOT NULL,
  `password` varchar(255) NOT NULL,
  `full_name` varchar(100) DEFAULT NULL,
  `phone_number` varchar(15) DEFAULT NULL,
  `address` varchar(255) DEFAULT NULL,
  `role_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Đang đổ dữ liệu cho bảng `account`
--

INSERT INTO `account` (`id`, `username`, `password`, `full_name`, `phone_number`, `address`, `role_id`) VALUES
(1, '1', '1', '1', '1', '1', 1),
(2, '2', '2', '2', '2', '2', 3),
(3, '3', '3', '3', '3', '3', 2);

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `banbida1`
--

CREATE TABLE `banbida1` (
  `MaBan` int(11) NOT NULL,
  `TenBan` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  `LoaiBida` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  `TinhTrang` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Đang đổ dữ liệu cho bảng `banbida1`
--

INSERT INTO `banbida1` (`MaBan`, `TenBan`, `LoaiBida`, `TinhTrang`) VALUES
(1, 'Bàn số 1', 'Bida thường', 'Trống'),
(2, 'Bàn số 2', 'Bida nâng cao', 'Trống'),
(3, 'Bàn số 3', 'Bida thường', 'Có khách'),
(4, 'Bàn số 4', 'Bida thường', 'Có khách'),
(5, 'Bàn số 5', 'Bida nâng cao', 'Có khách'),
(6, 'Bàn số 6', 'Bida thường', 'Có khách'),
(8, '5', '7', 'Có khách');

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `ca_lam_viec`
--

CREATE TABLE `ca_lam_viec` (
  `id` int(11) NOT NULL,
  `account_id` int(11) NOT NULL,
  `phat_id` int(11) DEFAULT NULL,
  `cong_viec` text DEFAULT NULL,
  `ngay_ca_lam` date NOT NULL,
  `gio_bat_dau` time NOT NULL,
  `gio_ket_thuc` time NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Đang đổ dữ liệu cho bảng `ca_lam_viec`
--

INSERT INTO `ca_lam_viec` (`id`, `account_id`, `phat_id`, `cong_viec`, `ngay_ca_lam`, `gio_bat_dau`, `gio_ket_thuc`) VALUES
(1, 1, 1, 'Quản lý bàn bida', '2024-07-01', '08:00:00', '16:00:00'),
(2, 2, 2, 'Phục vụ khách hàng', '2024-07-02', '14:00:00', '22:00:00'),
(3, 3, 3, 'Vệ sinh phòng chơi', '2024-07-03', '18:00:00', '02:00:00'),
(4, 1, NULL, 'Quản lý nhân viên', '2024-07-04', '08:00:00', '16:00:00'),
(5, 2, NULL, 'Làm thêm giờ', '2024-07-05', '14:00:00', '22:00:00'),
(6, 3, NULL, 'Tiếp nhận đặt hàng', '2024-07-06', '18:00:00', '02:00:00'),
(7, 1, NULL, 'Xử lý thanh toán', '2024-07-07', '08:00:00', '16:00:00'),
(8, 2, NULL, 'Chăm sóc khách hàng', '2024-07-08', '14:00:00', '22:00:00'),
(9, 3, NULL, 'Làm việc với nhà cung cấp', '2024-07-09', '18:00:00', '02:00:00'),
(10, 1, NULL, 'Đào tạo nhân viên mới', '2024-07-10', '08:00:00', '16:00:00'),
(11, 2, NULL, 'Tổ chức sự kiện', '2024-07-11', '14:00:00', '22:00:00'),
(12, 3, NULL, 'Lập kế hoạch marketing', '2024-07-12', '18:00:00', '02:00:00'),
(13, 1, NULL, 'Thiết kế menu', '2024-07-13', '08:00:00', '16:00:00'),
(14, 2, NULL, 'Quản lý đơn hàng online', '2024-07-14', '14:00:00', '22:00:00'),
(15, 3, NULL, 'Bảo trì thiết bị', '2024-07-15', '18:00:00', '02:00:00');

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `chitietorder`
--

CREATE TABLE `chitietorder` (
  `MaOrder` int(11) NOT NULL,
  `MaHoaDon` int(11) NOT NULL,
  `MaBan` int(11) DEFAULT NULL,
  `MaSP` int(11) DEFAULT NULL,
  `SoLuong` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Đang đổ dữ liệu cho bảng `chitietorder`
--

INSERT INTO `chitietorder` (`MaOrder`, `MaHoaDon`, `MaBan`, `MaSP`, `SoLuong`) VALUES
(240, 4, NULL, 2, 3);

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `hoadon`
--

CREATE TABLE `hoadon` (
  `MaHoaDon` int(11) NOT NULL,
  `MaBan` int(11) DEFAULT NULL,
  `MaMember` int(11) DEFAULT NULL,
  `ThoiGianBatDau` datetime DEFAULT NULL,
  `ThoiGianKetThuc` datetime DEFAULT NULL,
  `ThanhTienThoigianchoi` decimal(18,2) DEFAULT NULL,
  `ThanhTienOrder` decimal(18,2) DEFAULT NULL,
  `TongTien` decimal(18,2) GENERATED ALWAYS AS (ifnull(`ThanhTienThoigianchoi`,0) + ifnull(`ThanhTienOrder`,0)) STORED,
  `NgayTao` datetime DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Đang đổ dữ liệu cho bảng `hoadon`
--

INSERT INTO `hoadon` (`MaHoaDon`, `MaBan`, `MaMember`, `ThoiGianBatDau`, `ThoiGianKetThuc`, `ThanhTienThoigianchoi`, `ThanhTienOrder`, `NgayTao`) VALUES
(1, 1, 1, '2024-07-01 10:00:00', '2024-07-01 12:00:00', 100000.00, 150000.00, '2024-07-01 12:30:00'),
(2, 2, 2, '2024-07-02 11:00:00', '2024-07-02 13:00:00', 120000.00, 200000.00, '2024-07-02 13:30:00'),
(3, 1, NULL, '2024-12-19 07:53:13', '2024-12-19 07:59:06', 35300.00, NULL, '2024-12-19 07:53:13'),
(4, 3, 5, '2024-12-19 07:53:18', '2024-12-19 07:54:11', 5300.00, 75000.00, '2024-12-19 07:53:18'),
(5, 4, NULL, '2024-12-19 07:54:31', NULL, NULL, NULL, '2024-12-19 07:54:31'),
(6, 6, 5, '2024-12-19 07:54:35', '2024-12-19 07:56:12', 9700.00, NULL, '2024-12-19 07:54:35'),
(7, 3, NULL, '2024-12-19 07:55:49', NULL, NULL, NULL, '2024-12-19 07:55:49'),
(8, 8, NULL, '2024-12-19 07:56:29', NULL, NULL, NULL, '2024-12-19 07:56:29'),
(9, 5, NULL, '2024-12-19 07:57:37', NULL, NULL, NULL, '2024-12-19 07:57:37'),
(10, 6, NULL, '2024-12-19 07:57:40', NULL, NULL, NULL, '2024-12-19 07:57:40'),
(11, 2, NULL, '2024-12-19 07:59:23', '2024-12-19 07:59:24', 100.00, NULL, '2024-12-19 07:59:23');

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `luong`
--

CREATE TABLE `luong` (
  `id` int(11) NOT NULL,
  `account_id` int(11) NOT NULL,
  `thang` int(2) NOT NULL,
  `nam` int(4) NOT NULL,
  `luong_co_ban` decimal(10,2) NOT NULL,
  `thuong` decimal(10,2) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Đang đổ dữ liệu cho bảng `luong`
--

INSERT INTO `luong` (`id`, `account_id`, `thang`, `nam`, `luong_co_ban`, `thuong`) VALUES
(1, 1, 7, 2024, 15000000.00, 2000000.00),
(2, 2, 7, 2024, 12000000.00, 1500000.00),
(3, 3, 7, 2024, 10000000.00, 1000000.00),
(4, 1, 6, 2024, 15000000.00, 2000000.00),
(5, 2, 6, 2024, 12000000.00, 1500000.00);

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `member`
--

CREATE TABLE `member` (
  `MaMember` int(11) NOT NULL,
  `TenMember` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `DiaChi` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  `SoDienThoai` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  `Email` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Đang đổ dữ liệu cho bảng `member`
--

INSERT INTO `member` (`MaMember`, `TenMember`, `DiaChi`, `SoDienThoai`, `Email`) VALUES
(1, 'Nguyễn Thị Khách Hàng', '123 Đường ABC, Quận XYZ', '0987654321', 'nguyenthikhachhang@example.com'),
(2, 'Trần Văn Thành Viên', '456 Đường XYZ, Quận ABC', '0123456789', 'tranvanthanhvien@example.com'),
(3, 'Lê Thị Lan', '789 Đường XYZ, Quận XYZ', '0909090909', 'lethilan@example.com'),
(4, 'Phạm Văn Nam', '321 Đường XYZ, Quận XYZ', '0988888888', 'phamvannam@example.com'),
(5, 'Hoàng Thị Hồng', '567 Đường XYZ, Quận ABC', '0123456789', 'hoangthihong@example.com'),
(6, 'Trần Văn Hùng', '678 Đường ABC, Quận XYZ', '0909090909', 'tranvanhung@example.com');

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `phat`
--

CREATE TABLE `phat` (
  `id` int(11) NOT NULL,
  `ly_do` varchar(255) NOT NULL,
  `so_tien_phat` decimal(10,2) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Đang đổ dữ liệu cho bảng `phat`
--

INSERT INTO `phat` (`id`, `ly_do`, `so_tien_phat`) VALUES
(1, 'Quên làm việc', 100000.00),
(2, 'Đi muộn', 50000.00),
(3, 'Làm việc không chính xác', 70000.00),
(4, 'Không đeo đồ bảo hộ', 80000.00);

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `role`
--

CREATE TABLE `role` (
  `id` int(11) NOT NULL,
  `name` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Đang đổ dữ liệu cho bảng `role`
--

INSERT INTO `role` (`id`, `name`) VALUES
(1, 'Admin'),
(2, 'User'),
(3, 'khách hàng');

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `sanpham`
--

CREATE TABLE `sanpham` (
  `MaSP` int(11) NOT NULL,
  `TenSP` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  `Gia` decimal(10,2) DEFAULT NULL,
  `SoLuong` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Đang đổ dữ liệu cho bảng `sanpham`
--

INSERT INTO `sanpham` (`MaSP`, `TenSP`, `Gia`, `SoLuong`) VALUES
(1, 'Cà phê đen', 200040.00, 92),
(2, 'Trà sữa trân châu', 25000.00, 20),
(3, 'Nước ngọt Coca-Cola', 15000.00, 72),
(4, 'Bánh mì sandwich', 30000.00, 6),
(5, 'Hamburger', 35000.00, 19),
(6, 'Pizza hải sản', 40000.00, 16),
(7, 'Nước ép cam', 18000.00, 37),
(8, 'Bánh cookie sô cô la', 10000.00, 40),
(9, '3388', 443.01, 5488);

--
-- Chỉ mục cho các bảng đã đổ
--

--
-- Chỉ mục cho bảng `account`
--
ALTER TABLE `account`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`),
  ADD KEY `role_id` (`role_id`);

--
-- Chỉ mục cho bảng `banbida1`
--
ALTER TABLE `banbida1`
  ADD PRIMARY KEY (`MaBan`);

--
-- Chỉ mục cho bảng `ca_lam_viec`
--
ALTER TABLE `ca_lam_viec`
  ADD PRIMARY KEY (`id`),
  ADD KEY `account_id` (`account_id`),
  ADD KEY `ca_lam_viec_FK_phat` (`phat_id`);

--
-- Chỉ mục cho bảng `chitietorder`
--
ALTER TABLE `chitietorder`
  ADD PRIMARY KEY (`MaOrder`),
  ADD KEY `MaBan` (`MaBan`),
  ADD KEY `MaSP` (`MaSP`),
  ADD KEY `hoadon_chitiet` (`MaHoaDon`);

--
-- Chỉ mục cho bảng `hoadon`
--
ALTER TABLE `hoadon`
  ADD PRIMARY KEY (`MaHoaDon`),
  ADD KEY `fk_hd_mm` (`MaMember`),
  ADD KEY `fk_hd_ban` (`MaBan`);

--
-- Chỉ mục cho bảng `luong`
--
ALTER TABLE `luong`
  ADD PRIMARY KEY (`id`),
  ADD KEY `account_id` (`account_id`);

--
-- Chỉ mục cho bảng `member`
--
ALTER TABLE `member`
  ADD PRIMARY KEY (`MaMember`);

--
-- Chỉ mục cho bảng `phat`
--
ALTER TABLE `phat`
  ADD PRIMARY KEY (`id`);

--
-- Chỉ mục cho bảng `role`
--
ALTER TABLE `role`
  ADD PRIMARY KEY (`id`);

--
-- Chỉ mục cho bảng `sanpham`
--
ALTER TABLE `sanpham`
  ADD PRIMARY KEY (`MaSP`);

--
-- AUTO_INCREMENT cho các bảng đã đổ
--

--
-- AUTO_INCREMENT cho bảng `account`
--
ALTER TABLE `account`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=33;

--
-- AUTO_INCREMENT cho bảng `banbida1`
--
ALTER TABLE `banbida1`
  MODIFY `MaBan` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT cho bảng `ca_lam_viec`
--
ALTER TABLE `ca_lam_viec`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;

--
-- AUTO_INCREMENT cho bảng `chitietorder`
--
ALTER TABLE `chitietorder`
  MODIFY `MaOrder` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=241;

--
-- AUTO_INCREMENT cho bảng `hoadon`
--
ALTER TABLE `hoadon`
  MODIFY `MaHoaDon` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- AUTO_INCREMENT cho bảng `luong`
--
ALTER TABLE `luong`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT cho bảng `member`
--
ALTER TABLE `member`
  MODIFY `MaMember` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT cho bảng `phat`
--
ALTER TABLE `phat`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT cho bảng `sanpham`
--
ALTER TABLE `sanpham`
  MODIFY `MaSP` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- Các ràng buộc cho các bảng đã đổ
--

--
-- Các ràng buộc cho bảng `account`
--
ALTER TABLE `account`
  ADD CONSTRAINT `account_ibfk_1` FOREIGN KEY (`role_id`) REFERENCES `role` (`id`);

--
-- Các ràng buộc cho bảng `ca_lam_viec`
--
ALTER TABLE `ca_lam_viec`
  ADD CONSTRAINT `ca_lam_viec_FK_phat` FOREIGN KEY (`phat_id`) REFERENCES `phat` (`id`),
  ADD CONSTRAINT `ca_lam_viec_ibfk_1` FOREIGN KEY (`account_id`) REFERENCES `account` (`id`);

--
-- Các ràng buộc cho bảng `chitietorder`
--
ALTER TABLE `chitietorder`
  ADD CONSTRAINT `chitiet_sanpham` FOREIGN KEY (`MaSP`) REFERENCES `sanpham` (`MaSP`),
  ADD CONSTRAINT `hoadon_chitiet` FOREIGN KEY (`MaHoaDon`) REFERENCES `hoadon` (`MaHoaDon`);

--
-- Các ràng buộc cho bảng `hoadon`
--
ALTER TABLE `hoadon`
  ADD CONSTRAINT `fk_hd_ban` FOREIGN KEY (`MaBan`) REFERENCES `banbida1` (`MaBan`),
  ADD CONSTRAINT `fk_hd_mm` FOREIGN KEY (`MaMember`) REFERENCES `member` (`MaMember`);

--
-- Các ràng buộc cho bảng `luong`
--
ALTER TABLE `luong`
  ADD CONSTRAINT `luong_ibfk_1` FOREIGN KEY (`account_id`) REFERENCES `account` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
