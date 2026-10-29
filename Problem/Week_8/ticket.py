"""w"""
def main():
    """ww8"""
    seat = int(input())
    price = 0
    while seat > 0:
        age,ticket = map(int,input().split())
        if age < 15:
            print("-1")
        elif ticket > seat:
            print("-2")
        else:
            if age <= 22:
                price = ticket*120
                seat -= ticket
            elif age >= 60:
                price = ticket*75
                seat -= ticket
            else:
                price = ticket*150
                seat -= ticket
            print(f"{price} {seat}")
main()
