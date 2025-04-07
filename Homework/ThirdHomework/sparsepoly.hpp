#pragma once
#include <vector>
#include <iostream>

struct Term {
    int coeff;
    int exp;
    bool operator<(const Term& other) const {
        return exp > other.exp;
    }
};

class SparsePoly {
public:
    std::vector<Term> terms;
    void addTerm(int coeff, int exp);
    void input(); // 사용자 입력 함수
    SparsePoly add(const SparsePoly& other);
    void print(const std::string& name) const;
};
