"""pro"""
def main():
    """main"""
    x = int(input()) # โปร มา x จ่าย y
    y = int(input()) # โปร มา x จ่าย y
    a = int(input()) # ราคา a/คน
    z = int(input()) # มาจริง z คน
    total = ((((z//x))*y)+(z%x))*a # (จำนวนคนที่เข้าร่วมโปร + เศษคนที่เหลือ)*ราคา
    print(total)
main()
