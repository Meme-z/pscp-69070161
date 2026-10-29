"""wow"""
def main():
    s = []
    while True:
        a = input()
        if a == "NULL":
            break
        s.append(a)
    for f in reversed(s):
        print(f)
main()
