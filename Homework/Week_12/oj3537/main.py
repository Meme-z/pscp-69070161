"""sussybaka"""
import json
def main():
    """amogus"""
    alive = {}
    dead = {}
    while True:
        name = input()
        if name == "Start":
            break
        alive.update(json.loads(name))
    while True:
        vote = input()
        if vote == "End":
            break
        if vote in alive:
            dead[vote] = alive.pop(vote)
    print(f"{list(alive.values()).count('Impostor')} Impostor Remains")
    print("***Alive***")
    alive = sorted(alive.items())
    dead = sorted(dead.items())
    for n, s in alive:
        print(f"{n} : {s}")
    print("***Dead***")
    for n, s in dead:
        print(f"{n} : {s}")
main()
