"""3005"""
def main():
    """rabbit"""
    vet = input().split()
    carrot = int(vet[0])
    cabbage = int(vet[1])
    tomato = int(vet[2])
    ans = carrot * 10 + cabbage * 25 + tomato * 3
    print(ans)
main()
