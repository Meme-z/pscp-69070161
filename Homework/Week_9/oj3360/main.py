"""www"""
def main():
    """www"""
    w, h, _, _ = map(int, input().split())
    xs = [0] + [int(x) for x in input().split()] + [w]
    ys = [0] + [int(y) for y in input().split()] + [h]
    dx = []
    for i in range(1, len(xs)):
        dx.append(xs[i] - xs[i - 1])
    dy = []
    for i in range(1, len(ys)):
        dy.append(ys[i] - ys[i - 1])
    dx.sort(reverse=True)
    dy.sort(reverse=True)
    mx1 = dx[0] * dy[0]
    mx2 = max(dx[0] * dy[1], dx[1] * dy[0])
    print(f"{mx1} {mx2}")
main()
