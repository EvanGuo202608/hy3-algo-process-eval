#include <iostream>
#include <vector>
using namespace std;

struct SegmentTree {
    int n;
    vector<long long> sum;
    vector<long long> lazy;

    explicit SegmentTree(const vector<long long> &a) {
        n = static_cast<int>(a.size()) - 1;
        sum.assign(4 * n + 4, 0);
        lazy.assign(4 * n + 4, 0);
        build(1, 1, n, a);
    }

    void build(int node, int left, int right, const vector<long long> &a) {
        if (left == right) {
            sum[node] = a[left];
            return;
        }
        int mid = (left + right) / 2;
        build(node * 2, left, mid, a);
        build(node * 2 + 1, mid + 1, right, a);
        sum[node] = sum[node * 2] + sum[node * 2 + 1];
    }

    void apply(int node, int left, int right, long long delta) {
        sum[node] += delta * (right - left + 1LL);
        lazy[node] += delta;
    }

    void push(int node, int left, int right) {
        if (lazy[node] == 0 || left == right) return;
        int mid = (left + right) / 2;
        apply(node * 2, left, mid, lazy[node]);
        apply(node * 2 + 1, mid + 1, right, lazy[node]);
        lazy[node] = 0;
    }

    void add(int node, int left, int right, int query_left, int query_right, long long delta) {
        if (query_left <= left && right <= query_right) {
            apply(node, left, right, delta);
            return;
        }
        push(node, left, right);
        int mid = (left + right) / 2;
        if (query_left <= mid) add(node * 2, left, mid, query_left, query_right, delta);
        if (mid < query_right) add(node * 2 + 1, mid + 1, right, query_left, query_right, delta);
        sum[node] = sum[node * 2] + sum[node * 2 + 1];
    }

    long long query(int node, int left, int right, int query_left, int query_right) {
        if (query_left <= left && right <= query_right) return sum[node];
        push(node, left, right);
        int mid = (left + right) / 2;
        long long answer = 0;
        if (query_left <= mid) answer += query(node * 2, left, mid, query_left, query_right);
        if (mid < query_right) answer += query(node * 2 + 1, mid + 1, right, query_left, query_right);
        return answer;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, q;
    if (!(cin >> n >> q)) return 0;
    vector<long long> a(n + 1);
    for (int i = 1; i <= n; ++i) cin >> a[i];

    SegmentTree tree(a);
    while (q--) {
        int type, l, r;
        cin >> type >> l >> r;
        if (type == 1) {
            long long x;
            cin >> x;
            tree.add(1, 1, n, l, r, x);
        } else {
            cout << tree.query(1, 1, n, l, r) << '\n';
        }
    }
    return 0;
}

