"""wow"""
from math import ceil
def main():
    """ink"""
    n = input().split()
    a = int(n[0])
    people = int(n[1])
    for _ in range(people):
        location = input().split()
        x = int(location[0])
        y = int(location[1])
        time = ceil(((3.1416)* (x**2+y**2))/a)
        print(time)
main()
