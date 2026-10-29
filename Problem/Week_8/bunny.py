"""bunny"""
def main():
    """son"""
    text = input()
    count = 0
    maxi = 0
    if "b" in text or "B" in text:
        for i, char in enumerate(text):
            if char in ("b", "B"):
                j = 1
                while i + j < len(text) and text[i + j] in ("u", "U"):
                    j += 1
                    count += 1
                if count > maxi:
                    maxi = count
                count = 0
        if maxi >= 2:
            print(f"Yes {maxi}")
        else:
            for i, char in enumerate(text):
                if char in ("b", "B"):
                    print(text[:i + 1] + "U" * (len(text) - i - 1))
                    break
    else:
        print(("BUU" * len(text))[:len(text)])
main()
