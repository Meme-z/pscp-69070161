"""w"""
from decimal import Decimal, ROUND_HALF_UP
def main():
    """ww8"""
    u = int(input())
    pay = 0
    if u <= 10:
        pay = u*5
    elif u <= 50:
        pay = (u-10)*7 + 50
    elif u <= 100:
        pay = (u-50)*10 + 330
    elif u <= 200:
        pay = (u-100)*12 + 830
    elif u > 200:
        pay = (u-200)*15 + 2030
    pay = str(pay+(pay*0.07)+(u*0.5))
    pay = Decimal(pay).quantize(Decimal('0.1'), ROUND_HALF_UP)
    print(pay)
main()
