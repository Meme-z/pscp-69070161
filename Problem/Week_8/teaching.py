"""w"""
def main():
    """ww8"""
    teach = int(input())
    time = int(input())
    h = teach*time//60
    m = teach*time%60
    if not teach or not time:
        print("No teaching")
    elif not m:
        print(f"{h} hours")
    elif not h:
        print(f"{m} minute")
    elif m and h:
        print(f"{h} hours {m} minute")
main()
