#include <algorithm>
#include <iostream>
#include <numeric>
#include <vector>
using namespace std;

struct Edge {
    int u;
    int v;
    long long w;
};

struct DSU {
    vector<int> parent;
    vector<int> size;

    explicit DSU(int n) : parent(n + 1), size(n + 1, 1) {
        iota(parent.begin(), parent.end(), 0);
    }

    int find(int x) {
        if (parent[x] == x) return x;
        parent[x] = find(parent[x]);
        return parent[x];
    }

    bool unite(int a, int b) {
        a = find(a);
        b = find(b);
        if (a == b) return false;
        if (size[a] < size[b]) swap(a, b);
        parent[b] = a;
        size[a] += size[b];
        return true;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;
    vector<Edge> edges(m);
    for (auto &edge : edges) {
        cin >> edge.u >> edge.v >> edge.w;
    }

    sort(edges.begin(), edges.end(), [](const Edge &a, const Edge &b) {
        return a.w < b.w;
    });

    DSU dsu(n);
    long long total = 0;
    int used = 0;
    for (const auto &edge : edges) {
        if (dsu.unite(edge.u, edge.v)) {
            total += edge.w;
            ++used;
            if (used == n - 1) break;
        }
    }

    if (used == n - 1) {
        cout << total << '\n';
    } else {
        cout << "orz\n";
    }
    return 0;
}

