#include <string>
#include <vector>
#include <algorithm>

using namespace std;

string solution(string my_string) {
    string removeChars = "aeiou";
    my_string.erase(
        remove_if(my_string.begin(), my_string.end(), [&](char c){
            return removeChars.find(c) != string::npos;
        }), 
        my_string.end()
    );
    return my_string;
}