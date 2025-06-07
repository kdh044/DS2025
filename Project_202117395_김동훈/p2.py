# 프로젝트 문제 2번
input = ")))()"

def problem2(input):          
    open_count = 0            
    close_count = 0

    for char in input:  
        if char == '(':      
            open_count += 1   
        else: # ')'
            if open_count > 0:  
                open_count -= 1
            else:
                close_count += 1
    result = close_count + open_count
    # 입력 힌트
    for char in input:
        print(char)
    return result

result = problem2(input)
assert result == 3
print("정답입니다.")