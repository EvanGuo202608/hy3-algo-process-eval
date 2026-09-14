#include <algorithm>
#include <climits>
#include <iostream>
using namespace std;

int main() {
    long long n;
    if (!(cin >> n)) return 0;

    long long ans = LLONG_MAX;
    for (int i = 0; i < 3; ++i) {
        long long count, price;
        cin >> count >> price;
        long long packages = (n + count - 1) / count;
        ans = min(ans, packages * price);
    }

    cout << ans << '\n';
    return 0;
}
