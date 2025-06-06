#include "bits/stdc++.h"
#include <iostream>
#include <iomanip>
#include <math.h>
#include <cassert>

using namespace std;




int minIncrementForUnique(vector<int>& nums) {
    int count = 0;
    sort(nums.begin(), nums.end());
    int i = 0;
    int j = i;
    do {
        j = i + 1;
        while (nums[j] == nums[i]) {
            nums[j]++;
            j++;
            count++;
        }
        i++;
    } while (i < nums.size());
    return count;
}

int main() {
    int list[] = { 3, 2, 1, 2, 1, 7 };
    vector<int> nums(begin(list), end(list));
    cout << minIncrementForUnique(nums) << endl;
}