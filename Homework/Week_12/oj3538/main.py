"""www"""
def main():
    """www"""
    s = input()
    ans = ""
    for c in s:
        if s.count(c) % 2 != 0 and c not in ans:
            ans += c
    print(ans if ans else "fully paired")
main()
