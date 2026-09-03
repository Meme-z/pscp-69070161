"""export"""
def main():
    """supply"""
    sup = int(input())
    odd,even,total=0,0,0
    for _ in range(sup):
        num=int(input())
        if not num%2:
            even +=1
        else:
            odd +=1
        total +=num
    print(f"SUM {total}")
    print(f"EVEN {even}")
    print(f"ODD {odd}")
main()
