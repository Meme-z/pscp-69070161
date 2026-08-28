"""schoolshop"""
from decimal import Decimal, ROUND_HALF_UP
def main():
    """schoolshop"""
    member = input()
    items = int(input())
    pay = 0
    for _ in range(items):
        pay += Decimal(input())
    if member == "Y":
        pay = pay * Decimal("0.95")
    elif member == "N":
        if pay >= 500:
            pay = pay*Decimal("0.97")
    pay = Decimal(pay).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
    print(f"{pay:.2f}")
main()
