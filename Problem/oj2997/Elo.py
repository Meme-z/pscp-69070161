"""PSCP Problem: Elo (2997)"""
def main():
    """main"""
    ra = int(input())
    rb = int(input())
    guess = input()
    winner = 0
    if guess == "A":
        winner = 1/(1 + 10**((rb - ra)/400))
    elif guess == "B":
        winner = 1/(1 + 10**((ra - rb)/400))
    print(f"{winner:.2f}")
main()
