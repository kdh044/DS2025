def bubble_sort(a_list):
    for pass_num in range(len(a_list) - 1, 0, -1):
        for i in range(pass_num):
            if a_list[i] > a_list[i + 1]:
                temp = a_list[i]
                a_list[i] = a_list[i + 1]
                a_list[i + 1] = temp

# 예시
arr = [5, 8, 4, 9, 1, 6, 2, 7]
bubble_sort(arr)
print("Bubble Sort 결과:", arr)
