[TOC]



### Dijkstra 算法的概念：

**Dijkstra 算法**是用来解决“最短路径问题”的一种算法。假设我们有一个图，其中每个节点之间有一条边，每条边都有一个权重（或者说长度），Dijkstra 算法可以帮我们找到从一个起始点到其他所有点的最短路径。

#### 算法基本步骤：

1. **初始化**：
   - 为图中的每个节点分配一个“距离”，初始时都设置为无穷大（表示暂时不知道该节点到起始点的距离）。
   - 然后把起始点的距离设为0，因为从起始点到自己是零。
2. **选择最小距离的节点**：
   - 选择当前距离最小的那个节点，开始更新它的相邻节点的距离。
3. **更新相邻节点的距离**：
   - 对于选中的节点，检查它的每个邻居，看看从这个节点到邻居的距离是否比原来记录的距离小。如果是，就更新邻居的距离。
4. **重复步骤 2 和 3**：
   - 直到所有节点的最短路径都被找到。

### 举个简单的例子：

假设你有一个图，节点和边的权重如下：

```
A --(1)--> B --(3)--> C
|         ^
(4)       |
v         |
D ---(2)--+
```

- 从 A 到 B 的权重是 1
- 从 B 到 C 的权重是 3
- 从 A 到 D 的权重是 4
- 从 D 到 B 的权重是 2

**目标**：找到从 A 到所有其他节点的最短路径。

### Dijkstra 算法的具体操作：

1. **初始化**：设定每个节点的距离为无穷大，除了起点 A，A 的距离设为 0。

   - A: 0
   - B: ∞
   - C: ∞
   - D: ∞

2. **选择 A（距离最小）**，更新它的邻居 B 和 D：

   - A 到 B 的距离是 1，更新 B 的距离为 1。
   - A 到 D 的距离是 4，更新 D 的距离为 4。

   现在的距离表：

   - A: 0
   - B: 1
   - C: ∞
   - D: 4

3. **选择 B（距离最小）**，更新它的邻居 C：

   - B 到 C 的距离是 3，B 的距离是 1，所以 A 到 C 的最短路径是 1 + 3 = 4，更新 C 的距离为 4。

   现在的距离表：

   - A: 0
   - B: 1
   - C: 4
   - D: 4

4. **选择 D（优先队列，D比C排在前面）**，D的邻居B已经被选择，不再更新。

   现在的距离表：

   - A: 0
   - B: 1
   - C: 4
   - D: 4

5. **选择 C**，但 C 没有未访问的邻居，因此结束。

最终的最短路径结果是：

- 从 A 到 A 的最短路径是 0
- 从 A 到 B 的最短路径是 1
- 从 A 到 C 的最短路径是 4
- 从 A 到 D 的最短路径是 4



另外一个例子：[一文彻底搞懂Dijkstra算法（迪杰斯特拉算法）](https://zhuanlan.zhihu.com/p/788846492)

### 优先队列实现实现：

```python
import heapq

def dijkstra(graph, start):
    # 创建一个字典来记录每个节点到起点的最短距离，初始值为无穷大
    distances = {node: float('inf') for node in graph}
    distances[start] = 0  # 起点到自己的距离是0
    
    # 使用优先队列来存储每个节点和其距离
    pq = [(0, start)]  # 起点的距离是0

    while pq:
        current_distance, current_node = heapq.heappop(pq)  # 取出距离最小的节点
        
        # 如果这个节点的最短路径已经被找到，就跳过
        if current_distance > distances[current_node]:
            continue
        
        # 更新相邻节点的距离
        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight  # 当前节点到相邻节点的路径长度
            
            # 如果发现更短的路径，就更新相邻节点的最短路径
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))  # 将更新后的节点加入队列
    
    return distances

# 示例图：字典表示邻接表，键是节点，值是相邻节点和边的权重
graph = {
    'A': [('B', 1), ('D', 4)],
    'B': [('A', 1), ('C', 3)],
    'C': [('B', 3)],
    'D': [('A', 4), ('B', 2)]
}

start_node = 'A'
shortest_paths = dijkstra(graph, start_node)

print(shortest_paths)
# {'A': 0, 'B': 1, 'C': 4, 'D': 4}
```

### 非优先队列实现

```python
def dijkstra(graph, start):
    # 创建一个字典来记录每个节点到起点的最短距离，初始值为无穷大
    distances = {node: float('inf') for node in graph}
    distances[start] = 0  # 起点到自己的距离是0
    
    # 创建一个集合来记录所有未访问的节点
    unvisited_nodes = list(graph.keys())
    
    while unvisited_nodes:
        # 从未访问的节点中选择一个距离最小的节点
        min_node = None
        for node in unvisited_nodes:
            if min_node is None:
                min_node = node
            elif distances[node] < distances[min_node]:
                min_node = node
        
        # 更新 min_node 的相邻节点的距离
        for neighbor, weight in graph[min_node]:
            new_distance = distances[min_node] + weight
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
        
        # 将选中的节点从未访问的节点中移除
        unvisited_nodes.remove(min_node)
    
    return distances

# 示例图：字典表示邻接表，键是节点，值是相邻节点和边的权重
graph = {
    'A': [('B', 1), ('D', 4)],
    'B': [('A', 1), ('C', 3)],
    'C': [('B', 3)],
    'D': [('A', 4), ('B', 2)]
}

start_node = 'A'
shortest_paths = dijkstra(graph, start_node)

print(shortest_paths)

```



### 总结：

- Dijkstra 算法通过逐步选择最短路径的节点，更新相邻节点的最短距离，最终得到从起点到所有节点的最短路径。
- 在实际应用中，这个算法非常适用于计算地图、网络中最短路径等问题。