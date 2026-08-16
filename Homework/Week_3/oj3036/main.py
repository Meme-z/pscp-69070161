"""tri"""
def main():
    """wow"""
    num = int(input())
    row = 1
    while num > row**2:
        row += 1
    where = num-((row-1)**2)+1
    ans = (row-1)*2
    if where%2 == 1:
        ans -=1
    print(ans)
main()
