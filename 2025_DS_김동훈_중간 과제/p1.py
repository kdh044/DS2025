from collections import deque

A = {
    0: [1, 2, 3],
    1: [0, 2, 4, 5],
    2: [0, 1, 6],
    3: [0],
    4: [1],
    5: [1],
    6: [2]
}
def bfs(A):
    """
    [과제 1-1] 너비 우선 탐색(BFS) 구현
    
    기능 개요:
    주어진 그래프에서 시작 노드(0번)부터 너비 우선 탐색을 수행하여 
    모든 노드를 방문하는 순서를 반환하는 함수입니다.
    BFS는 현재 노드와 같은 레벨의 모든 노드를 먼저 방문한 후 
    다음 레벨로 넘어가는 특징을 가집니다.
    
    구현 방법:
    1. 자료구조 선택: collections.deque를 사용하여 큐 구현
       - deque.popleft()와 append()로 O(1) 시간에 삽입/삭제 가능
       - 일반 리스트의 pop(0)은 O(n)이므로 성능상 deque가 유리
    
    2. 방문 관리: visited 리스트로 중복 방문 방지
       - visited[i] = True/False로 i번 노드의 방문 여부 저장
       - 큐에 삽입할 때 즉시 방문 처리하여 중복 삽입 방지
    
    3. 탐색 순서 제어: sorted() 함수로 인접 노드를 오름차순 정렬
       - 문제에서 요구하는 "낮은 번호부터 우선 방문" 조건 만족
       - 일관된 결과를 보장하여 테스트 케이스 통과
    
    동작 과정:
    초기: queue=[0], visited[0]=True
    1단계: 0 방문 → 인접노드 1,2,3을 큐에 추가 → queue=[1,2,3]
    2단계: 1 방문 → 미방문 인접노드 4,5를 큐에 추가 → queue=[2,3,4,5]
    3단계: 2 방문 → 미방문 인접노드 6을 큐에 추가 → queue=[3,4,5,6]
    4단계: 3,4,5,6 순서대로 방문하여 탐색 완료
    
    Args:
        A (dict): 인접 리스트로 표현된 그래프
                 key: 노드 번호(int), value: 인접 노드 리스트(list)
    
    Returns:
        list: BFS 순서로 방문한 노드들의 리스트 [0,1,2,3,4,5,6]
        
    시간복잡도: O(V + E) - 모든 노드와 간선을 한 번씩 방문
    공간복잡도: O(V) - visited 배열과 큐에 최대 V개 노드 저장
    """

    answer = []
    visited = [False] * len(A)
    queue = deque([0])
    visited[0] = True

    while queue:
        node = queue.popleft()
        answer.append(node)

        for neighbor in sorted(A[node]):  # 낮은 번호부터 방문
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)

    return answer

def dfs(A):
    """
    [과제 1-2] 깊이 우선 탐색(DFS) 구현
    
    기능 개요:
    주어진 그래프에서 시작 노드(0번)부터 깊이 우선 탐색을 수행하여
    모든 노드를 방문하는 순서를 반환하는 함수입니다.
    DFS는 한 경로를 끝까지 탐색한 후 백트래킹하여 다른 경로를 탐색하는 특징을 가집니다.
    
    구현 방법:
    1. 자료구조 선택: Python 리스트를 스택으로 활용
       - append()와 pop()을 사용하여 LIFO(Last In First Out) 구현
       - 재귀 함수 대신 반복문 + 스택으로 구현하여 스택 오버플로우 방지
    
    2. 방문 순서 제어의 핵심: reversed() 함수 사용
       - 인접 노드를 역순으로 스택에 삽입
       - 스택의 LIFO 특성으로 인해 결과적으로 낮은 번호부터 방문됨
       - 예: [1,4,5] → reversed([1,4,5]) = [5,4,1] → 스택에서 pop할 때 1,4,5 순서
    
    3. 조기 방문 처리: 스택에 삽입할 때 즉시 visited=True 설정
       - 같은 노드가 스택에 중복으로 들어가는 것을 방지
       - 메모리 사용량 최적화 및 정확한 탐색 보장
    
    동작 과정:
    초기: stack=[0], visited[0]=True
    1단계: 0 방문 → 인접노드를 역순으로 스택에 추가 → stack=[3,2,1]
    2단계: 1 방문(pop) → 미방문 인접노드를 역순 추가 → stack=[3,2,5,4]
    3단계: 4 방문(pop) → 인접노드 없음 → stack=[3,2,5]
    4단계: 5 방문(pop) → 인접노드 없음 → stack=[3,2]
    5단계: 2 방문(pop) → 미방문 인접노드 6 추가 → stack=[3,6]
    6단계: 6,3 순서대로 방문하여 탐색 완료
    
    왜 이런 구현을 선택했는가:
    - 재귀 vs 반복: 깊은 그래프에서 안전성을 위해 반복 구현 선택
    - 방문 순서: 문제 요구사항인 "낮은 번호 우선"을 만족하기 위한 reversed() 활용
    - 성능: 시간복잡도 O(V+E)로 최적, 추가 정렬 없이 원하는 순서 달성
    
    Args:
        A (dict): 인접 리스트로 표현된 그래프
                 key: 노드 번호(int), value: 인접 노드 리스트(list)
    
    Returns:
        list: DFS 순서로 방문한 노드들의 리스트 [0,1,4,5,2,6,3]
        
    시간복잡도: O(V + E) - 모든 노드와 간선을 한 번씩 방문
    공간복잡도: O(V) - visited 배열과 스택에 최대 V개 노드 저장
    """
     
    answer = []
    visited = [False]*len(A)
    stack = [0]
    visited[0] = True

    while stack:
        node = stack.pop()
        answer.append(node)

        for neighbor in reversed(A[node]):
            if not visited[neighbor]:
                stack.append(neighbor)
                visited[neighbor] = True

    return answer

# 아래는 체크함수입니다. 수정하실 필요 없습니다.
bfs_result = bfs(A)
dfs_result = dfs(A)
print("실제 DFS 결과:", dfs_result)

assert bfs_result == [0,1,2,3,4,5,6]
assert dfs_result == [0,1,4,5,2,6,3]
print('PASSED!')

