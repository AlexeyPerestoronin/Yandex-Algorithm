#include <iostream>
#include <map>

int main() {
    std::map<char, int> symbols{};

    std::string f{}, s{};
    std::cin >> f;
    std::cin >> s;

    for (auto ch : f)
        ++(symbols[ch]);

    for (auto ch : s)
        --(symbols[ch]);

    for (auto [ch, num] : symbols)
        if (num != 0) {
            std::cout << 0;
            return 0;
        }

    std::cout << 1;
    return 0;
}
