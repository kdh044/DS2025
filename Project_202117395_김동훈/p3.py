# 프로젝트 문제 3번
input = [[4, 3, 2, 1],
         [0, 0, 0, 0],
         [0, 0, 9, 0],
         [1, 2, 3, 4]]
N = 4

forest = []

def problem3(input):
    bear_size = 2
    honeycomb_count = 0
    time = 0
    bear_x, bear_y = 0, 0
    # 입력 힌트

    # forest 리스트를 input 리스트로 초기화
    forest = [row[:] for row in input]
    
    # 곰의 초기 위치 찾기
    for i in range(N):
        for j in range(N):
            if forest[i][j] == 9:
                bear_x, bear_y = i, j
                forest[i][j] = 0
    print("곰의 초기 위치 x : {0}, y : {1}".format(bear_x, bear_y))

    #여기에서부터 코드를 작성하세요.
    from collections import deque
    result = 0
    def bfs(x, y, size):
        visited = [[False]*N for _ in range(N)]
        q = deque()
        q.append((x, y, 0))
        visited[x][y] = True
        edible = []

        while q:
            cx, cy, dist = q.popleft()
            for dx, dy in [(-1,0),(0,-1),(0,1),(1,0)]:  # 위, 왼, 오, 아래 순
                nx, ny = cx + dx, cy + dy
                if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                    cell = forest[nx][ny]
                    if cell <= size:
                        visited[nx][ny] = True
                        q.append((nx, ny, dist + 1))
                        if 0 < cell < size:
                            edible.append((dist + 1, nx, ny))
        if not edible:
            return None
        edible.sort()
        return edible[0]  # 거리, x, y

    while True:
        target = bfs(bear_x, bear_y, bear_size)
        if not target:
            break
        dist, nx, ny = target
        time += dist
        honeycomb_count += 1
        if honeycomb_count == bear_size:
            bear_size += 1
            honeycomb_count = 0
        forest[nx][ny] = 0
        bear_x, bear_y = nx, ny
    result = time
    return result

result = problem3(input)

assert result == 14
print("정답입니다.")