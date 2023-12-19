def heapify(arr, n, i):
    largest = i  # 현재 노드를 가장 큰 값으로 설정한다
    left = 2 * i + 1  # 왼쪽 자식 노드의 인덱스
    right = 2 * i + 2  # 오른쪽 자식 노드의 인덱스

    # 왼쪽 자식이 부모보다 크면 largest 갱신
    if left < n and arr[left] > arr[largest]:
        largest = left

    # 오른쪽 자식이 부모나 왼쪽 자식보다 크면 largest 갱신gk기
    if right < n and arr[right] > arr[largest]:
        largest = right

    # largest가 변경되었으면 노드 교환
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]

        # 교환 후 하위 서브트리에 대해 재귀적으로 heapify 호출한다
        heapify(arr, n, largest)


def build_max_heap(arr):
    n = len(arr)

    # 내부 노드부터 역순으로 heapify 호출
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)


# 주어진 숫자 배열
numbers = [10, 40, 30, 5, 12, 6, 15, 9, 60]

# 최대 힙 트리 구성
build_max_heap(numbers)

print("최대 힙 트리:", numbers)


