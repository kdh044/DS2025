#include <iostream>

int findMax(int arr[], int size) {
    int maxVal = arr[0];  // 배열의 첫 번째 요소를 최댓값으로 가정
    for (int i = 1; i < size; i++) {
        if (arr[i] > maxVal) {
            maxVal = arr[i];
        }
    }
    return maxVal;
}

int main() {
    int arr[] = {3, 7, 2, 9, 1, 5};  // 테스트할 배열
    int size = sizeof(arr) / sizeof(arr[0]);

    std::cout << "최댓값: " << findMax(arr, size) << std::endl;
    return 0;
}
