"""expo"""
def main():
    """func"""
    num = int(input())
    avg = 0
    f = False
    for _ in range(num):
        score = int(input())
        if score < 50 and not f:
            f = True
        avg += score
    avg /= num
    print(f"{avg:.1f}")
    if avg >= 60 and not f:
        print("PASS")
    elif avg < 60 or f:
        print("FAIL")
main()
