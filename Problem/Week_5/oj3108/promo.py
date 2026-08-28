"""wow"""
def main():
    """wow"""
    info = input().split()
    a = int(info[0])
    b = int(info[1])
    c = int(info[2])
    pay = a*25+b*40+c*55
    if a + b + c >= 3:
        pay = pay - pay*0.1
    print(int(pay))
main()
