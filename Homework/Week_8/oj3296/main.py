"""wow"""
import math
def main():
    """w"""
    c11,c12,c13 = map(int, input().split())
    c21,c22,c23 = map(int, input().split())
    nc1 = math.floor((c11+c21)/2)
    nc2 = math.floor((c12+c22)/2)
    nc3 = math.floor((c13+c23)/2)
    print(f"{nc1} {nc2} {nc3}")
main()
