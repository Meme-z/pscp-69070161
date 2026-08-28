"""qbc"""
def main():
    """school"""
    text = input().upper()
    pass1 = ord(text[0])
    pass2 = ord(text[-1])
    nlist =[0,1,2,3,4,5,6,7,8,9]
    for i in range(10):
        if not i % 2:
            nlist[i] += pass1
        else:
            nlist[i] = pass2 - nlist[i]
        nlist[i] %= len(text)
        if nlist[i] > 9:
            nlist[i] %=10
        nlist[i] = str(nlist[i])
    realpass = " ".join(nlist[2:8])
    print(realpass)
main()
