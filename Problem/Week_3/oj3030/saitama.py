"""anime"""
import math
def main():
    """sai"""
    pugoal= int(input())
    sugoal= int(input())
    udgoal= int(input())
    rgoal= int(input())
    pud = int(input())
    sud = int(input())
    rd = int(input())
    udd = int(input())
    goal1 = math.ceil(pugoal / pud)
    goal2 = math.ceil(sugoal / sud)
    goal3 = math.ceil(udgoal / udd)
    goal4 = math.ceil(rgoal / rd)
    print(int(max(goal1, goal2, goal3, goal4)))
main()
