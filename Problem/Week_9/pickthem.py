"""wow"""
import json
def main():
    num = json.loads(input())
    ev = [n for n in num if n%2 == 0]
    if ev:
        for i in ev:
            print(i)
    else:
        print("Nope")
main()
