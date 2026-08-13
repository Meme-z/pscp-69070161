"""are"""
def main():
    """rec"""
    xa, ya, wa, ha = list(map(int, input().split()))
    xb, yb, wb, hb = list(map(int, input().split()))
    wo = max(0,min(xa+wa,xb+wb)-max(xa,xb))
    ho = max(0,min(ya+ha,yb+hb)-max(ya,yb))
    area = wo * ho
    if area > 0:
        print(area)
    else:
        print("no overlapping")
main()
