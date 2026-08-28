"""aeiou"""
def main():
    """wow"""
    text = input().lower()
    ac = text.count("a")
    ec = text.count("e")
    ic = text.count("i")
    oc = text.count("o")
    uc = text.count("u")
    if ac > 0:
        print(f"a : {ac}")
    if ec > 0:
        print(f"e : {ec}")
    if ic > 0:
        print(f"i : {ic}")
    if oc > 0:
        print(f"o : {oc}")
    if uc > 0:
        print(f"u : {uc}")
main()
