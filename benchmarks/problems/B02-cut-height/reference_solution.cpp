#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;

static bool feasible(const vector<long long>& heights, long long cut, long long need) {
    long long total = 0;
    for (long long h : heights) {
        if (h > cut) total += h - cut;
        if (total >= need) return true;
    }
    return total >= need;
}

int main() {
    int n;
    long long need;
    if (!(cin >> n >> need)) return 0;
    vector<long long> heights(n);
    long long high = 0;
    for (int i = 0; i < n; ++i) {
        cin >> heights[i];
        high = max(high, heights[i]);
    }

    long long low = 0;
    long long ans = 0;
    while (low <= high) {
        long long mid = low + (high - low) / 2;
        if (feasible(heights, mid, need)) {
            ans = mid;
            low = mid + 1;
        } else {
            high = mid - 1;
        }
    }

    cout << ans << '\n';
    return 0;
}

