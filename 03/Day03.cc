#include<bits/stdc++.h>
using namespace std;

vector<string> get_lines(string file_name) {
    vector<string> res;
    ifstream file(file_name);
    string s;
    while(getline(file, s)) {
        res.push_back(s);
    }
    return res;
}

int priority(char c) {
    if(c >= 'a') {
            return (c - 'a') + 1;
        }
        else {
            return (c - 'A') + 27;
        } 
}

void solve_1(string file_name) {
    int ans = 0;

    vector<string> lines = get_lines(file_name);

    for(string& s : lines) {
        string t = s.substr(s.length() / 2);
        for(int i = 0; i < s.length() / 2; i++) {
            if(t.contains(s[i])) {
                ans += priority(s[i]);
                break;
            }
        }
    }

    cout << "Part 1: " << ans << '\n';
}

void solve_2(string file_name) {
    int ans = 0;

    vector<string> lines = get_lines(file_name);

    for(int i = 0; i < lines.size(); i += 3) {
        string s = lines[i], s1 = lines[i + 1], s2 = lines[i + 2];
        char c = '0';
        set<char> st1;
        for(char c1 : s) {
            st1.insert(c1);
        }
        set<int> st2;
        for(char c1 : s1) {
            if(st1.contains(c1)) {
                st2.insert(c1);
            }
        }
        for(char c1 : s2) {
            if(st2.contains(c1)) {
                c = c1;
                break;
            }
        }

        ans += priority(c);
    }

    cout << "Part 2: " <<  ans << '\n';
}

int main() {
    solve_1("input.txt");
    solve_2("input.txt");
    return 0;
}