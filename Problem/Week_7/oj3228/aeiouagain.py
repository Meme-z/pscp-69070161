"""xd"""
def main():
    """w7"""
    text = input()
    count = 0
    for t in text:
        if t in ("a", "e", "i", "o", "u"):
            count += 1
    print(count)
main()
