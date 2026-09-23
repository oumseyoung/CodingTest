#include <string>
#include <vector>

using namespace std;

string solution(string my_string, int n) {
    string answer = "";
    for(char alpha : my_string) {
        answer += string(n, alpha);
    }
    return answer;
}