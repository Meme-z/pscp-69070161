"""w"""
def main():
    """ww8"""
    from math import ceil
    work = int(input())
    day = work
    hour = []
    more = 0
    nm = 0
    for _ in range(work):
        hour.append(int(input()))
    for i in hour:
        if i > 18:
            more += 1
        else:
            nm += 1
    if more/2 > nm:
        day += ceil(more/2)-nm
    print(day)
main()
