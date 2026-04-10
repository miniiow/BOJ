# 단어 순서 뒤집기

turn = int(input())
for i in range(turn):
    user_input = input().split()
    print(f'Case #{i+1}: ', end='')
    for j in range(len(user_input)-1, -1, -1):
        print(user_input[j], end=' ')
    print()