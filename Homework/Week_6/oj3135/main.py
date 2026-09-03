"""steal"""
def main():
    """gift"""
    num = input().split()
    check = 0
    if int(num[2]) == 1:
        print(1)
        return
    for i in range(1, int(num[0])):
        at = ((1+i*int(num[1]))%int(num[0]))
        if not at:
            at = int(num[0])
        if at == int(num[2]):
            check += 1
            break
        if at == 1:
            break
        check += 1
    print(check+1)
main()
