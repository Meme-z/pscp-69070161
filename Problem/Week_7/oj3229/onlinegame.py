"""xd"""
def main():
    """w7"""
    s = int(input())
    bs = int(input())
    d = int(input())
    rank = 0
    total = s + bs
    if d > 3:
        total *= 1.5
    print(int(total))
    if total >= 1500:
        rank = 5
    elif total >= 1000:
        rank = 4
    elif total >= 500:
        rank = 3
    elif total >= 200:
        rank = 2
    elif total < 200:
        rank = 1
    print(rank)
    if rank == 5 and d >= 7:
        print(99)
    elif rank == 4 and bs > 300:
        print(88)
    else:
        print(0)
main()
