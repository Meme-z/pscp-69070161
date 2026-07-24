"""gift"""
def main():
    """aa"""
    size = input().split()
    r = float(size[0])
    h = float(size[1])
    g = float(size[2])
    width = 2*3.14*r+g
    lenght = h+(2*r)
    print(f"{lenght:.2f} {width:.2f}")
main()
