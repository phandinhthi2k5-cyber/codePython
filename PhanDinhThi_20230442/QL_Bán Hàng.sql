CREATE TABLE MatHang (
    MaHang INT PRIMARY KEY IDENTITY,
    TenHang NVARCHAR(100),
    NguonGoc NVARCHAR(100),
    Gia FLOAT
);

-- Khách hàng
CREATE TABLE KhachHang (
    MaKH INT PRIMARY KEY IDENTITY,
    TenKH NVARCHAR(100),
    DiaChi NVARCHAR(200),
    SDT NVARCHAR(20)
);

-- Hóa đơn
CREATE TABLE HoaDon (
    MaHD INT PRIMARY KEY IDENTITY,
    MaKH INT,
    NgayLap DATE,
    FOREIGN KEY (MaKH) REFERENCES KhachHang(MaKH)
);

-- Chi tiết hóa đơn
CREATE TABLE ChiTietHoaDon (
    MaHD INT,
    MaHang INT,
    SoLuong INT,
    DonGia FLOAT,
    PRIMARY KEY (MaHD, MaHang),
    FOREIGN KEY (MaHD) REFERENCES HoaDon(MaHD),
    FOREIGN KEY (MaHang) REFERENCES MatHang(MaHang)
);