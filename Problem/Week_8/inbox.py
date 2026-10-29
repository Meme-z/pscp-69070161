"""w"""
def main():
    """ww8"""
    w,l,m,n = list(map(int,input().split()))
    mini = (l%m)*(w%m)
    for i in range(m+1, n+1):
        if (l%i)*(w%i) < mini:
            mini = (l%i)*(w%i)
    print(mini)
main()
