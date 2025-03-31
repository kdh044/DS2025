#include "Car.h"

int main() {
    SportsCar sc;
    sc = SportsCar(50, (char*)"슈퍼카", 2);  // 생성자 호출

    sc.display();

    sc.setTurbo(false);
    sc.speedUp();  // 일반 가속
    sc.display();

    sc.setTurbo(true);
    sc.speedUp();  // 터보 가속
    sc.display();

    sc.whereAmI();

    return 0;
}
