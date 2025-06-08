#include "bits/stdc++.h"
#include <iostream>
#include <iomanip>
#include <math.h>
#include <cassert>

using namespace std;


class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        int residue;
        vector<int> output;
        std::vector<int>::iterator pos;
        for (int i = 0; i < nums.size(); i++) {
            residue = target - nums[i];
            pos = std::find(nums.begin() + i + 1, nums.end(), residue);
            if (pos != nums.begin() && pos != nums.end()) {
                output.push_back(i);
                output.push_back(pos - nums.begin());
                return output;
            }
        }
        return output;
    }
};