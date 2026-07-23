"""main"""
def main():
    """surpise"""
    total = float(input())
    highest = float(input())
    lowest = 0
    if total>highest*2:
        lowest = total - highest*2
    if highest - lowest > 2:
        print("Surprising")
    else:
        print("Not surprising")
main()
