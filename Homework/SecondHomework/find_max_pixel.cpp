#include <iostream>
#include <opencv2/opencv.hpp>
using namespace std;
using namespace cv;

int findMaxPixel(const Mat& img) {
    double minVal, maxVal;
    minMaxLoc(img, &minVal, &maxVal);
    return static_cast<int>(maxVal);
}

int main() {
    Mat img = imread("/home/danny/Desktop/DS2025/Homework/SecondHomework/Lenna.png", IMREAD_UNCHANGED);
    if (img.empty()) {
        cout << "이미지를 불러올 수 없습니다." << endl;
        return -1;
    }
    cout << "최대 밝기 값: " << findMaxPixel(img) << endl;
    return 0;
}
