#include "sparsepoly.hpp"
#include <algorithm>

void SparsePoly::addTerm(int coeff, int exp) {
    if (coeff == 0) return;

    // 이미 같은 차수가 있으면 누적
    for (auto& term : terms) {
        if (term.exp == exp) {
            term.coeff += coeff;
            return;
        }
    }
    terms.push_back({coeff, exp});
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

    // A 항 복사
    for (const auto& term : terms)
        result.addTerm(term.coeff, term.exp);

    // B 항 더하기
    for (const auto& term : other.terms)
        result.addTerm(term.coeff, term.exp);

    return result;
}

void SparsePoly::print(const std::string& name) const {
    std::vector<Term> sortedTerms = terms;
    std::sort(sortedTerms.begin(), sortedTerms.end());

    std::cout << "다항식 " << name << ": ";
    bool first = true;
    for (const auto& term : sortedTerms) {
        if (term.coeff == 0) continue;

        if (!first) std::cout << " + ";
        std::cout << term.coeff << "x^" << term.exp;
        first = false;
    }
    std::cout << std::endl;
}

int main() {
    SparsePoly A, B;

    std::cout << "[다항식 A 입력]" << std::endl;
    A.input();

    std::cout << "\n[다항식 B 입력]" << std::endl;
    B.input();

    SparsePoly C = A.add(B);

    std::cout << "\n[덧셈 결과: A + B]" << std::endl;
    A.print("A");
    B.print("B");
    C.print("A + B");

    return 0;
}
