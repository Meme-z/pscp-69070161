"""wow"""
def main():
    """wow"""
    money = int(input())
    k = 0
    vh = 0
    h = 0
    if money % 100:
        print("ERROR")
    else:
        k = money // 1000
        money -= k*1000
        vh = money // 500
        money -= vh*500
        h = money // 100
        if k > 0:
            print(f"1000 = {k}")
        if vh > 0:
            print(f"500 = {vh}")
        if h > 0:
            print(f"100 = {h}")
main()
