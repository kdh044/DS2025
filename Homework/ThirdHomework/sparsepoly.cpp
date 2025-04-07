#include "sparsepoly.hpp"
#include <algorithm>

void SparsePoly::addTerm(int coeff, int exp) {
    if (coeff != 0) {
        terms.push_back({coeff, exp});
    }
}

void SparsePoly::input() {
    int n;
    std::cout << "항의 개수를 입력하세요: ";
    std::cin >> n;
    for (int i = 0; i < n; ++i) {
        int c, e;
        std::cout << i + 1 << "번째 항의 계수와 차수를 입력하세요 (예: 계수 차수): ";
        std::cin >> c >> e;
        addTerm(c, e);
    }
}

SparsePoly SparsePoly::add(const SparsePoly& other) {
    SparsePoly result;
    std::vector<Term> A = terms;
    std::vector<Term> B = other.terms;
    std::sort(A.begin(), A.end());
    std::sort(B.begin(), B.end());

    size_t i = 0, j = 0;
    while (i < A.size() && j < B.size()) {
        if (A[i].exp == B[j].exp) {
            int sum = A[i].coeff + B[j].coeff;
            if (sum != 0)
                result.addTerm(sum, A[i].exp);
            ++i; ++j;
        } else if (A[i].exp > B[j].exp) {
            result.addTerm(A[i].coeff, A[i].exp);
            ++i;
        } else {
            result.addTerm(B[j].coeff, B[j].exp);
            ++j;
        }
    }

    while (i < A.size()) result.addTerm(A[i].coeff, A[i].exp), ++i;
    while (j < B.size()) result.addTerm(B[j].coeff, B[j].exp), ++j;

    return result;
}

void SparsePoly::print(const std::string& name) const {
    std::cout << "Poly " << name << ": ";
    for (size_t i = 0; i < terms.size(); ++i) {
        std::cout << terms[i].coeff << ".0x^" << terms[i].exp;
        if (i != terms.size() - 1) std::cout << " + ";
    }
    std::cout << std::endl;
}

// ------------------ main ------------------
int main() {
    SparsePoly A, B;
    std::cout << "[다항식 A 입력]" << std::endl;
    A.input();
    A.print("A");

    std::cout << "\n[다항식 B 입력]" << std::endl;
    B.input();
    B.print("B");

    SparsePoly C = A.add(B);
    std::cout << "\n[결과 다항식 C = A + B]" << std::endl;
    C.print("C");

    return 0;
}
