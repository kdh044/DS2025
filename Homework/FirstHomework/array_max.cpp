#include <iostream>
#include <vector>
using namespace std;

int findMax(const vector<int>& arr) {
    if (arr.empty()) return -1; // 예외 처리
    int maxVal = arr[0];
    for (int num : arr) {
        if (num > maxVal) maxVal = num;
    }
    return maxVal;
}

int main() {
    vector<int> arr = {3, 7, 2, 9, 10, 5}; // 입력값
    cout << "최댓값: " << findMax(arr) << endl;
    return 0;
}
