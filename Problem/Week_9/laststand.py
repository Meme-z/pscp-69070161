"""ig"""
def main():
    """wow"""
    a = input().strip("[").strip("]").split(",")
    nl = [x.strip() for x in a if x.strip()]
    for i in nl:
        print(i[-1])
main()
