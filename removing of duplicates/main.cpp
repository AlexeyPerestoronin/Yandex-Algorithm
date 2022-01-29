#include <fstream>
#include <queue>

int getInt() {
    static std::ifstream input{ "input.txt" };
    int result;
    input >> result;
    return result;
}

void putInt(int i_num) {
    static std::ofstream output{ "output.txt", std::ios::trunc };
    static uint32_t counter{0};
    if (counter++ != 0)
        output << '\n';
    output << i_num;
}

int main() {
    // creating the empty output.txt file before start a general logic
    std::ofstream{ "output.txt", std::ios::trunc };

    std::queue<int> nums{};
    for (int numQuantity{ getInt() }; numQuantity > 0; --numQuantity) {
        int num{ getInt() };
        nums.push(num);
        if (size_t size = nums.size(); size == 1) {
            putInt(num);
        } else if (size == 2) {
            if (int prevNum{ nums.front() }; num != prevNum)
                putInt(num);
            nums.pop();
        }
    }

    return 0;
}
