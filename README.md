# Kenh14 – Thu thập tin tức của kenh14.vn

**Kenh14** là công cụ tự động thu thập tin tức mới nhất từ chuyên mục **Cine** của trang [Kenh14.vn](https://kenh14.vn/cine.chn). Dự án hỗ trợ lưu trữ thông tin bài viết như tiêu đề, mô tả, ảnh, nội dung và liên kết gốc vào file CSV theo từng ngày.

---

## Tính năng

- **Tự động thu thập toàn bộ các bài viết** trong chuyên mục Cine (không giới hạn số trang)
- Trích xuất đầy đủ thông tin:
  - Tiêu đề (Title)
  - Mô tả ngắn (Summary)
  - Ảnh đại diện (Thumbnail)
  - Nội dung chính (Content)
  - Đường dẫn bài viết (URL)
- Lưu kết quả vào file CSV theo định dạng: `TinTucKenh14_YYYY-MM-DD.csv`
- Hỗ trợ **lập lịch chạy tự động mỗi ngày lúc 06:00 sáng**

---

## Công nghệ sử dụng

- Python 3.10.0+
- [`requests`](https://pypi.org/project/requests/) – Gửi yêu cầu HTTP
- [`beautifulsoup4`](https://pypi.org/project/beautifulsoup4/) – Phân tích HTML
- [`pandas`](https://pypi.org/project/pandas/) – Xử lý dữ liệu
- [`schedule`](https://pypi.org/project/schedule/) – Lập lịch tự động

---

## Cách sử dụng

### Bước 1: Cài đặt thư viện cần thiết
```bash
pip install -r requirements.txt
