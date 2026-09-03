"""coffee"""
def main():
    """wow"""
    cup = []
    num = int(input())
    for _ in range(num):
        cup.append(int(input()))
    avg = round(sum(cup)/num,1)
    print(sum(cup))
    print(max(cup))
    print(min(cup))
    print(f"{avg:.1f}")
main()
