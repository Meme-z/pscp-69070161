"""year"""
def main():
    """year"""
    year = int(input())
    if year >= 1582:
        if not year % 4:
            if not year % 100:
                if not year % 400:
                    print("yes")
                else:
                    print("no")
            else:
                print("yes")
        else:
            print("no")
    else:
        if not year % 4:
            print("yes")
        else:
            print("no")
main()
