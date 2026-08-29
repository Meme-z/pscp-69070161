"""wow"""
def main():
    """w"""
    text = []
    try:
        for _ in range(5):
            text.append(input().strip(" "))
    except EOFError:
        text.append("")
    size = max(len(t) for t in text)
    print("*"*(size+4))
    for t in text:
        print("* " + t + " "*(size - len(t)) + " *")
    print("*"*(size+4))
main()
