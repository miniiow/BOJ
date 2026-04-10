# 주몽

N = int(input())
M = int(input())
material_num_list = list(map(int, input().split()))

start = 0
end = N -1
# print(end)
# print(material_num_list)
material_num_list.sort()
# print(material_num_list)
count = 0

while True:
    if start > end or start == end:
        break
    # 둘의 합이 M보다 작을때 sart를 늘림
    # print('start:', start, 'end:', end)

    if material_num_list[start] + material_num_list[end] < M:
        start += 1
    # 둘의 합이 M보다 크면 end를 줄임
    elif material_num_list[start] + material_num_list[end] > M:
        end -= 1
    # 조건에 맞으면 카운트를 1 더하고 start를 1늘리고, end를 1줄임
    elif material_num_list[start] + material_num_list[end] == M:
        count += 1
        start += 1
        end -= 1
    # 위 내용 반복
print(count)