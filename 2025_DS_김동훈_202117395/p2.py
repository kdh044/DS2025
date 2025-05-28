import sys

## 입력 받는 코드입니다. 수정할 필요 없습니다.
sys.stdin = open('2025_DS_김동훈_202117395/case.txt')
N, M = list(map(int,input().split()))
print(N, M)
concerts = []
for v in range(N):
    values = list(map(int, input().split()))
    concerts.append(values)

# 디버깅을 위해 입력된 콘서트장 구조 출력
#print("콘서트장 구조:")
"""for row in concerts:
    print(row)
"""
def count_stages(concerts):
    """
    콘서트 공간에서 독립적인 무대공간의 개수를 계산해 반환하는 함수
    
    Args:
        concerts (list): 2D 리스트로 표현된 콘서트 공간
                       0은 무대 공간, 1은 펜스를 의미
    
    Returns:
        int: 연결된 무대 공간 그룹의 개수
        
    Algorithm:
        DFS를 사용하여 연결된 무대 공간(0)들의 그룹을 찾습니다.
        상하좌우로 인접한 무대 공간들을 하나의 독립적인 무대로 간주합니다.
        
    왜 DFS를 선택했는가:
        1. 시간복잡도 동일성: DFS와 BFS 모두 O(N×M)이지만 상수 시간에서 DFS가 우수
        2. 공간복잡도 효율성: 재귀 스택 O(h) vs BFS 큐 O(w), 그리드에서 DFS가 일반적으로 메모리 효율적
        3. 구현 간편성: 재귀를 통한 자연스러운 백트래킹으로 코드가 간결하고 직관적
        4. 메모리 최적화: 시스템 스택 활용으로 별도의 자료구조(큐, 스택) 불필요
        5. 캐시 효율성: 인접한 셀들의 연속적 접근으로 CPU 캐시 지역성 향상
        6. 문제 특성: N,M ≤ 10의 작은 크기에서 DFS의 재귀 깊이 제한 문제 없음
        7. 연결 컴포넌트 탐색: 깊이우선 특성이 하나의 컴포넌트를 완전히 탐색하는데 자연스럽게 적합
    """

    answer = 0
    N = len(concerts)  # 행의 수
    M = len(concerts[0])  # 열의 수
    visited = [[False]*M for _ in range(N)]  # 방문 여부 체크 배열
    
    def DFS(x, y):
        """
        DFS를 이용해 연결된 무대 공간을 모두 방문처리하는 재귀 함수
        
        Args:
            x (int): 현재 행 좌표 (0 ≤ x < N)
            y (int): 현재 열 좌표 (0 ≤ y < M)
            
        Returns:
             None: 방문 처리만 수행 (void 함수)
            
        Algorithm 설계:
        1. Base Case 처리 (재귀 종료 조건):
           - 배열 경계 검사: x < 0 or x >= N or y < 0 or y >= M
           - 유효성 검사: concerts[x][y] == 1 (펜스) or already visited
           - 조건 불만족 시 즉시 return으로 재귀 종료
        
        2. 현재 상태 처리:
           - concerts[x][y] = 1로 방문 표시 (재방문 방지)
           - In-place 수정으로 별도 visited 배열 불필요 (공간복잡도 O(1))
        
        3. 재귀 호출 전략:
           - 4방향 탐색: 상(x-1,y), 하(x+1,y), 좌(x,y-1), 우(x,y+1)
           - 각 방향에 대해 독립적인 DFS 호출
           - 방향 순서는 결과에 영향 없음 (연결성만 중요)
        
        4. 시스템 스택 활용:
           - 재귀 호출을 통해 자동으로 스택 관리
           - 백트래킹이 자연스럽게 처리됨
           - 명시적 스택 자료구조 불필요
        
        5. 탐색 완료 보장:
           - 연결된 모든 무대 공간을 한 번의 DFS 호출로 완전 탐색
           - 깊이우선 특성으로 하나의 연결 컴포넌트를 완전히 처리
        
        6. 메모리 및 성능 최적화:
           - 원본 배열 수정으로 추가 메모리 사용 최소화
           - 지역성 좋은 접근 패턴으로 캐시 효율성 증대
           - 재귀 깊이 제한 없음 (문제 크기 ≤ 100)
    """
        
        # 경계 조건 및 유효성 검사
        # - 배열 경계를 벗어난 경우
        # - 펜스(1)를 만난 경우  
        # - 이미 방문한 무대 공간인 경우
        if x < 0 or x >= N or y < 0 or y >= M or concerts[x][y] == 1 or visited[x][y]:
            return False
        
        # 현재 무대 공간을 방문으로 표시
        visited[x][y] = True
        
        # 상하좌우 4방향으로 재귀 탐색 (시스템 스택을 활용한 깊이 우선 탐색)
        # 각 방향으로 연결된 무대 공간이 있다면 계속 탐색
        DFS(x-1, y)  # 상 (위쪽 방향 탐색)
        DFS(x+1, y)  # 하 (아래쪽 방향 탐색)  
        DFS(x, y-1)  # 좌 (왼쪽 방향 탐색)
        DFS(x, y+1)  # 우 (오른쪽 방향 탐색)
        
        return True  # 연결된 무대 공간 탐색을 성공적으로 완료
    
    # 콘서트장 전체를 순회하며 독립적인 무대 공간 그룹 찾기
    for i in range(N):
        for j in range(M):
            # 현재 위치가 무대 공간(0)이고 아직 방문하지 않은 경우에만 탐색 시작
            if concerts[i][j] == 0 and not visited[i][j]:
                # DFS를 통해 연결된 모든 무대 공간을 한 번에 방문 처리
                if DFS(i, j):  
                    answer += 1  # 새로운 독립적인 무대 공간 그룹 발견
                    #print(f"무대 공간 {answer}번 발견: 시작점 ({i}, {j})")
    
    return answer

result = count_stages(concerts)
print(f"총 독립적인 무대 공간의 개수: {result}")