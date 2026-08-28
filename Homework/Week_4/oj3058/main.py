"""wow"""
def main():
    """brick"""
    a = int(input())
    b = int(input())
    goal = int(input())
    maxv = min(b, goal//5)*5
    need = goal - maxv
    if 0 <= need <= a:
        print(need)
    else:
        print("-1")
main()
