import requests
from bs4 import BeautifulSoup
import pandas as pd
import schedule
import time
from datetime import datetime

url_goc = "https://kenh14.vn/cine.chn"
headers = {
    "User-Agent": "Mozilla/5.0"
}

def lay_tin_kenh14():
    danh_sach_bai = []
    da_xem = set()
    trang_so = 1

    while True:
        url_hien_tai = f"{url_goc}?trang={trang_so}"
        print(f"Đang đọc: {url_hien_tai}")

        try:
            response = requests.get(url_hien_tai, headers=headers, timeout=5)
            response.raise_for_status()
        except Exception as e:
            print(f"Không thể truy cập {url_hien_tai}: {e}")
            break

        soup = BeautifulSoup(response.content, "html.parser")
        cac_tin = soup.find_all('li', class_='knswli')

        if not cac_tin:
            print("Không còn bài viết, dừng lại.")
            break

        tin_moi_trong_trang = 0

        for tin in cac_tin:
            try:
                the_tieu_de = tin.find('h3', class_='knswli-title')
                if not the_tieu_de:
                    continue

                the_link = the_tieu_de.find('a')
                link_bai = the_link['href']
                link_day_du = "https://kenh14.vn" + link_bai if link_bai.startswith("/") else link_bai
                if link_day_du in da_xem:
                    continue
                da_xem.add(link_day_du)
                tin_moi_trong_trang += 1

                tieu_de_bai = the_link.text.strip()

                anh_bia = ""
                khung_anh = tin.find('div', class_='knswli-left')
                if khung_anh:
                    the_anh = khung_anh.find('img')
                    if the_anh and the_anh.get('src'):
                        anh_bia = the_anh['src']

                try:
                    bai_viet = requests.get(link_day_du, headers=headers, timeout=5)
                    bai_viet.raise_for_status()
                    soup_bai = BeautifulSoup(bai_viet.content, "html.parser")
                except Exception as e:
                    print(f"Lỗi khi mở bài {link_day_du}: {e}")
                    continue

                the_tom_tat = soup_bai.find("h2", class_="knc-sapo")
                tom_tat = the_tom_tat.text.strip() if the_tom_tat else ""

                the_than_bai = soup_bai.find("div", id="ContentDetail")
                noi_dung = "\n".join(p.text.strip() for p in the_than_bai.find_all("p")) if the_than_bai else ""

                if not anh_bia and the_than_bai:
                    anh_trong_bai = the_than_bai.find("img")
                    if anh_trong_bai and anh_trong_bai.get("src"):
                        anh_bia = anh_trong_bai["src"]

                danh_sach_bai.append({
                    "TieuDe": tieu_de_bai,
                    "TomTat": tom_tat,
                    "AnhBia": anh_bia,
                    "NoiDung": noi_dung,
                    "Link": link_day_du
                })

                print(f"{tieu_de_bai}")

            except Exception as e:
                print(f"Lỗi khi xử lý tin: {e}")

        if tin_moi_trong_trang == 0:
            print("Trang không có tin mới, dừng lại.")
            break
        trang_so += 1

    df = pd.DataFrame(danh_sach_bai)
    ten_file = f"TinTucKenh14_{datetime.now().strftime('%Y-%m-%d')}.csv"
    df.to_csv(ten_file, index=False, encoding='utf-8')
    print(f"\nĐã lưu {len(df)} tin vào {ten_file}")

schedule.every().day.at("06:00").do(lay_tin_kenh14)

if __name__ == "__main__":
    print("Đang chờ lịch chạy lúc 06:00 mỗi ngày...")
    while True:
        schedule.run_pending()
        time.sleep(20)
