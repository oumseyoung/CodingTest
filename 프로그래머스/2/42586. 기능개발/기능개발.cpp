#include <string>
#include <vector>

using namespace std;

vector<int> solution(vector<int> progresses, vector<int> speeds) {
    vector<int> answer;
    vector<int> days(progresses.size(), 0);
    for(int i=0; i<progresses.size(); i++) {
        days[i] = (99 - progresses[i] + speeds[i]) / speeds[i];
    }
    int start = 0;
    int i, cnt;
    while(start < days.size()) {
        cnt = 1;
        for(i=start+1; i<progresses.size(); i++) {
            if(days[start] >= days[i]) {
                cnt++;
            }
            else { break; }
        }
        start = i;
        answer.push_back(cnt);
    }
    
    return answer;
}