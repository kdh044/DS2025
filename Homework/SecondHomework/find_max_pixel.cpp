#include <iostream>
#include <opencv2/opencv.hpp>
using namespace std;
using namespace cv;

int main() {
    // 이미지 그레이스케일로 불러오기
    Mat img = imread("Lenna.png", IMREAD_GRAYSCALE);

    if (img.empty()) {
        cout << "이미지를 불러올 수 없습니다." << endl;
        return -1;
    }

    // 최대 화소 밝기 구하기
    double minVal, maxVal;
    minMaxLoc(img, &minVal, &maxVal);

    cout << "최대 화소 밝기값: " << maxVal << endl;
    return 0;
}
