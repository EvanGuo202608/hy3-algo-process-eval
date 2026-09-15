#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;

int main() {
    int n, limit;
    if (!(cin >> n >> limit)) return 0;
    vector<int> weights(n);
    for (int i = 0; i < n; ++i) cin >> weights[i];

    sort(weights.begin(), weights.end());
    int left = 0;
    int right = n - 1;
    int groups = 0;

    while (left <= right) {
        if (left < right && weights[left] + weights[right] <= limit) {
            ++left;
        }
        --right;
        ++groups;
    }

    cout << groups << '\n';
    return 0;
}

