"""main"""
def main():
    """abc"""
    many = int(input())
    count = 0
    for _ in range(many):
        abc = input()
        if abc in ("A", "E", "I", "O", "U"):
            count += 1
    print(count)
main()
