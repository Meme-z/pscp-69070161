"""aaa"""
def main():
    """wow"""
    num = list(input().split())
    f = input()
    for _ in range(num.count(f)):
        print(" ".join([str(num.index(f))] * num.count(f)))
main()
