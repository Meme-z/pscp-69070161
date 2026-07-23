"""milk"""
def main():
    """milk"""
    a = int(input()) # ราคา a บาท
    b = int(input()) # นำ b ฝา แลกได้ c ขวด
    c = int(input()) # นำ b ฝา แลกได้ c ขวด
    d = int(input()) # มีเงิน d บาทได้นมกี่ขวด max
    cap = d//a # หาฝาเช็ต 1
    total = cap
    if b > 0 and c < b:
        while cap >= b: # หากเหลือฝายังแลกได้ต่อ
            extra = (cap//b)*c # หาฝาแลกเพิ่ม (เช็ต n)
            total += extra # บวกจำนวนที่แลกได้เพิ่ม
            cap = (cap % b)+extra # หาฝาว่ายังเหลือไหม
    else:
        total = d//a # ไม่มีโปร
    print(int(total))
main()
