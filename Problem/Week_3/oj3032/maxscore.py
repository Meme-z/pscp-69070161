"""test"""
def main():
    """aa"""
    test = int(input())
    scorelist = []
    for _ in range(test):
        score = int(input())
        scorelist.append(score)
        amount = scorelist.count(max(scorelist))
    print(max(scorelist))
    print(amount)
main()
