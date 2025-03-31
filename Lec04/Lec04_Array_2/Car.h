#pragma once
#include <cstdio>
#include <cstring>

// ---------------------------
// 🚗 Car 클래스 (부모)
// ---------------------------
class Car {
protected:
    int speed;          // 속도 (private)
    char name[40];      // 이름 (private)

public:
    int gear;           // 기어 (public)

    Car() { }           // 기본 생성자

    ~Car() { }          // 소멸자

    Car(int s, char* n, int g)  // 매개변수 생성자
        : speed(s), gear(g) {
        strcpy(name, n);
    }

    void changeGear(int g = 4) {
        gear = g;
    }

    void speedUp() {
        speed += 5;
    }

    void display() {
        printf("[%s] : 기어=%d단 속도=%dkmph\n", name, gear, speed);
    }

    void whereAmI() {
        printf("객체 주소 = %p\n", this);  // %x → %p
    }
};

// ---------------------------
// 🏎️ SportsCar 클래스 (자식)
// ---------------------------
class SportsCar : public Car {
public:
    bool bTurbo;  // 터보 장치 ON?

    void setTurbo(bool bTur) {
        bTurbo = bTur;
    }

    void speedUp() {
        if (bTurbo)
            speed += 20;
        else
            Car::speedUp();
    }
};
