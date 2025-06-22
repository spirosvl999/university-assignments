# Classic Algorithms

This repository contains clean and simple implementations of commonly taught algorithms from my university course named "Algorithms". Each algorithm includes a brief description and its time/space complexity into this README.

---

## 📦 Sorting Algorithms

### 🔹 Quick Sort
- **Description**: Divide-and-conquer algorithm. Picks a pivot and partitions the array.
- **Average Time Complexity**: O(n log n)
- **Worst Case**: O(n²) (when the smallest or largest element is always picked)
- **Space Complexity**: O(log n) (in-place, due to recursion stack)

### 🔹 Merge Sort
- **Description**: Divide-and-conquer, divides the array and merges sorted halves.
- **Time Complexity**: O(n log n)
- **Space Complexity**: O(n)

### 🔹 Radix Sort
- **Description**: Non-comparative sorting, sorts by individual digit position.
- **Time Complexity**: O(nk), where *k* is the number of digits
- **Space Complexity**: O(n + k)

### 🔹 Heap Sort
- **Description**: Uses a binary heap to sort the array.
- **Time Complexity**: O(n log n)
- **Space Complexity**: O(1) (in-place)

---

## 🌲 Graph Traversal

### 🔹 Depth-First Search (DFS)
- **Description**: Explores as far as possible along each branch before backtracking.
- **Time Complexity**: O(V + E)
- **Space Complexity**: O(V) (due to recursion or stack)

### 🔹 Breadth-First Search (BFS)
- **Description**: Explores all neighbors at the current depth before going deeper.
- **Time Complexity**: O(V + E)
- **Space Complexity**: O(V) (due to queue)

---

## 🧠 Graph Algorithms

### 🔹 Dijkstra's Algorithm
- **Description**: Finds the shortest paths from a single source to all nodes (non-negative weights).
- **Time Complexity**: O((V + E) log V) with min-heap
- **Space Complexity**: O(V)

### 🔹 Bellman-Ford Algorithm
- **Description**: Finds shortest paths, handles negative weights.
- **Time Complexity**: O(VE)
- **Space Complexity**: O(V)

### 🔹 Floyd-Warshall Algorithm
- **Description**: All-pairs shortest path algorithm using dynamic programming.
- **Time Complexity**: O(V³)
- **Space Complexity**: O(V²)

### 🔹 Prim's Algorithm
- **Description**: Finds a Minimum Spanning Tree (MST) using a greedy approach.
- **Time Complexity**: O((V + E) log V) with min-heap
- **Space Complexity**: O(V)

### 🔹 Kruskal's Algorithm
- **Description**: Builds an MST by sorting edges and using Union-Find.
- **Time Complexity**: O(E log E)
- **Space Complexity**: O(V)

---

## 🛠 How to Use

You can run any of these implementations individually. Each algorithm is in its own file and can be tested with example inputs.

---

## 💡 Contributing

Feel free to open issues or pull requests if you'd like to contribute more algorithms or improve the existing code.
