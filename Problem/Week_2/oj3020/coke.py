"""coke"""
def main():
    """coke"""
    a = int(input()) # ราคาปกติ
    b = int(input()) # นำ b ฝามาแลกซื้อ c บาท
    c = int(input()) # ราคาโปร
    d = int(input()) # จำนวนขวด
    if d > 0 and 0 < b and a >= c:
        special = d/b # จำนวนขวดที่ซิ้อได้ในราคาโปร
        if float(int(special)) == special:  # หารลงตัว -1
            special -= 1
        total = ((d-int(special))*a)+((int(special))*c)
    else:
        total = d*a # ไม่มีโปรซื้่อราคาปกติ
    print(total)
main()
