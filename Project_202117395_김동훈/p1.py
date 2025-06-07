# 프로젝트 문제 1번
input = [10, 40, 30, 60, 30]        #N = 5 이기 때문에 상수

def problem1(input):                # 아래는 실행 횟수
    mean = sum(input)/len(input)    # # sum은 5번(덧셈) + len은 1번(접근) + 나눗셈 1번 + 대입 1번
    input.sort()                    # 5log5(정렬)
    median = input[2]               # 1번(대입)
    result = [0,0]                  # 1번(대입)
    result[0] = mean                # 1번(대입)
    result[1] = median              # 1번(대입)
    return result                   # 1번(반환)

result = problem1(input)            

assert result == [34, 30]
print("정답입니다.")
