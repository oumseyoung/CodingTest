#include <string>
#include <vector>
#include <algorithm>

using namespace std;

string solution(vector<int> numbers) {
    string answer = "";
    vector<string> arr;
    for(int num : numbers) {
        arr.push_back(to_string(num));
    }
    sort(arr.begin(), arr.end(), [](string a, string b) {
        return a + b > b + a;
    });
    
    if(arr[0] == "0") {return "0";}
    
    for(auto i : arr) {
        answer += i;
    }
    return answer;
}