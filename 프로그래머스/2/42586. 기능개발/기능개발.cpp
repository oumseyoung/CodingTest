#include <string>
#include <vector>

using namespace std;

vector<int> solution(vector<int> progresses, vector<int> speeds) {
    vector<int> answer;
    int cnt = 1;
    int first = (100 - progresses[0] + speeds[0] -1) / speeds[0];

    for(int i=1; i<progresses.size(); i++) {
        int day = (100 - progresses[i] + speeds[i] -1) / speeds[i];
        if(first >= day) {
            cnt++;
        }
        else { answer.push_back(cnt); cnt = 1; first = day; }
    }
    answer.push_back(cnt);
    
    return answer;
}