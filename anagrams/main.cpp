#include <fstream>
#include <map>

char getChar() {
    static std::ifstream input{ "input.txt" };
    char result{ '\0' };
    if (input.peek() != EOF)
        input.get(result);
    return result;
}

void putInt(int i_num) {
    static std::ofstream output{ "output.txt", std::ios::trunc };
    output << i_num;
}

int main() {
    std::map<char, int> symbols{};

    for (char ch{ getChar() }; ch != '\n'; ch = getChar()) {
        symbols[ch]++;
    }

    for (char ch{ getChar() }; ch != '\0'; ch = getChar()) {
        symbols[ch]--;
    }

    int result{ 1 };
    for (auto [ch, num] : symbols)
        if (num != 0) {
            result = 0;
            break;
        }

    putInt(result);
    return 0;
}
