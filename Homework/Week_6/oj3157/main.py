"""wow"""
def main():
    """w"""
    play = int(input())
    score = 0
    for _ in range(play):
        sign = input()
        if sign == "+":
            score += 10
        elif sign =="-":
            score -= 5
    print(score)
main()
