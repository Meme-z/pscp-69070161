"""milktea"""
def main():
    """milktea"""
    bubble , gram = input().split()
    tea , sweet , cc = input().split()
    gram = float(gram)
    sweet = int(sweet)
    cc = float(cc)
    bc = { 'H': 5, 'O': 3, 'J': 2 }
    tc = { 'R': [12,18,25], 'T': [15,20,30], 'M': [10,15,20] }
    energy = bc[bubble] * gram + tc[tea][sweet-1] * cc
    if energy == int(energy):
        print(int(energy))
    else:
        print(energy)
main()
