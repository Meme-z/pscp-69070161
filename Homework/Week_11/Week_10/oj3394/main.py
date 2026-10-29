"""www"""
def main():
    """www"""
    n, s = map(int, input().split())
    nxt = [0] + [int(input()) for _ in range(n)]
    vis = [False] * (n + 1)
    cur = s
    while cur != 0 and not vis[cur]:
        vis[cur] = True
        cur = nxt[cur]
    print(vis.count(True))
main()
