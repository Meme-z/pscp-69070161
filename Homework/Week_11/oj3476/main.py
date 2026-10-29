"""www"""
def main():
    """www"""
    dictcat = {}
    dictfox = {}
    n = int(input())
    have01cat = False
    have01fox = False
    for _ in range(n):
        rawinput = input().split(":")
        name = rawinput[0].strip().strip('"{}\'')
        num_str = rawinput[1].strip().strip('"{}\'')
        if "Cat" in num_str:
            num = int(num_str.split("Cat")[1])
            if num == 1:
                have01cat = True
            dictcat[name] = num
        else:
            num = int(num_str.split("Fox")[1])
            if num == 1:
                have01fox = True
            dictfox[name] = num
    if not have01cat and "Garfield" not in dictcat and "Garfield" not in dictfox:
        dictcat["Garfield"] = 1
    if not have01fox and "Fubuki" not in dictcat and "Fubuki" not in dictfox:
        dictfox["Fubuki"] = 1
    sort_cat = []
    for name, num in dictcat.items():
        sort_cat.append((num, name))
    sort_cat.sort()
    sort_fox = []
    for name, num in dictfox.items():
        sort_fox.append((num, name))
    sort_fox.sort()
    print(f"Cat : {len(sort_cat)}")
    print(f"Fox : {len(sort_fox)}")
    for num, name in sort_cat:
        print(f"{name} : Cat{num:02d}")
    for num, name in sort_fox:
        print(f"{name} : Fox{num:02d}")
main()
