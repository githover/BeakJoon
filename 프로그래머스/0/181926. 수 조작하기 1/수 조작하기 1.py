def solution(n, control):
    answer = 0
    for i in control:
        if i=='w':
            n = n+1
        elif i=='s':
            n = n-1
        elif i=='d':
            n = n+10
        else:
            n = n-10
    return n