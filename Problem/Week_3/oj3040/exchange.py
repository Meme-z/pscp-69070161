"""main"""
def main():
    """what"""
    cash = int(input())
    ten = cash//10
    cash -= ten*10
    five = cash//5
    cash -= five*5
    two = cash//2
    cash -= two*2
    one = cash//1
    cash -= one*1
    print(f"10 = {ten}")
    print(f"5 = {five}")
    print(f"2 = {two}")
    print(f"1 = {one}")
main()
