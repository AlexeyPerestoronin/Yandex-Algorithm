#include <fstream>
#include <vector>

int getInt() {
    static std::ifstream input{ "input.txt" };
    int result;
    input >> result;
    return result;
}

int main() {
    std::vector<int> numbers{};

    for (int numQuantity{ getInt() }; numQuantity > 0; --numQuantity)
        numbers.push_back(getInt());

    int max{ 0 }, local_max{ 0 };
    for (int number : numbers)
        if (number == 1) {
            ++local_max;
            max = std::max(max, local_max);
        } else {
            local_max = 0;
        }

    std::ofstream output{ "output.txt" };
    output << max;

    return 0;
}
