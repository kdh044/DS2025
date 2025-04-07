#include "SportsCar.h"

int main() {
    Car myCar;
    Car momsCar(10, "K5", 2);
    SportsCar mySecondCar;

    myCar.whereAmI();
    momsCar.whereAmI();

    myCar.changeGear(3);
    momsCar.speedUp();
    momsCar.display();

    mySecondCar.setTurbo(true);

    return 0;
}
