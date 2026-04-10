# 문제 10828

# user_input = input().split()
# num = len(user_input) = 1
# print(user_input)
# print(num)

# 아니 시간제한 어케 맞추냐 눈물난다 진짜...
import sys
input = sys.stdin.readline

turn = int(input())
statck = []
user_input = []

# statck에 데이터 늘어가는지 테스트
# input_len = len(user_input)

# if user_input[0] == 'push':
#     data = int(user_input[input_len-1])
#     statck.append(data)
# print(statck)

for i in range(0,turn):
    # 입력을 받는다
    user_input = input().split()
    input_len = len(user_input)
    index_0 = user_input[0]
    
    # 입력값이 한개일때
    if input_len <= 1:
        if index_0 == 'top':
            if len(statck) > 0:
                print(statck[-1])
            else:
                print(-1)
        elif index_0 == 'size':
            data = len(statck)
            print(data)
        elif index_0 == 'empty':
            if len(statck) < 1:
                print(1)
            else:
                print(0)
        elif index_0 == 'pop':
            if len(statck) > 0:
                print(statck.pop())
            else:
                print(-1)
    # 입력값이 두개일때
    elif input_len == 2:
        if index_0 == 'push':
            statck.append(user_input[input_len-1])