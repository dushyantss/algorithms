# Python DSA Roadmap

## Plan

### Phase 1: Core linear structures and hashing

Build:

- `SinglyLinkedList`
- `DoublyLinkedList`
- `Stack`
- `Queue`
- `Deque`
- `HashMap`
- `HashSet`

Study:

- Open Data Structures
- CLRS hash table chapter for `HashMap`

Goal:

- Pointer manipulation
- Array vs. linked-list tradeoffs
- Collision handling
- Resize and rehash mechanics

Practice after this phase:

- Valid parentheses
- Implement queue using stacks / stack using queues
- LRU cache intuition
- Two sum
- First non-repeating character
- Sliding window basics

### Phase 2: Priority structures

Build:

- `BinaryHeap`
- `IndexedPriorityQueue`

Study:

- CLRS heap chapter
- William Fiset for indexed priority queue intuition

Goal:

- Heap invariants
- `sift_up` / `sift_down`
- `heapify`
- Key-priority updates

Practice:

- Kth largest / smallest
- Top k frequent
- Merge k sorted lists
- Task scheduler
- Running median
- Dijkstra prep

### Phase 3: Ordered trees

Build:

- `BST` with explicit duplicate policy
- `AVLTree`
- `RedBlackTree` or `Treap`

Study:

- Open Data Structures for `BST` and `AVLTree`
- CLRS for `RedBlackTree`
- cp-algorithms for `Treap`

Goal:

- Recursive tree manipulation
- Rotations
- Balance invariants
- Deletion edge cases
- Ordered operations

Practice:

- Validate BST
- Kth smallest in BST
- Inorder successor
- Tree diameter
- Lowest common ancestor
- Serialize / deserialize tree

Recommendation:

- Do `Treap` before `RedBlackTree` if you want smoother progress
- Do `RedBlackTree` if you want stronger textbook and systems familiarity

### Phase 4: Prefix and connectivity

Build:

- `Trie`
- `UnionFind`

Study:

- Open Data Structures and standard trie references
- cp-algorithms for DSU

Goal:

- Prefix indexing
- Path compression
- Union by size / rank

Practice:

- Word search / autocomplete style problems
- Replace words
- Number of islands
- Accounts merge
- Redundant connection
- Kruskal MST

### Phase 5: Range-query structures

Build:

- `FenwickTree`
- `SegmentTree`
- `LazySegmentTree`
- `SparseTable`

Study:

- cp-algorithms for all four

Goal:

- Prefix aggregation
- Point vs. range update tradeoffs
- Static vs. dynamic query structures
- Tree-on-array representations

Practice:

- Range sum query
- Range minimum query
- Mutable range queries
- Interval update problems
- Subtree query problems after `EulerTour`

### Phase 6: High-value advanced additions

Build:

- `SkipList`
- `OrderStatisticTree`
- `LRUCache`
- `MonotonicQueue`

Study:

- Open Data Structures for `SkipList`
- CLRS for `OrderStatisticTree`
- Standard editorials for `LRUCache` and `MonotonicQueue`

Goal:

- Probabilistic balancing
- Augmented trees
- Composition of simpler data structures
- Sliding window optimization

Practice:

- Sliding window maximum
- Kth smallest / median maintenance variants
- Cache design
- Rank / select problems

### Phase 7: Advanced string structures

Build:

- `SuffixArray`
- `AhoCorasick`

Study:

- cp-algorithms

Goal:

- Substring indexing
- LCP intuition
- Multi-pattern matching

Practice:

- Substring search
- Repeated substring problems
- Multi-word match problems

### Phase 8: Tree algorithm frameworks

Build:

- `EulerTour`
- `BinaryLifting`
- `HeavyLightDecomposition`

Study:

- cp-algorithms

Goal:

- Turn trees into arrays
- Subtree and path queries
- Ancestor jumping
- Combine tree logic with segment trees

Practice:

- LCA queries
- Kth ancestor
- Subtree sum / min / max
- Path sum / max queries

### Phase 9: Systems-oriented trees

Build only if you want systems and database depth:

- `BTree`
- `BPlusTree`

Study:

- CLRS for `BTree` basics
- CMU 15-445 for `BPlusTree` and page-level intuition

Goal:

- Disk-friendly branching
- Range scans
- Leaf linkage
- Systems design intuition

## Workflow

For every structure, use the same loop:

1. Define scope and duplicate / edge-case policy.
2. Define exact public methods.
3. Write tests in the same style as `tests/test_dynamic_array.py`.
4. Implement.
5. Practice 5-10 matching problems.
