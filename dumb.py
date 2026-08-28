"""time"""
def main():
    """time"""
    info = input().split()
    shop = int(info[0])
    time = []
    for _ in range(shop):
        start, stop = map(int, input().split())
        time.append([start,stop])
    check = input().split()
    ans = []
    for t in check:
        stopen = 0
        for start, stop in time:
            if start <= int(t) <= stop-1:
                stopen += 1
        ans.append(str(stopen))
    print(" ".join(ans))
main()
