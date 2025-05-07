# Kenh14 - Thu Thập Tin Tức Điện Ảnh Tự Động (Bài Tập Sinh Viên)

**Mục tiêu:** Dự án nhỏ này nhằm mục đích tự động thu thập tin tức điện ảnh từ trang web Kenh14.vn, phục vụ mục đích học tập và nộp bài tập.

---

## Chức Năng Chính

1.  **Thu thập dữ liệu bài viết:** Lấy thông tin chi tiết của các bài viết điện ảnh, bao gồm:
    * Tiêu đề bài viết
    * Mô tả ngắn
    * Hình ảnh đại diện
    * Nội dung chi tiết của bài viết
    * Đường dẫn (URL) của bài viết
2.  **Thu thập nhiều trang:** Lấy dữ liệu từ nhiều trang khác nhau của chuyên mục điện ảnh trên Kenh14 (hiện tại đang lấy từ 3 trang đầu).
3.  **Lưu trữ dữ liệu:** Lưu trữ toàn bộ dữ liệu thu thập được vào một file định dạng CSV (Comma Separated Values) để dễ dàng xem và xử lý.
4.  **Lập lịch tự động:** Thiết lập để script tự động chạy mỗi ngày vào lúc 6:00 sáng, giúp cập nhật tin tức một cách tự động.
5.  **Dự án GitHub:** Mã nguồn của dự án được công khai trên GitHub để tiện theo dõi và đánh giá.
6.  **Hướng dẫn cài đặt:** File `README.md` này cung cấp các bước cài đặt và chạy dự án một cách rõ ràng.

---

## Hướng Dẫn Cài Đặt

Để chạy dự án này trên máy tính của bạn, hãy làm theo các bước sau:

### Bước 1: Cài đặt Python

Đảm bảo rằng bạn đã cài đặt Python 3 trên máy tính của mình. Bạn có thể tải Python từ trang web chính thức: [https://www.python.org/downloads/](https://www.python.org/downloads/)

### Bước 2: Cài đặt các thư viện cần thiết

Dự án này sử dụng một số thư viện Python bên ngoài. Để cài đặt chúng, bạn cần sử dụng `pip`, trình quản lý gói của Python.

1.  Mở **Terminal** (trên macOS/Linux) hoặc **Command Prompt** (trên Windows).
2.  Điều hướng đến thư mục mà bạn đã tải hoặc sao chép mã nguồn của dự án này về.
3.  Chạy lệnh sau để cài đặt các thư viện cần thiết được liệt kê trong file `requirements.txt` (nếu có):

    ```bash
    pip install -r requirements.txt
    ```

    Nếu không có file `requirements.txt`, bạn có thể cài đặt từng thư viện một bằng lệnh sau:

    ```bash
    pip install requests beautifulsoup4 pandas schedule
    ```

    * `requests`: Để gửi yêu cầu HTTP đến trang web.
    * `beautifulsoup4`: Để phân tích cú pháp HTML của trang web.
    * `pandas`: Để làm việc và lưu dữ liệu vào file CSV.
    * `schedule`: Để lên lịch chạy script tự động.

### Bước 3: Chạy script thu thập tin tức

1.  Mẫn Terminal hoặc Command Prompt (vẫn ở thư mục dự án).
2.  Chạy script Python chính (thường có tên là `code_1.py` hoặc tương tự) bằng lệnh sau:

    ```bash
    python <tên_script>.py
    ```

    Thay `<tên_script>.py` bằng tên thực tế của file Python chính trong dự án của bạn.

    Khi script chạy lần đầu tiên, nó sẽ thu thập dữ liệu từ các trang web và lưu vào một file CSV có tên tương tự như `TinTucKenh14_YYYY-MM-DD.csv` trong cùng thư mục.

### Bước 4: Thiết lập lịch chạy tự động (tùy chọn)

Để script tự động chạy mỗi ngày vào lúc 6:00 sáng, bạn có thể sử dụng thư viện `schedule` tích hợp trong code hoặc sử dụng công cụ lập lịch của hệ điều hành.

**Sử dụng thư viện `schedule` (nếu có trong code):**

Nếu code của bạn đã sử dụng thư viện `schedule`, bạn chỉ cần đảm bảo rằng script Python được chạy một lần (ví dụ: khi bạn đăng nhập vào máy tính). Thư viện `schedule` sẽ tự động quản lý việc chạy script theo lịch đã đặt (thường là 6:00 sáng hàng ngày).

---

## Cấu Trúc Dự Án
BaitapLonn/
├── code_1.py
├── requirements.txt
└── README.md

---
