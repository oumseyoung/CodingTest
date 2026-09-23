#include <string>
#include <vector>

using namespace std;

int solution(int num1, int num2) {
    int answer = 0;
    answer = static_cast<int>(static_cast<double>(num1) / static_cast<double>(num2) * 1000);
    return answer;
}