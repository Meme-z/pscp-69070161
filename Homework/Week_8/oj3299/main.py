"""wow"""
def main():
    """w"""
    l,t = map(int, input().split())
    count = 1
    while True:
        block = count * l
        total = block * (block+1)//2
        if total >= t:
            print(count)
            break
        count += 1
main()
