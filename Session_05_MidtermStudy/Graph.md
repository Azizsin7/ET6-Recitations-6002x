## ❓ Graph Structures from Code

In each code snippet, examine how edges are added and identify the type of graph that results.  
**Possible graph types:**
- Tree
- Graph (undirected graph)
- Digraph (directed graph)
- Complete graph or clique
- Loop or connected chain of nodes

---

🔹 Problem 1
```python
for i in range(len(nodes)):
    x = random.choice(nodes)
    y = random.choice(nodes)
    addEdge(x, y)
```
<details> <summary>🔎 Answer & Explanation</summary>
✅ Answer: Digraph (directed graph)

Explanation: Edges are added in one direction only (from x to y), and random pairs are selected. This forms a directed graph (digraph), where connections aren’t necessarily mutual.

</details>

🔹 Problem 2
```python
for i in range(len(nodes)):
    x = random.choice(nodes)
    y = random.choice(nodes)
    addEdge(x, y)
    addEdge(y, x)
```
<details> <summary>🔎 Answer & Explanation</summary>
✅ Answer: Graph (undirected graph)

Explanation: For each random pair of nodes (x, y), two edges are added in both directions, making connections effectively undirected. So, this creates an undirected graph.

</details>

🔹 Problem 3
```python
for i in range(len(nodes)):
    w = random.choice(nodes)
    x = random.choice(nodes)
    y = random.choice(nodes)
    z = random.choice(nodes)
    addEdge(w, x)
    addEdge(x, y)
    addEdge(y, z)
    addEdge(z, w)
```

<details> <summary>🔎 Answer & Explanation</summary>
❌ Answer: Not a loop or connected chain of nodes

Correct Answer: Digraph (directed graph)

Explanation: This code adds multiple separate 4-node cycles randomly — not one large loop or chain connecting all nodes. Because the nodes are randomly selected each time, the graph consists of disconnected cycles, forming a directed graph (digraph).

</details>

 Problem 4

```python
for x in nodes:
    for y in nodes:
        addEdge(x, y)
        addEdge(y, x)
```

<details> <summary>🔎 Answer & Explanation</summary>
✅ Answer: Complete graph or clique

Explanation: This double loop connects every node to every other node in both directions. This forms a complete graph (clique), where all nodes are fully interconnected.

</details>

🔹 Problem 5
Which graph has the largest out-degree per node?

<details> <summary>🔎 Answer & Explanation</summary>
✅ Answer: Complete graph or clique

Explanation: In a complete graph, each node connects to every other node.
So, the out-degree (number of neighbors) is maximized for every node.

</details> 
