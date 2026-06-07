# Oryo Browser

Đây là dự án trình duyệt mã nguồn mở Oryo được phát triển và tối ưu bởi Sakayori Studio. 

LƯU Ý QUAN TRỌNG: Repository này KHÔNG phải là toàn bộ mã nguồn (Full Source) của trình duyệt. Đây chỉ là nơi lưu trữ các file cấu hình thương hiệu (Rebrand), các bản vá lỗi và mã nguồn C++ tùy biến nâng cao nhằm tối ưu hóa hiệu năng và giảm lượng RAM tiêu thụ cực hạn so với Chromium gốc.

## Yêu cầu hệ thống (Requirements) để build dự án
* Hệ điều hành: Windows 10/11 64-bit (đã bật Developer Mode).
* Ổ cứng: Trống tối thiểu 100 GB (khuyến khích dùng ổ SSD tốc độ cao).
* Công cụ bắt buộc: Bộ công cụ depot_tools của Google và Microsoft Visual Studio (đầy đủ gói C++ và Windows SDK tương thích với Chromium).

## Hướng dẫn cài đặt và đồng bộ dành cho Contributor
Để có đầy đủ bộ nguồn và bắt đầu lập trình, bạn cần thực hiện theo các bước sau:

1. Tải toàn bộ mã nguồn Chromium gốc của Google (khoảng 30-40 GB) về máy thông qua công cụ fetch của depot_tools:
   fetch chromium

2. Di chuyển vào thư mục nguồn vừa tải:
   cd src

3. Khởi tạo kết nối Git tới repository Oryo này:
   git init
   git remote add origin https://github.com/Sakayorii/Oryo-Browser.git

4. Tiến hành kéo mã nguồn tùy biến của Oryo về để ghi đè tự động vào cấu trúc thư mục gốc:
   git pull origin main --allow-unrelated-histories

5. Đồng bộ lại các thư viện bên thứ ba của Google:
   gclient sync

## Lệnh tạo file cấu hình và Build trình duyệt
Sau khi đồng bộ xong, bạn chạy các lệnh sau bằng CMD/PowerShell với quyền Administrator để tiến hành biên dịch:

1. Nạp lại sơ đồ build graph để hệ thống nhận diện target mới:
   gn gen out\Default

2. Tiến hành build phiên bản Oryo độc bản bằng Ninja:
   autoninja -C out\Default oryo
