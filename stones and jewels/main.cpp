#include <algorithm>
#include <fstream>
#include <vector>

int main() {
    std::ifstream input{ "input.txt" };

    std::string j{}, s{};
    
    input >> j >> s;

    int result = 0;
    for (const char ch : s) {
        result += j.find(ch) != std::string::npos;
    }

    std::ofstream output{ "output.txt" };
    output << result;

    return 0;
}