#include <iostream>
#include <vector>
#include <algorithm>
#include <map>
#include <math.h>

using namespace std;


int find_max_less(int index, vector<int>& vec, vector<int> ref_vec, int value) {
    vector<int>::const_iterator first = vec.begin();
    if (vec[index] > value) {
        vector<int>::const_iterator first = vec.begin();
    } 
    
    while ( first != vec.end() && !( *first <= value ) ) {
        first++;
        }
    int max_ref = ref_vec[first - vec.begin()];
    vector<int>::const_iterator max = first;
    for (int i = first - vec.begin(); i < vec.size(); i++ ) {
        first++;
        if ( *first <= value && ref_vec[first - vec.begin()] > max_ref) {
            max = first;
            }
        }
    return ref_vec[max - vec.begin()];
}


int maxProfitAssignment(vector<int>& difficulty, vector<int>& profit, vector<int>& worker) {
    int sum_profit = 0;
    for (int i = 0; i < worker.size(); i++) {
        vector<int>::const_iterator first = difficulty.begin();

        while ( first != difficulty.end() && !( *first <= worker[i] ) ) {
            first++;
            }
        int max_ref = profit[first - difficulty.begin()];
        vector<int>::const_iterator max = first;
        for (int j = first - difficulty.begin(); j < difficulty.size(); j++ ) {
            first++;
            if ( *first <= worker[i] && profit[first - difficulty.begin()] >= max_ref) {
                max = first;
                max_ref = profit[first - difficulty.begin()];
                }
            }
        if (max != difficulty.end()) {
            sum_profit += profit[max - difficulty.begin()];
        }
    
        }
    return sum_profit;
}


int main() {
    int list1[] = { 5,50,92,21,24,70,17,63,30,53 };
    vector<int> difficulty(begin(list1), end(list1));
    int list2[] = { 68,100,3,99,56,43,26,93,55,25 };
    vector<int> profit(begin(list2), end(list2));
    int list3[] = { 96,3,55,30,11,58,68,36,26,1 };
    vector<int> worker(begin(list3), end(list3));

    cout << maxProfitAssignment(difficulty, profit, worker) << endl;
}