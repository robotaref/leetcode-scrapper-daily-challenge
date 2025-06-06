#include "bits/stdc++.h"
#include <iostream>
#include <iomanip>
#include <math.h>
#include <cassert>

using namespace std;

double averageWaitingTime(vector<vector<int> >& customers) {
    vector<int> waiting_times(customers.size());
    waiting_times[0] = customers[0][1];
    int lag = 0;

    for (int i = 1; i < customers.size(); i++) {
        if (customers[i-1][0] + customers[i-1][1] > customers[i][0]) {
            lag = customers[i-1][0] + customers[i-1][1] - customers[i][0];
            waiting_times[i] = customers[i][1] + lag;

            customers[i][0] += lag;
        } else {
            waiting_times[i] = customers[i][1];
        }

    }

    return std::accumulate(waiting_times.begin(), waiting_times.end(), 0.0);
}

int main() {
    vector<vector<int> > vec { { 1, 2 }, { 2, 5 }, { 4, 3 } };
    cout << averageWaitingTime(vec) << endl;

}