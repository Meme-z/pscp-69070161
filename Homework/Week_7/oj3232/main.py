"""wow"""
def main():
    """idk"""
    info = input().split()
    jp = int(info[0])
    goal = int(info[1])
    go = 0
    count = 0
    while jp > 0 and go < goal:
        go += jp
        count += 1
        jp -= 2
    if goal > go:
        print(-1)
    else:
        print(count)
main()
