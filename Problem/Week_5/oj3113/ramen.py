"""wow"""
def main():
    """wow"""
    ramen = input().split()
    topping = input()
    price = 0
    size = ramen[0]
    if size == "S":
        price = 60
    elif size == "M":
        price = 80
    elif size == "L":
        price = 100
    if ramen[1] == "T":
        price += 20
    if topping != "N":
        top = topping.split()
        if top[0] == "P":
            price = price + int(top[1])*15
        elif top[0] == "E":
            price = price + int(top[1])*10
    print(price)
main()
