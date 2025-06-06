#include <iostream>
#include <vector>
#include <algorithm>
#include <numeric>
#include <math.h>

using namespace std;

int findTheWinner(int n, int k) {
    vector<int> v(n);
    iota(v.begin(), v.end(), 1);
    int diff = 0;
    vector<int>::iterator itr = v.begin(); 
    
    while (v.size() > 1) {
        if (itr + k <= v.end()) {
            itr += k - 1;
            v.erase(itr);
            if (itr == v.end()) {
                itr = v.begin();
            }

        } else {
            diff = abs(k - (v.end() - itr) - 1) % v.size();
            itr = v.begin() + diff;

            v.erase(itr);
            if (itr == v.end()) {
                itr = v.begin();
            }
        }
    }
    return v[0];
}

int main() {

    cout << findTheWinner(5, 2) << endl;

}
