# Classic Algorithms

This repository contains clean and simple implementations of commonly taught algorithms from my university course named "Algorithms". Each algorithm includes a brief description and its time/space complexity into this README.

---

## Each algorithm is presented in its essential form, without input/output handling, and is meant to serve as a reference for academic and interview preparation purposes.

---
## 📦 Sorting Algorithms

### 🔹 Quick Sort
- **What it does**: Sorts an array in ascending order.
- **How it works**: Recursively selects a pivot, partitions elements into “less” and “greater” sub-arrays, and concatenates the sorted results.
- **Average Time Complexity**: O(n log n)
- **Worst-Case**: O(n²)
- **Space Complexity**: O(log n) (recursion stack)

### 🔹 Merge Sort
- **What it does**: Produces a sorted array while guaranteeing O(n log n) performance.
- **How it works**: Recursively divides the input in half until single-element lists remain, then merges those lists in sorted order.
- **Time Complexity**: O(n log n)
- **Space Complexity**: O(n)

### 🔹 Radix Sort
- **What it does**: Sorts integers (or fixed-length strings) without comparisons.
- **How it works**: Processes digits from least to most significant, grouping elements by digit value at each pass (typically with counting sort).
- **Time Complexity**: O(n k) (*k* = digit count)
- **Space Complexity**: O(n + k)

### 🔹 Heap Sort
- **What it does**: In-place comparison sort that always runs in O(n log n).
- **How it works**: Builds a binary heap, then repeatedly swaps the root with the last element and re-heapifies the reduced heap.
- **Time Complexity**: O(n log n)
- **Space Complexity**: O(1)

---

## 🌲 Graph Traversal

### 🔹 Depth-First Search (DFS)
- **What it does**: Visits every vertex reachable from a start node, exploring as deep as possible before backtracking.
- **How it works**: Uses recursion or an explicit stack to push unvisited neighbors, unwinding when no further moves are possible.
- **Time Complexity**: O(V + E)
- **Space Complexity**: O(V)

### 🔹 Breadth-First Search (BFS)
- **What it does**: Traverses a graph level by level and finds the shortest path in unweighted graphs.
- **How it works**: Uses a queue to visit all immediate neighbors before moving to the next depth layer.
- **Time Complexity**: O(V + E)
- **Space Complexity**: O(V)

---

## 🧠 Graph Algorithms

### 🔹 Dijkstra’s Algorithm
- **What it does**: Computes the shortest path from one source to every other vertex when all edge weights are non-negative.
- **How it works**: Repeatedly extracts the vertex with the smallest tentative distance from a min-heap and relaxes its outgoing edges.
- **Time Complexity**: O((V + E) log V)
- **Space Complexity**: O(V)

### 🔹 Bellman-Ford Algorithm
- **What it does**: Finds single-source shortest paths even with negative weights and detects negative cycles.
- **How it works**: Relaxes every edge V − 1 times; an extra pass checks for distance updates to reveal negative cycles.
- **Time Complexity**: O(V E)
- **Space Complexity**: O(V)

### 🔹 Floyd-Warshall Algorithm
- **What it does**: Produces shortest-path distances between every pair of vertices.
- **How it works**: Iteratively improves a distance matrix by considering each vertex as an intermediate point (dynamic programming).
- **Time Complexity**: O(V³)
- **Space Complexity**: O(V²)

### 🔹 Prim’s Algorithm
- **What it does**: Constructs a Minimum Spanning Tree (MST) for a connected, weighted graph.
- **How it works**: Starts from an arbitrary vertex and greedily grows the MST by adding the cheapest edge that connects a visited vertex to an unvisited one (min-heap for efficiency).
- **Time Complexity**: O((V + E) log V)
- **Space Complexity**: O(V)

### 🔹 Kruskal’s Algorithm
- **What it does**: Builds an MST by always choosing the globally lightest edge that doesn’t form a cycle.
- **How it works**: Sorts edges by weight and uses Union-Find to merge components while avoiding cycles.
- **Time Complexity**: O(E log E)
- **Space Complexity**: O(V)

---

## 🛠 How to Use

You can run any of these implementations individually. Each algorithm is in its own file and can be tested with example inputs.

---

## 💡 Contributing

Feel free to open issues or pull requests if you'd like to contribute more algorithms or improve the existing code.
