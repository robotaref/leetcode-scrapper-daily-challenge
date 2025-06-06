#include "bits/stdc++.h"
#include <iostream>
using namespace std;

string reverse(string s) {
    string r_s;
    for (int i = s.size() - 1; i >= 0; i--) {
        if (s[i] == ')') {
            r_s.push_back('(');
        } else if (s[i] == '(') {
            r_s.push_back(')');
        } else {
            r_s.push_back(s[i]);
        }
    
    }
    return r_s;
}

vector<int> find_parantheses(string s) {
    vector<int> indices;
    for (int i = 0; i < s.size(); i++) {
        if (s[i] == '(') {
            indices.push_back(i);
            break;
        }
    }

    int in_between_parantheses = 0;
    if (indices.empty()) {
        indices.push_back(-1);
        indices.push_back(-1);
        return indices;
    }
    for (int j = indices[0] + 1; j < s.size(); j++) {
        if (s[j] == '(') {
            in_between_parantheses++;
        }
        if (s[j] == ')') {
            if (in_between_parantheses == 0) {
                indices.push_back(j);
                break;
            } else {
                in_between_parantheses--;
            }
        }
    }

    if (indices.size() < 2) {
        indices.push_back(-1);
        indices.push_back(-1);
    }

    return indices;
}


string reverseParentheses(string s) {
    vector<int> indices = find_parantheses(s);
    string to_replace;
    while (indices[0] != -1 && indices[1] != -1) {
        to_replace = reverse(s.substr(indices[0] + 1, indices[1] - indices[0] - 1));
        s.replace(indices[0], indices[1] - indices[0] + 1, to_replace);
        indices = find_parantheses(s);
    }

    return s;
}

int main() {
    string word = "ta()usw((((a))))";
    word = reverseParentheses(word);
    cout << word << endl;

    return 0;
} 