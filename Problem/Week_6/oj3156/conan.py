"""conan"""
def main():
    """what"""
    alp = ["a","b","c","d","e","f","g","h","i","j","k","l",
           "m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    text = input()
    move = int(input())
    for i in text:
        if i in alp:
            idx = alp.index(i)
            print(alp[(idx+move)%26],end="")
main()
