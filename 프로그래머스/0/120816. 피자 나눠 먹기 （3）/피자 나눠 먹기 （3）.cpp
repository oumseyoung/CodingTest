#include <string>
#include <vector>

using namespace std;

int solution(int slice, int n) { 
    int answer;
    if(n <= slice) { return 1; }
    else {
        answer = n / slice;
        if(n % slice) {
            answer += 1;
        }
        return answer;
    }
}