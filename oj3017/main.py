"""main"""
def main():
    """bill"""
    bill = int(input())
    tip = bill * 0.1
    if tip < 50:
        tip = 50
    elif tip > 1000:
        tip = 1000
    total = (bill + tip)+ ((bill + tip)*0.07)
    print(f"{total:.2f}")
main()
