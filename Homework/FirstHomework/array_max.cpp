#include <iostream>
#include <vector>
using namespace std;

// 최대값 구하기
int findMax(const vector<int>& arr) {
    if (arr.empty()) return -1;
    int maxVal = arr[0];
    for (int num : arr) {
        if (num > maxVal) maxVal = num;
    }
    return maxVal;
}

// 배열 출력 함수
void printArray(const vector<int>& arr) {
    cout << "[ ";
    for (int num : arr) {
        cout << num << " ";
    }
    cout << "]";
}

int main() {
    // 여러 개의 테스트 배열
    vector<vector<int>> testArrays = {
        {3, 7, 2, 9, 10, 5},
        {-10, -5, -3},
        {100, 200, 300, 50, 400},
        {0, 0, -2, 0},
        {10000}
    };

    // 각 배열에 대해 출력
    for (size_t i = 0; i < testArrays.size(); ++i) {
        cout << "배열 " << i + 1 << ": ";
        printArray(testArrays[i]);
        cout << " → 최댓값: " << findMax(testArrays[i]) << endl;
    }

    return 0;
}
