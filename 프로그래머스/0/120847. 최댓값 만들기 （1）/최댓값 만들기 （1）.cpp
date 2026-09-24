#include <string>
#include <vector>

using namespace std;

int solution(vector<int> numbers) {
    int max = numbers[0] * numbers[1];
    int calculate;
    for(int i=1; i<numbers.size()-1; i++) {
        for(int j=i+1; j<numbers.size(); j++) {
            calculate = numbers[i] * numbers[j];
            if(calculate > max) {
                max = calculate;
            }
        }
    }
    return max;
}