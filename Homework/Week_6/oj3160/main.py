"""wow"""
def imprime(x):
    """prime"""
    if x < 2:
        return False
    for i in range(2, int(x**(0.5))+1):
        if not x % i:
            return False
    return True

def main():
    """w"""
    info = input().split()
    total = 0
    ans = ""
    for i in range(int(info[0]), int(info[1])+1):
        if imprime(i):
            ans += str(i) + " "
            total += 1
    if total > 0:
        print(ans.strip(" "))
    print(f"Total primes: {total}")
main()
