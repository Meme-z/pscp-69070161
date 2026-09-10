"""xd"""
def main():
    """w7"""
    many = int(input())
    bunny = ""
    maxi = -2000000000
    count = 0
    for _ in range(many):
        info = input().split()
        if int(info[1]) > 15:
            count +=1
        if int(info[1]) > maxi:
            bunny = info[0]
            maxi = int(info[1])
    print(count)
    print(bunny)
main()
