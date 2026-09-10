"""xd"""
def main():
    """w7"""
    cash = float(input())
    year = int(input())
    stang = int(cash * 100)
    for _ in range(year):
        increase = (stang * 381) // 10000
        stang += increase
    print(f"{stang // 100}.{stang % 100:02d}")
main()
