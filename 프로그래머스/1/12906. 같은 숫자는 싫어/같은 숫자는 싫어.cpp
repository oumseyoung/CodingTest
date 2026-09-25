#include <vector>
#include <iostream>
#include <stack>

using namespace std;

vector<int> solution(vector<int> arr) 
{
    vector<int> answer;
    for(int i=0; i<arr.size(); i++) {
        if(answer.empty() == true) {
            answer.push_back(arr[i]);
        }
        else if(arr[i] != answer[answer.size()-1]) {
            answer.push_back(arr[i]);
        }
    }
    
    return answer;
}