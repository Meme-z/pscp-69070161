"""wow"""
def main():
    """idk"""
    k = input().upper()
    fdict = {"J":"jack","Q":"queen","K":"king","A":"ace"}
    bdict = {"S":"spades","D":"diamonds","C":"clubs","H":"hearts"}
    if k[0].isalpha():
        print(f"{fdict[k[0]]} of {bdict[k[-1]]}")
    else:
        print(f"{k[0:-1]} of {bdict[k[-1]]}")
main()
