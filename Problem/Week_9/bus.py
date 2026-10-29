"""bus"""
def main():
    """www"""
    seat,row,sit = map(int, [input() for _ in range(3)])
    for i in range(seat):
        sl = []
        for j in range(1, row+1):
            if sit == (j*seat)-i:
                sl.append("XX")
            else:
                sl.append(f"{(j*seat)-i:02d}")
        print(" ".join(sl))
        if not (i+1)%2 and i+1 != seat:
            print()
main()
