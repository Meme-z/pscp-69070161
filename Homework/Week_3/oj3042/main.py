"""main"""
def main():
    """ten"""
    num =  int(input())
    ten = num//10
    for _ in range(ten):
        print(f"{ten*10}", end=" ")
        ten -= 1
    print("0")
main()
