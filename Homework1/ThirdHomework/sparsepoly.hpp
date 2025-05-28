#pragma once
#include <vector>
#include <iostream>

struct Term {
    int coeff;
    int exp;
    bool operator<(const Term& other) const {
        return exp > other.exp; // 내림차순 정렬
    }
};

class SparsePoly {
public:
    std::vector<Term> terms;

    void addTerm(int coeff, int exp);         // 항 추가
    void input();                             // 사용자 입력
    SparsePoly add(const SparsePoly& other);  // 다항식 덧셈
    void print(const std::string& name) const;// 출력
};
