"""a"""
def main():
    """w"""
    n = int(input())
    for _ in range(n):
        t = list(map(float,input().split()))
        ans = f"{sum(t):.1f}"
        if sum(t) > 50:
            ans += ", Overloaded"
        if t[0] > 20:
            ans += ", Check Type Plastic"
        if t[1] > 20:
            ans += ", Check Type Can"
        if t[2] > 20:
            ans += ", Check Type Glass"
        print(ans)
main()
