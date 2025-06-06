#include <iostream>
#include <vector>
#include <algorithm>
#include <map>
#include <math.h>
using namespace std;

map<int, int> make_map(vector<int> vec1, vector<int> vec2) {   
    map<int, int> map;
    std::transform(vec1.begin(), vec1.end(), vec2.begin(), std::inserter(map, map.end()), [](int a, int b)
{
    return std::make_pair(a, b);
});
    return map;
}

map<int, int> primeFactors(int n) 
{   
    map<int, int> factors;
    // Print the number of 2s that divide n 
    while (n % 2 == 0) 
    { 
        factors[2]++;
        n = n/2;
    } 
 
    // n must be odd at this point. So we can skip 
    // one element (Note i = i +2) 
    for (int i = 3; i <= sqrt(n); i = i + 2) 
    { 
        // While i divides n, print i and divide n 
        while (n % i == 0) 
        { 
            factors[i]++;
            n = n/i; 
        } 
    } 
 
    // This condition is to handle the case when n 
    // is a prime number greater than 2 
    if (n > 2) {
        factors[n]++; 
    }
    return factors;
} 

bool judgeSquareSum(int c) {
    bool judge = true;
    map<int, int> factors = primeFactors(c);
    
    // map<int, int> repeats;
    // for (int i = 0; i < factors.size(); i++) {
    //     if (repeats.find(factors[i]) == repeats.end()) {
    //         repeats[factors[i]] = 1;
    //     } else {
    //         repeats[factors[i]] += 1;
    //     }
    // }

    for (auto it = factors.begin(); it != factors.end(); ++it) {
        // cout << it->first << " " << it->second << endl;
        if (it->first % 4 == 3 && it->second % 2 == 1) {
            judge = false;
        }
    }

    return judge;
}


int main() {
    cout << judgeSquareSum(4294967295) << endl;
}