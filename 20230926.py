#백준14681사분면 고르기 https://www.acmicpc.net/problem/14681

score = int(input())
if 90<=score<=100:
    print('A')
elif 80<=score:
    print('B')
elif 70<=score:
    print('C')
elif 60<=score:
    print('D')
else:
    print('F')
