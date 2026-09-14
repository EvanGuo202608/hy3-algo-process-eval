#include <iostream>
#include <vector>
using namespace std;

int main() {
    int L, m;
    if (!(cin >> L >> m)) return 0;

    vector<int> removed(L + 1, 0);
    for (int i = 0; i < m; ++i) {
        int left, right;
        cin >> left >> right;
        for (int pos = left; pos <= right; ++pos) {
            removed[pos] = 1;
        }
    }

    int remaining = 0;
    for (int pos = 0; pos <= L; ++pos) {
        if (!removed[pos]) ++remaining;
    }
    cout << remaining << '\n';
    return 0;
}

