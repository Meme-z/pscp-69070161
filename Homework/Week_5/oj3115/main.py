"""time"""
def main():
    """time"""
    info = input().split()
    shop = int(info[0])
    timeline = [0]*1441
    for _ in range(shop):
        start, stop = map(int, input().split())
        for c in range(start, stop):
            timeline[c] += 1
    check = input().split()
    ans = []
    for t in check:
        ans.append(str(timeline[int(t)]))
    print(" ".join(ans))
main()
