#include <fstream>
#include <string>

int getInt() {
    static std::ifstream input{ "input.txt" };
    int result;
    input >> result;
    return result;
}

void putString(const std::string& i_str) {
    static std::ofstream output{ "output.txt", std::ios::trunc };
    static uint32_t counter{ 0 };
    if (counter++ != 0)
        output << '\n';
    output << i_str;
}

void generateBrackets(int i_open, int i_close = 0, std::string i_res = "") {
    if (i_open > 0)
        generateBrackets(i_open - 1, i_close + 1, std::string{ i_res }.append("("));

    if (i_close > 0)
        generateBrackets(i_open, i_close - 1, std::string{ i_res }.append(")"));

    if (i_open == 0 && i_close == 0)
        putString(i_res);
}

int main() {
    // creating the empty output.txt file before start a general logic
    std::ofstream{ "output.txt", std::ios::trunc };

    generateBrackets(getInt());

    return 0;
}
