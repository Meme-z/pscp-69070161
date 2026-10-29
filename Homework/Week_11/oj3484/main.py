"""www"""
def main():
    """www"""
    n, p = input().split()
    n = int(n)
    p = float(p)
    grid = []
    for _ in range(n):
        grid.append([int(x) for x in input().split()])
    for i in range(n):
        row = grid[i]
        c_tile = sum(1 for x in row if x > 0)
        c_pts = sum(row)
        line = " ".join(str(x) for x in row)
        print(f"{line} {c_tile} {c_pts}")
    col_tiles = []
    col_pts = []
    for j in range(n):
        c_tile = 0
        c_pts = 0
        for i in range(n):
            if grid[i][j] > 0:
                c_tile += 1
            c_pts += grid[i][j]
        col_tiles.append(c_tile)
        col_pts.append(c_pts)
    print(" ".join(str(x) for x in col_tiles))
    print(" ".join(str(x) for x in col_pts))
    tot_tiles = sum(col_tiles)
    tot_pts = sum(col_pts)
    fine = tot_pts * p
    print(f"{tot_tiles} {tot_pts} {fine:.2f}")
main()
