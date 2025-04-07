#ifndef SPORTSCAR_H
#define SPORTSCAR_H

#include "Car.h"

class SportsCar : public Car {
private:
    bool turbo;

public:
    SportsCar() : turbo(false) {
        // 기본값 설정
        speed = 20;
        gear = 5;
        strcpy(name, "Porsche911");
    }

    void setTurbo(bool t) {
        turbo = t;
        if (turbo) {
            printf("🚀 Turbo 모드 ON!\n");
            speed += 50;
        } else {
            printf("🛑 Turbo 모드 OFF!\n");
        }
    }
};

#endif
