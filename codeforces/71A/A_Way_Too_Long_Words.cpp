#include<bits/stdc++.h>
using namespace std;

void solve(string word) {
    int n = word.length();
    if (n > 10) {
        char begin = word.at(0);
        char end = word.at(n-1);
        cout << begin << n-2 << end << endl;
    } else {
        cout << word << endl;
    }

}
int main() {
    int t;
    cin >> t;
    for (int i = 0; i < t; i++) {
        string word;
        cin >> word;
        solve(word);
    }

    return 0;
}