"""xd"""
def main():
    """w7"""
    key = input()
    code = 1300
    nl = [900,1000,1100,1200,1400]
    for i in range(5):
        if int(key[i]) > 5:
            code = nl[i]
            break
    if key == key[::-1]:
        if int(key[0]) + int(key[4]) > 5:
            code += 10
        elif int(key[1]) * int(key[3]) > 5:
            code += 20
    else:
        if int(key[4]) and int(key[0]) // int(key[4]) > 5:
            code += 10
        elif int(key[1]) - int(key[4]) > 5:
            code += 20
    if int(key[0]) + int(key[1]) + int(key[2]) + int(key[3]) + int(key[4]) > 25:
        code += 1
    elif int(key[0]) * int(key[1]) * int(key[2]) * int(key[3]) * int(key[4]) > 55:
        code += 2
    print(code)
main()
