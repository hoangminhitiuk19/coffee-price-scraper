import re

def extract_market_data(input_text):
    # Define a regex pattern to match market data (name, average price, and change)
    pattern = r"(Đắk Lắk|Lâm Đồng|Gia Lai|Đắk Nông|Giá tiêu).*?\n(\d{1,3}(?:[.,]\d{3})*)\n([+-]?\d{1,3}(?:[.,]?\d{3})*)"
    matches = re.findall(pattern, input_text)

    # Format results into a list of dictionaries
    market_data = []
    for match in matches:
        market_data.append({
            "Market": match[0],
            "Average Price": match[1],
            "Change": match[2]
        })

    return market_data

# Input text from the OCR result
ocr_text = """GIACAPHE COM
Giới thiệL
Giá Cafe
Giá tiêu hôm nz
Ián bór
sẵU riêng
Giá =
phê hôm
ngày 07/12/2024
124,000 đ/kg
+3,900
cà phê trona nướ
Thav đò
Đắk Lắk
124,000
+4,000
Đổna
123 000
+3,50C
Gia Lai
124,000
4,OOC
k Nông
124,000
3 806
Giá tiêL
147,000
+2,000
USDVND
25.134
giả: giacapl
Đơn vị tính: VNĐfkg
nis theo Vietcombank
Xem ngà
'khác v
Giá cà phê Robusta London
1ay đổi
Thắp nhắt
udng
Mđ cú
Hôm tr
01/25
5,153
4,889
4,963
4,895
20,972
5.27%
+243
5,152
4,885
03/25
5,116
8,832
4,925
32,579
+238
4,835
5,065
,433
4,890
4,827
4.93%
07125
5 0oo
1.074
4.829
4,767
3 579
a0 dich
cà phê Arabica New York
Thay đổi
+16.75
331.70
313 70
03/25
330.25
+0.20
27,925
315.95
313.50
103,98
18.20
+16.30
328.65
311.40
05/25
327.60
313.30
311.30
+15.40
07125
321,95
308.00
306.55
24,6
5.02%
~0.20
+13.05
14.80
300.70
09/25
314 15
30110
413.70
Đơn vi tinl
centflb: Ilb
0.4Ska
ao dich
'Đoc thêr-..
Cà phê Arabica sana USDItấn
Giá
phê hôm nay
07/12/2024 đươc câp nhât liên tuc
'phê hõm nay ngày 07/12/2024 trung bìnl
' mức 124,000 đfkg tăng mạnl
+3 900
nqàv hôm
nhất thu mua
vùng trọng điểm
' Nguyên (Đắk Lắk
Đổng
Gia LaiĐắk
được ghi
ở mức 124,000 đfkg
trong
1 nqàw
phê thế giới kết hợp với việc khảo sát liên tục từ các doanh nghiệp, đại lý thu mua
cả nước
nhiêr
những ngày giá
Đoc tíêp
Giế
phê những ngày khác:
[2024
Naàv 06/12/2024
{12/2024
- Naàv 04/12/2024
- Ngày 03/12/2024
'02/12/2024
30/11/2024
Ngày 29/11/2024
28/11/2024
27/11/2024
Nqàl
Nqàv
71/2024
24/11/2024
- Naàv
[11/2024
Có thể bạn
Giắ cà phê thể aiới trưc tuven
vàng
Giá tiê
cà phê tươi
Giắ tiêl
Kién thức
dich hàna hóa phắi sinh
RƯỜNG CÀ PHÊ
Các lệnh thôn
dung trong ciao dich
phê
Các loại Iệnh thông dụng trong giao dịch kỳ hạn trên thị trường cà phê trên thị trường
hạn
Fàn mạn cùng giá cà phê
Thời aian aẩn đâv có rất nhiều bài viết phân tích
cà phê: chủ vếu là dánh aiá các
nquvên nhân
dông dên thị trường cà phê
giới. Các qiới phân tích mỗi người
dua ra môt nhên dinb
Xuất khẩu
phê: Bán
chốt trước hay chốt sau?
Mua bán
hợp dông
tai song song
hợp dông
'rõ rang
mà theo đó
bên mua và bán quyết dịnh một mức giá đơn vị nhất dịnh cho
hợp dông
Luận về "giá trừ lùi" trong mua bán
phê
Bài luận bàn giá trừ lùi
không
giải pháp cho giai đoạn thị trường hiện
muốn cùng bạn tìm cách cho một hướng mua bán hữu hiệu và lâu dài.
Kinh nghiệm
phòng giàm giá
phê thú vị cua các nhà sàn xuất Trung Mỹ
nhà sản xuất
phê tại Trung Mũ dang sử dung lợi nhuân thu dược trong mùa VL
giá cao, trồng các loại nông sản khác và thiết kế tour
dẻ da
dana
phòng diên biên
Chuvên
TIN TỨC
BANG GIÁ
Gíới thíêu
Bài chuyên
Giá cà phê hôm
Liên hê
Thị trường
Giá cà phê trực tuyên
' viết về YSCafe
Đíều kho
Cà phê
1 tiêu trưc tuvến
3 Website
Cậng đồng "
Giá cao su truc tuvến
Giá cz
trực tuyến
Quàn tri
THEO DỖl YSCAFE
Diên t
Giá phân
@c
Chăr sóc cà phê
Tý giá ngoại tệ
61 RSS feed
Chế b
cà phê
CÔNG CU
TAFacehook
đằu tư
@ Pi
Tính mức Stop loss
Cuậc sống
' giá Arabica
iên hé auẩna cáo: 02633 747181 {
phê tudi
"giacaphe-com
Sána lâp
Nội dung phong phú
dóna aóp
Gôna dôna YScaf
mona
chia
kiến thức
nahiêm
con nông dân, doanh nghiệp, chuyêr
' trong ngành dếr
với tất
moi
công dông
phê Viêt N
qiới
nauổn kinh
uy trì hoạt động, YSCafe
auảna
website
Đôi khi chúna mana dén sư khó chiu
t mong quý Bò
thông
Trona trườna
nghiệp
quảng
quảng bá
minh
lòng
1tin bê
dưới ,
quảng
0945 745 536
info@qiacaphe.
@2008
Gíacaphe
Vận hành
TNHH Cà phê Y5
GPDKKD
5800921425 do
ĐT Lâm Đổng
12/07/2010
protected
reCAPTCHA and the Google Privacy Policy
apply
XEM THÊM
Giá cà phê tƯơi
Jái sinh
cà phê
4 Giá sẩu
Thinh
cà phê Đẳk N
Giá cÈ
Gia Lai
Đổng
Đổi giá
Nông,
1 thế giới
riêng.
@ Google
USDỊtấn"""

# Extract the specific data
extracted_data = extract_market_data(ocr_text)

# Print the results
print("\nExtracted Market Data:")
for data in extracted_data:
    print(data)
