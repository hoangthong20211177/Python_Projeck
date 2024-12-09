-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3307
-- Generation Time: Jul 09, 2024 at 04:13 PM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `qlbida`
--

-- --------------------------------------------------------

--
-- Table structure for table `account`
--

CREATE TABLE `account` (
  `id` int(11) NOT NULL,
  `username` varchar(50) NOT NULL,
  `password` varchar(20) NOT NULL,
  `full_name` varchar(30) DEFAULT NULL,
  `phone_number` varchar(15) DEFAULT NULL,
  `address` varchar(100) DEFAULT NULL,
  `role_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `account`
--

INSERT INTO `account` (`id`, `username`, `password`, `full_name`, `phone_number`, `address`, `role_id`) VALUES
(2, '2', '2', '2', '2', '2', 1),
(45, '123', '353', '5345', '345', '234', 1),
(46, '456tT545', '5674tT%33', '678', '456', '56', 2);

-- --------------------------------------------------------

--
-- Table structure for table `banbida1`
--

CREATE TABLE `banbida1` (
  `MaBan` int(11) NOT NULL,
  `TenBan` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  `LoaiBida` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  `TinhTrang` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `banbida1`
--

INSERT INTO `banbida1` (`MaBan`, `TenBan`, `LoaiBida`, `TinhTrang`) VALUES
(1, 'Bàn số 1', 'Bida thường', 'Trống'),
(2, 'Bàn số 2', 'Bida nâng cao', 'Trống'),
(3, 'Bàn số 3', 'Bida thường', 'Có khách'),
(4, 'Bàn số 4', 'Bida thường', 'Có khách'),
(6, 'Bàn số 6', 'Bida thường', 'Trống'),
(8, 'b77', '676', '67'),
(9, 'b77', '676', '67'),
(10, '56y', 'h', 'r5'),
(11, '56y', 'h', 'r5'),
(12, '4', '56', '8'),
(13, '4', '56', '8'),
(14, '99', '99', '99');

-- --------------------------------------------------------

--
-- Table structure for table `ca_lam_viec`
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
-- Dumping data for table `ca_lam_viec`
--

INSERT INTO `ca_lam_viec` (`id`, `account_id`, `phat_id`, `cong_viec`, `ngay_ca_lam`, `gio_bat_dau`, `gio_ket_thuc`) VALUES
(5, 2, NULL, 'Làm thêm giờ', '2024-07-05', '14:00:00', '22:00:00'),
(8, 2, NULL, 'Chăm sóc khách hàng', '2024-07-08', '14:00:00', '22:00:00'),
(11, 2, NULL, 'Tổ chức sự kiện', '2024-07-11', '14:00:00', '22:00:00'),
(14, 2, NULL, 'Quản lý đơn hàng online', '2024-07-14', '14:00:00', '22:00:00');

-- --------------------------------------------------------

--
-- Table structure for table `chitietorder`
--

CREATE TABLE `chitietorder` (
  `MaOrder` int(11) NOT NULL,
  `MaHoaDon` int(11) NOT NULL,
  `MaBan` int(11) DEFAULT NULL,
  `MaSP` int(11) DEFAULT NULL,
  `SoLuong` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `chitietorder`
--

INSERT INTO `chitietorder` (`MaOrder`, `MaHoaDon`, `MaBan`, `MaSP`, `SoLuong`) VALUES
(240, 2, NULL, 1, 1),
(241, 3, NULL, 1, 4),
(242, 3, NULL, 2, 1),
(243, 7, NULL, 1, 1),
(244, 8, NULL, 4, 1);

-- --------------------------------------------------------

--
-- Table structure for table `hoadon`
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
-- Dumping data for table `hoadon`
--

INSERT INTO `hoadon` (`MaHoaDon`, `MaBan`, `MaMember`, `ThoiGianBatDau`, `ThoiGianKetThuc`, `ThanhTienThoigianchoi`, `ThanhTienOrder`, `NgayTao`) VALUES
(1, 1, 1, '2024-07-01 10:00:00', '2024-07-01 12:00:00', 100000.00, 150000.00, '2024-07-01 12:30:00'),
(2, 2, 2, '2024-07-02 11:00:00', '2024-07-07 13:38:35', 44151500.00, 200040.00, '2024-07-02 13:30:00'),
(3, 1, 2, '2024-07-07 12:15:39', '2024-07-08 11:59:10', 8541100.00, 825160.00, '2024-07-07 12:15:39'),
(4, 6, NULL, '2024-07-08 11:59:48', '2024-07-08 21:32:39', 3437100.00, NULL, '2024-07-08 11:59:48'),
(5, 2, 1, '2024-07-08 11:59:51', '2024-07-08 12:01:28', 9700.00, NULL, '2024-07-08 11:59:51'),
(6, 1, 1, '2024-07-08 12:00:33', '2024-07-08 12:00:43', 1000.00, NULL, '2024-07-08 12:00:33'),
(7, 1, 1, '2024-07-08 12:01:21', '2024-07-08 12:11:56', 63500.00, 200040.00, '2024-07-08 12:01:21'),
(8, 4, NULL, '2024-07-08 12:12:56', '2024-07-08 21:31:27', 3351100.00, 30000.00, '2024-07-08 12:12:56'),
(9, 3, 1, '2024-07-08 12:13:00', '2024-07-08 12:19:28', 38800.00, NULL, '2024-07-08 12:13:00'),
(10, 2, 1, '2024-07-08 12:13:03', '2024-07-08 12:19:23', 38000.00, NULL, '2024-07-08 12:13:03'),
(11, 1, NULL, '2024-07-08 12:19:19', '2024-07-08 21:32:23', 3318400.00, NULL, '2024-07-08 12:19:19'),
(12, 2, NULL, '2024-07-08 21:30:37', '2024-07-08 21:31:55', 7800.00, NULL, '2024-07-08 21:30:37'),
(13, 4, NULL, '2024-07-08 21:32:26', NULL, NULL, NULL, '2024-07-08 21:32:26'),
(14, 3, NULL, '2024-07-08 21:33:32', '2024-07-08 21:33:50', 1800.00, NULL, '2024-07-08 21:33:32'),
(15, 3, NULL, '2024-07-08 21:40:36', NULL, NULL, NULL, '2024-07-08 21:40:36');

-- --------------------------------------------------------

--
-- Table structure for table `luong`
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
-- Dumping data for table `luong`
--

INSERT INTO `luong` (`id`, `account_id`, `thang`, `nam`, `luong_co_ban`, `thuong`) VALUES
(2, 2, 7, 2024, 12000000.00, 1500000.00),
(5, 2, 6, 2024, 12000000.00, 1500000.00);

-- --------------------------------------------------------

--
-- Table structure for table `member`
--

CREATE TABLE `member` (
  `MaMember` int(11) NOT NULL,
  `TenMember` varchar(25) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `DiaChi` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  `SoDienThoai` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  `Email` varchar(30) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `member`
--

INSERT INTO `member` (`MaMember`, `TenMember`, `DiaChi`, `SoDienThoai`, `Email`) VALUES
(1, 'Nguyễn Thị Khách Hàng6', '123 Đường ABC, Quận XYZ6', '09876543216', 'nguyenthikhachhang@example.com'),
(2, 'Trần Văn Thành Viên', '456 Đường XYZ, Quận ABC', '0123456789', 'tranvanthanhvien@example.com'),
(3, 'Lê Thị Lan', '789 Đường XYZ, Quận XYZ', '0909090909', 'lethilan@example.com'),
(4, 'Phạm Văn Nam', '321 Đường XYZ, Quận XYZ', '0988888888', 'phamvannam@example.com'),
(5, 'Hoàng Thị Hồng', '567 Đường XYZ, Quận ABC', '0123456789', 'hoangthihong@example.com');

-- --------------------------------------------------------

--
-- Table structure for table `phat`
--

CREATE TABLE `phat` (
  `id` int(11) NOT NULL,
  `ly_do` varchar(100) NOT NULL,
  `so_tien_phat` decimal(10,2) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `phat`
--

INSERT INTO `phat` (`id`, `ly_do`, `so_tien_phat`) VALUES
(1, 'Quên làm việc', 100000.00),
(2, 'Đi muộn', 50000.00),
(3, 'Làm việc không chính xác', 70000.00),
(4, 'Không đeo đồ bảo hộ', 80000.00);

-- --------------------------------------------------------

--
-- Table structure for table `role`
--

CREATE TABLE `role` (
  `id` int(11) NOT NULL,
  `name` varchar(15) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `role`
--

INSERT INTO `role` (`id`, `name`) VALUES
(1, 'Admin'),
(2, 'User'),
(3, 'khách hàng');

-- --------------------------------------------------------

--
-- Table structure for table `sanpham`
--

CREATE TABLE `sanpham` (
  `MaSP` int(11) NOT NULL,
  `TenSP` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  `Gia` decimal(10,2) DEFAULT NULL,
  `SoLuong` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `sanpham`
--

INSERT INTO `sanpham` (`MaSP`, `TenSP`, `Gia`, `SoLuong`) VALUES
(1, 'Cà phê đen', 200040.00, 9151),
(2, 'Trà sữa trân châu', 25000.00, 22),
(3, 'Nước ngọt Coca-Cola', 15000.00, 72),
(4, 'Bánh mì sandwich', 30000.00, 5),
(5, 'Hamburger', 35000.00, 19),
(6, 'Pizza hải sản', 40000.00, 16),
(7, 'Nước ép cam', 18000.00, 37),
(8, 'Bánh cookie sô cô la', 10000.00, 40),
(14, '567', 6876.00, 7897),
(15, '456', 5656.00, 565);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `account`
--
ALTER TABLE `account`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`),
  ADD KEY `role_id` (`role_id`);

--
-- Indexes for table `banbida1`
--
ALTER TABLE `banbida1`
  ADD PRIMARY KEY (`MaBan`);

--
-- Indexes for table `ca_lam_viec`
--
ALTER TABLE `ca_lam_viec`
  ADD PRIMARY KEY (`id`),
  ADD KEY `account_id` (`account_id`),
  ADD KEY `ca_lam_viec_FK_phat` (`phat_id`);

--
-- Indexes for table `chitietorder`
--
ALTER TABLE `chitietorder`
  ADD PRIMARY KEY (`MaOrder`),
  ADD KEY `MaBan` (`MaBan`),
  ADD KEY `MaSP` (`MaSP`),
  ADD KEY `hoadon_chitiet` (`MaHoaDon`);

--
-- Indexes for table `hoadon`
--
ALTER TABLE `hoadon`
  ADD PRIMARY KEY (`MaHoaDon`),
  ADD KEY `fk_hd_mm` (`MaMember`),
  ADD KEY `fk_hd_ban` (`MaBan`);

--
-- Indexes for table `luong`
--
ALTER TABLE `luong`
  ADD PRIMARY KEY (`id`),
  ADD KEY `account_id` (`account_id`);

--
-- Indexes for table `member`
--
ALTER TABLE `member`
  ADD PRIMARY KEY (`MaMember`);

--
-- Indexes for table `phat`
--
ALTER TABLE `phat`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `role`
--
ALTER TABLE `role`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `sanpham`
--
ALTER TABLE `sanpham`
  ADD PRIMARY KEY (`MaSP`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `account`
--
ALTER TABLE `account`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=47;

--
-- AUTO_INCREMENT for table `banbida1`
--
ALTER TABLE `banbida1`
  MODIFY `MaBan` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;

--
-- AUTO_INCREMENT for table `ca_lam_viec`
--
ALTER TABLE `ca_lam_viec`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=18;

--
-- AUTO_INCREMENT for table `chitietorder`
--
ALTER TABLE `chitietorder`
  MODIFY `MaOrder` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=245;

--
-- AUTO_INCREMENT for table `hoadon`
--
ALTER TABLE `hoadon`
  MODIFY `MaHoaDon` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;

--
-- AUTO_INCREMENT for table `luong`
--
ALTER TABLE `luong`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `member`
--
ALTER TABLE `member`
  MODIFY `MaMember` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `phat`
--
ALTER TABLE `phat`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `sanpham`
--
ALTER TABLE `sanpham`
  MODIFY `MaSP` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `account`
--
ALTER TABLE `account`
  ADD CONSTRAINT `account_ibfk_1` FOREIGN KEY (`role_id`) REFERENCES `role` (`id`);

--
-- Constraints for table `ca_lam_viec`
--
ALTER TABLE `ca_lam_viec`
  ADD CONSTRAINT `ca_lam_viec_FK_phat` FOREIGN KEY (`phat_id`) REFERENCES `phat` (`id`),
  ADD CONSTRAINT `ca_lam_viec_ibfk_1` FOREIGN KEY (`account_id`) REFERENCES `account` (`id`);

--
-- Constraints for table `chitietorder`
--
ALTER TABLE `chitietorder`
  ADD CONSTRAINT `chitiet_sanpham` FOREIGN KEY (`MaSP`) REFERENCES `sanpham` (`MaSP`),
  ADD CONSTRAINT `hoadon_chitiet` FOREIGN KEY (`MaHoaDon`) REFERENCES `hoadon` (`MaHoaDon`);

--
-- Constraints for table `hoadon`
--
ALTER TABLE `hoadon`
  ADD CONSTRAINT `fk_hd_ban` FOREIGN KEY (`MaBan`) REFERENCES `banbida1` (`MaBan`),
  ADD CONSTRAINT `fk_hd_mm` FOREIGN KEY (`MaMember`) REFERENCES `member` (`MaMember`);

--
-- Constraints for table `luong`
--
ALTER TABLE `luong`
  ADD CONSTRAINT `luong_ibfk_1` FOREIGN KEY (`account_id`) REFERENCES `account` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
