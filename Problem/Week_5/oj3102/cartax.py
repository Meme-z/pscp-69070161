"""wow"""
def main():
    """wow"""
    year = int(input())
    cc = int(input())
    tax = 0
    if year <= 1990:
        if cc <= 1500:
            tax = 1250
        elif cc <= 2000:
            tax = 1400
        elif cc > 2000:
            tax = 2000
    elif year <= 1999:
        if cc <= 1500:
            tax = 1100
        elif cc <= 2000:
            tax = 1300
        elif cc > 2000:
            tax = 1700
    elif year >= 2000:
        if cc <= 1500:
            tax = 1000
        elif cc <= 2000:
            tax = 1200
        elif cc > 2000:
            tax = 1500
    print(tax)
main()
