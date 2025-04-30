import heapq
import graphviz


class Graph:
    """
    带权有向图类，使用字符串标识节点，内部使用整数ID，维护前后继邻接表。
    """

    def __init__(self):
        """
        初始化图的成员变量。
        """
        # 用于 int 到 str 的映射
        self._int_to_str: dict[int, str] = {}
        # 用于 str 到 int 的映射
        self._str_to_int: dict[str, int] = {}
        # 用于生成新的节点ID
        self._next_node_id: int = 0

        # 邻接表：successor_adj_set[i] 存储节点 i 的后继节点及其边的权重，格式为 {(后继节点ID, 权重), ...}
        self._successor_adj_set: list[dict[int, int]] = []
        # 邻接表：predecessor_adj_set[i] 存储节点 i 的前驱节点及其边的权重，格式为 {(前驱节点ID), ...}
        self._predecessor_adj_set: list[set[int]] = []

    def __str__(self) -> str:
        """返回图的字符串表示，包含节点和边的信息。"""
        result = "Graph:\n"
        for node_id, node_str in self._int_to_str.items():
            successors = [
                f"{self._get_str(neighbor_id)}({weight})"
                for neighbor_id, weight in self._successor_adj_set[
                    node_id
                ].items()
            ]
            result += f"  {node_str} -> [{', '.join(successors)}]\n"
        return result

    def _get_id(self, node_str: str) -> int:
        """获取节点字符串对应的内部ID，如果不存在则抛出异常。"""
        if node_str not in self._str_to_int:
            raise ValueError(f"Node '{node_str}' does not exist in the graph.")
        return self._str_to_int[node_str]

    def _get_id_or_none(self, node_str: str) -> int | None:
        """获取节点字符串对应的内部ID，如果不存在则返回 None。"""
        return self._str_to_int.get(node_str)

    def _get_str(self, node_id: int) -> str:
        """获取节点ID对应的字符串，如果不存在则抛出异常（理论上不会发生）。"""
        if node_id not in self._int_to_str:
            # This should ideally not happen if using valid IDs from the graph
            raise IndexError(
                f"Internal error: Node ID {node_id} does not exist."
            )
        return self._int_to_str[node_id]

    def clear(self):
        """清空图的所有节点和边。"""
        self._int_to_str.clear()
        self._str_to_int.clear()
        self._next_node_id = 0
        self._successor_adj_set.clear()
        self._predecessor_adj_set.clear()

    def addNode(self, node_str: str):
        """
        添加节点。
        若节点已存在，则抛出 ValueError。
        """
        if node_str in self._str_to_int:
            raise ValueError(f"Node '{node_str}' already exists.")

        node_id = self._next_node_id
        self._str_to_int[node_str] = node_id
        self._int_to_str[node_id] = node_str
        self._next_node_id += 1

        # 为新节点扩展邻接表
        self._successor_adj_set.append({})
        self._predecessor_adj_set.append(set())

    def hasNode(self, node_str: str) -> bool:
        """
        检查图中是否有str标识的节点。
        """
        return node_str in self._str_to_int

    def addEdge(self, from_str: str, to_str: str, weight: int):
        """
        添加有向边。
        如果起始或终止节点不存在，则会自动创建。
        要求权重为非负整数。
        """
        if weight < 0:
            raise ValueError("Edge weight must be non-negative.")

        # 如果节点不存在，先创建
        if not self.hasNode(from_str):
            self.addNode(from_str)
        if not self.hasNode(to_str):
            self.addNode(to_str)

        from_id = self._get_id(from_str)
        to_id = self._get_id(to_str)

        # 添加边到后继邻接表
        self._successor_adj_set[from_id][to_id] = weight

        # 添加边到前驱邻接表
        self._predecessor_adj_set[to_id].add(from_id)

    def hasEdge(self, from_str: str, to_str: str) -> bool:
        """
        检查是否存在从 from_str 到 to_str 的有向边。
        如果起始或终止节点不存在，返回 False。
        """
        from_id = self._get_id_or_none(from_str)
        to_id = self._get_id_or_none(to_str)

        if from_id is None or to_id is None:
            return False

        # 检查邻接表中是否存在该边
        return from_id in self._predecessor_adj_set[to_id]

    def increaseEdgeWeight(self, from_str: str, to_str: str, weight: int):
        """
        增加有向边的权重。
        如果起始或终止节点不存在，则会自动创建。
        要求权重为非负整数。
        """
        if weight < 0:
            raise ValueError("Edge weight must be non-negative.")

        # 如果节点不存在，先创建
        if not self.hasNode(from_str):
            self.addNode(from_str)
        if not self.hasNode(to_str):
            self.addNode(to_str)

        from_id = self._get_id(from_str)
        to_id = self._get_id(to_str)

        # 查找当前权重
        current_weight = self._successor_adj_set[from_id].get(to_id, 0)
        if current_weight == 0:
            # 如果边不存在，添加新边
            self._successor_adj_set[from_id][to_id] = weight
            self._predecessor_adj_set[to_id].add(from_id)
        else:
            # 如果边存在，增加权重
            self._successor_adj_set[from_id][to_id] = current_weight + weight

    def getSuccessor(self, node_str: str) -> list[str]:
        """
        获取节点的后继节点列表。
        如果节点不存在，返回空列表。
        """
        node_id = self._get_id_or_none(node_str)
        if node_id is None:
            return []

        return [
            self._get_str(successor_id)
            for successor_id, _ in self._successor_adj_set[node_id].items()
        ]

    def getPredecessor(self, node_str: str) -> list[str]:
        """
        获取节点的前驱节点列表。
        如果节点不存在，返回空列表。
        """
        node_id = self._get_id_or_none(node_str)
        if node_id is None:
            return []

        return [
            self._get_str(predecessor_id)
            for predecessor_id in self._predecessor_adj_set[node_id]
        ]

    def getBridge(self, node1_str: str, node2_str: str) -> list[str]:
        """
        计算两个节点之间的桥接节点列表 (node1 -> node3 -> node2)。
        如果节点不存在，返回空列表。
        """
        node1_id = self._get_id_or_none(node1_str)
        node2_id = self._get_id_or_none(node2_str)

        if node1_id is None or node2_id is None:
            return []

        # 获取 node1 的后继节点ID集合
        successors_of_node1_ids = set(self._successor_adj_set[node1_id].keys())

        # 获取 node2 的前驱节点ID集合
        predecessors_of_node2_ids = self._predecessor_adj_set[node2_id]

        # 桥接节点ID集合是两者的交集
        bridge_ids = successors_of_node1_ids.intersection(
            predecessors_of_node2_ids
        )

        # 将桥接节点ID转换回字符串名称
        bridge_nodes = [self._get_str(bridge_id) for bridge_id in bridge_ids]

        # 可选：按字母顺序排序桥接节点名称
        bridge_nodes.sort()

        return bridge_nodes

    def getShortestPath(
        self,
        start_str: str,
        end_str: str | None = None,
        showMultiPath: bool = False,
    ) -> list[tuple[int, list[str]]]:
        """
        使用 Dijkstra 算法计算最短路径。

        Args:
            start_str: 起始节点字符串。
            end_str: 终止节点字符串，如果为 None，则计算从起始节点到所有其他节点的最短路径。
            showMultiPath: 如果为 True，当存在多条最短路径时，返回所有路径，否则只返回一条。

        Returns:
            一个列表，其中包含最短路径列表。
            如果找不到路径（当 end_str 不为 None 时），返回空列表。
            如果 end_str 为 None，返回从起始节点到所有可达节点的路径列表。
        """
        start_id: int | None = self._get_id_or_none(start_str)
        if start_id is None:
            # 起始节点必须存在
            return []  # 或者抛出 ValueError

        end_id: int | None = (
            self._get_id_or_none(end_str) if end_str is not None else None
        )
        if end_id is not None and end_id == start_id:
            return [(0, [start_str])]  # 起点终点相同，路径就是起点本身

        num_nodes: int = self._next_node_id
        if num_nodes == 0:
            return []

        # Dijkstra 初始化
        distances: dict[int, float] = {
            i: float("inf") for i in range(num_nodes)
        }
        distances[start_id] = 0

        # predecessors[v] 存储到达节点 v 的最短路径中，v 的所有前一个节点ID的列表
        predecessors: dict[int, list] = {i: [] for i in range(num_nodes)}

        # 优先队列，存储 (距离, 节点ID)
        priority_queue: list[tuple[int, int]] = [(0, start_id)]

        while priority_queue:
            current_distance, u_id = heapq.heappop(priority_queue)

            # 如果已处理过且距离更短，跳过
            if current_distance > distances[u_id]:
                continue

            # 遍历当前节点 u 的后继节点
            for v_id, weight in self._successor_adj_set[u_id].items():
                new_distance = distances[u_id] + weight

                if new_distance < distances[v_id]:
                    distances[v_id] = new_distance
                    predecessors[v_id] = [
                        u_id
                    ]  # 找到更短路径，清空旧前驱，记录新前驱
                    heapq.heappush(priority_queue, (new_distance, v_id))
                elif new_distance == distances[v_id] and showMultiPath:
                    # 找到相同距离的路径，如果允许展示多条路径，添加前驱
                    if u_id not in predecessors[v_id]:  # 避免重复添加同一个前驱
                        predecessors[v_id].append(u_id)

        # 路径重建
        def reconstruct_paths(target_id: int) -> list[list[int]]:
            """递归重建从起始节点到目标节点的所有最短路径（以ID列表表示）。"""
            if target_id == start_id:
                return [[start_id]]  # 到达起始节点，路径结束

            if not predecessors[target_id]:
                return []  # 无法回溯到起始节点，没有路径

            paths: list = []
            # 遍历所有可能的前驱节点
            for prev_id in predecessors[target_id]:
                # 递归获取到前驱节点的所有最短路径
                paths_to_prev: list[list[int]] = reconstruct_paths(prev_id)
                # 将当前节点添加到这些路径的末尾
                for path in paths_to_prev:
                    paths.append(path + [target_id])

                # 如果不展示多条路径，找到一条就停止回溯
                if not showMultiPath and paths_to_prev:
                    break  # 只回溯第一个前驱找到的路径

            return paths

        final_paths = []
        if end_id is not None:
            # 计算到特定终点的最短路径
            if distances[end_id] != float("inf"):
                id_paths: list[list[int]] = reconstruct_paths(end_id)
                # 将节点ID路径转换为字符串路径
                final_paths: list[tuple[int, list[str]]] = [
                    (
                        int(distances[end_id]),
                        [self._get_str(node_id) for node_id in path],
                    )
                    for path in id_paths
                ]
        else:
            # 计算到所有可达节点的最短路径
            for target_id in range(num_nodes):
                if target_id != start_id and distances[target_id] != float(
                    "inf"
                ):
                    id_paths = reconstruct_paths(target_id)
                    # 将节点ID路径转换为字符串路径
                    str_paths: list[tuple[int, list[str]]] = [
                        (
                            int(distances[target_id]),
                            [self._get_str(node_id) for node_id in path],
                        )
                        for path in id_paths
                    ]
                    final_paths.extend(
                        str_paths
                    )  # 将到每个目标的路径添加到总列表中

        return final_paths

    def getPageRank(
        self,
        d: float = 0.85,
        iterations: int = 100,
        initialization_strategy: str = "uniform",
        keyword_boosts: (
            dict[str, float] | None
        ) = None,  # Keep this for potential future use or manual override
    ) -> dict[str, float]:
        """
        使用 PageRank 算法计算每个节点的 PageRank 值。

        Args:
            d: 阻尼因子 (damping factor)，介于 0 到 1 之间，通常取 0.85。
            iterations: 迭代次数，用于计算 PageRank 值的收敛。
            initialization_strategy: 初始 PageRank 分配策略。可选值:
                'uniform': 标准均匀分配 (默认)。
                'in_degree': 根据节点的入度进行分配。入度越高的节点初始 PR 越高。
                'sum_incoming_weights': 根据节点的入边权重总和进行分配。总和越高的节点初始 PR 越高。
                'keyword_boosts': 使用 keyword_boosts 参数指定的权重进行分配。
            keyword_boosts: 仅当 initialization_strategy 为 'keyword_boosts' 时有效。
                            一个字典，用于指定重要关键词及其初始 PageRank 权重因子。
                            键是关键词字符串，值是权重因子（浮点数，应大于0）。
                            未指定的节点权重因子为 1.0。

        Returns:
            一个字典，键为节点字符串，值为对应的 PageRank 值。
            如果图为空，返回空字典。
        """
        num_nodes = self._next_node_id
        if num_nodes == 0:
            return {}

        # --- 初始值策略逻辑开始 ---
        initial_scores: dict[int, float] = {}

        if initialization_strategy == "uniform":
            # 标准均匀初始化
            initial_scores = {
                i: 1.0 for i in range(num_nodes)
            }  # Use 1.0 as raw score, will normalize later

        elif initialization_strategy == "in_degree":
            # 根据入度初始化
            initial_scores = {
                i: float(len(self._predecessor_adj_set[i]))
                for i in range(num_nodes)
            }

        elif initialization_strategy == "sum_incoming_weights":
            # 根据入边权重总和初始化
            initial_scores = {i: 0.0 for i in range(num_nodes)}
            # Iterate through all edges to calculate incoming weights sum for each node
            for from_id in range(num_nodes):
                for to_id, weight in self._successor_adj_set[from_id].items():
                    initial_scores[to_id] += weight
            # If a node has no incoming edges, its score remains 0.0

        elif initialization_strategy == "keyword_boosts":
            if (
                not keyword_boosts
                or not isinstance(keyword_boosts, dict)
                or len(keyword_boosts) == 0
            ):
                print(
                    "Warning: 'keyword_boosts' strategy selected but keyword_boosts dictionary is empty or invalid. Falling back to 'uniform'."
                )
                # Fallback to uniform if keyword_boosts is not provided or empty
                initial_scores = {i: 1.0 for i in range(num_nodes)}
            else:
                # Use keyword weights for initialization
                for node_id in range(num_nodes):
                    node_str = self._get_str(node_id)
                    # Get boost factor, default to 1.0 if not a keyword or boost <= 0
                    boost_factor = keyword_boosts.get(node_str, 1.0)
                    if boost_factor <= 0:
                        boost_factor = 1.0
                    initial_scores[node_id] = boost_factor

        else:
            raise ValueError(
                f"Unknown initialization strategy: {initialization_strategy}. "
                "Available strategies: 'uniform', 'in_degree', 'sum_incoming_weights', 'keyword_boosts'"
            )

        # Normalize initial scores so they sum to 1.0
        total_initial_score = sum(initial_scores.values())

        # Handle cases where total initial score is zero (e.g., graph with nodes but no edges)
        if total_initial_score == 0:
            print(
                f"Warning: Total initial score is 0 with strategy '{initialization_strategy}'. Falling back to uniform initialization."
            )
            pr = {i: 1.0 / num_nodes for i in range(num_nodes)}
        else:
            pr = {
                node_id: score / total_initial_score
                for node_id, score in initial_scores.items()
            }
        # --- 初始值策略逻辑结束 ---

        # 计算每个节点的出度
        out_degree = {
            i: len(self._successor_adj_set[i]) for i in range(num_nodes)
        }
        # Avoid division by zero for nodes with no outgoing links in the loop
        # Dangling nodes are handled separately

        # 迭代计算 PageRank 值
        for _ in range(iterations):
            new_pr = {}
            # 处理没有出链的节点（悬挂节点）的 PageRank 分布
            # PageRank of dangling nodes is distributed equally among all nodes
            dangling_pr_sum = sum(
                pr[i] for i in range(num_nodes) if out_degree[i] == 0
            )

            for j_id in range(num_nodes):
                # PageRank 公式的随机跳转部分
                # The "random surfer" jumps to a random page (equally likely)
                rank_sum = (1 - d) / num_nodes

                # PageRank 公式的基于链接的传递部分
                # Sum of PR from incoming links, divided by their out-degree
                sum_of_incoming_pr = 0.0
                for i_id in self._predecessor_adj_set[j_id]:
                    # Only consider incoming links from nodes that have outgoing links
                    # Dangling nodes' PR is handled via dangling_pr_sum
                    if out_degree[i_id] > 0:
                        sum_of_incoming_pr += pr[i_id] / out_degree[i_id]

                # 将悬挂节点的 PR 平均分配到所有节点上
                rank_sum += d * (
                    sum_of_incoming_pr + dangling_pr_sum / num_nodes
                )

                new_pr[j_id] = rank_sum

            pr = new_pr  # 更新 PageRank 值

        # 将节点ID转换回字符串名称
        pr_str = {
            self._get_str(node_id): score for node_id, score in pr.items()
        }

        return pr_str

    def toDigraph(
        self, highlightNodes: list[str] = None, highlightPath: list[str] = None
    ) -> graphviz.Digraph:
        """
        将图转换为 Graphviz Diagraph 对象。
        可选项 highLightNodes 和 highLightPath 用于在可视化图中高亮显示特定节点和路径。

        Args:
            highlightNodes: 一个列表，包含需要高亮显示的节点字符串。这些节点在图中将具有天蓝色背景。
            highlightPath: 一个列表，包含需要高亮显示的路径上的节点字符串序列 (e.g., ['A', 'B', 'C'])。
                           这条路径上的边将用加粗红色凸显。

        Returns:
            一个 graphviz.Digraph 对象，表示图的可视化表示。

        Raises:
            ValueError: 如果图中的节点数量超过 50，认为图过大不适合可视化。
        """

        # 当节点数过大时，抛出异常
        if len(self._str_to_int) > 50:
            raise ValueError(
                "节点数过多（超过 50），不适合可视化。请缩小图的规模。"
            )

        # 创建一个有向图对象
        dot = graphviz.Digraph()

        # 设置图的全局属性
        dot.attr(rankdir="LR", size="8,5")

        # 构建需要高亮显示的节点集合，方便快速查找
        highlightNodes_set = set(highlightNodes) if highlightNodes else set()

        # 添加所有节点到 graphviz 对象
        for node_str, node_id in self._str_to_int.items():
            node_attributes: dict[str, str] = {
                "label": node_str
            }  # 节点标签显示字符串名称

            if node_str in highlightNodes_set:
                # 如果节点在待高亮列表中，设置填充样式和颜色
                node_attributes["style"] = "filled"
                node_attributes["fillcolor"] = "lightblue"

            # 添加节点
            dot.node(node_str, **node_attributes)  # 使用字典解包应用属性

        # 构建需要高亮显示的边集合 (由路径上的相邻节点对组成)，方便快速查找
        # 集合中的元素是 (起始节点字符串, 终止节点字符串)
        highlight_edges_set = set()
        if highlightPath and len(highlightPath) >= 2:
            for i in range(len(highlightPath) - 1):
                u_str = highlightPath[i]
                v_str = highlightPath[i + 1]
                # 将路径上的相邻节点对作为需要高亮的边添加到集合中
                highlight_edges_set.add((u_str, v_str))

        # 添加所有边到 graphviz 对象
        # 遍历所有节点及其后继，添加边和权重
        for from_str, from_id in self._str_to_int.items():
            # _successor_adj_list[from_id] 存储的是 [(to_id, weight), ...]
            for to_id, weight in self._successor_adj_set[from_id].items():
                to_str = self._get_str(to_id)

                edge_attributes: dict[str, str] = {
                    "label": str(weight)
                }  # 边标签显示权重

                # 检查这条边 (from_str -> to_str) 是否在需要高亮的边集合中
                if (from_str, to_str) in highlight_edges_set:
                    # 如果需要高亮，设置边颜色和粗细
                    edge_attributes["color"] = "red"
                    edge_attributes["penwidth"] = "2.0"  # penwidth 控制线的粗细

                # 添加边
                dot.edge(
                    from_str, to_str, **edge_attributes
                )  # 使用字典解包应用属性

        return dot


# 示例用法：
if __name__ == "__main__":
    graph = Graph()

    # 添加节点 (也可以通过 addEdge 隐式添加)
    graph.addNode("A")
    graph.addNode("B")
    graph.addNode("C")
    graph.addNode("D")
    graph.addNode("E")

    # 添加边 (如果节点不存在会自动创建)
    graph.addEdge("A", "B", 1)
    graph.addEdge("A", "C", 2)
    graph.addEdge("B", "D", 3)
    graph.addEdge("C", "D", 1)
    graph.addEdge("C", "E", 5)
    graph.addEdge("D", "E", 2)
    graph.addEdge("E", "B", 1)  # 形成一个循环 E -> B
    graph.addEdge("A", "E", 5)

    print("Nodes:", list(graph._str_to_int.keys()))
    print("Has Node 'A'?", graph.hasNode("A"))
    print("Has Node 'Z'?", graph.hasNode("Z"))

    print("\nSuccessors of A:", graph.getSuccessor("A"))
    print("Predecessors of D:", graph.getPredecessor("D"))
    print("Successors of Z:", graph.getSuccessor("Z"))  # 不存在的节点

    print("\nBridges between A and D:", graph.getBridge("A", "D"))  # C 是桥接点
    print("Bridges between A and E:", graph.getBridge("A", "E"))

    print(
        "Bridges A -> B:", graph.getBridge("A", "B")
    )  # Expected: [] (direct edge, no intermediate node)

    print("\nShortest path from A to E:")
    paths_A_to_E = graph.getShortestPath("A", "E")
    print(
        paths_A_to_E
    )  # Should be ['A', 'C', 'E'] with weight 2+5=7 vs A->B->D->E with 1+3+2=6. A->C->D->E with 2+1+2=5. Shortest is A->C->D->E

    print("\nShortest path from A to E (Show Multi Path):")
    paths_A_to_E_multi = graph.getShortestPath("A", "E", showMultiPath=True)
    print(
        paths_A_to_E_multi
    )  # Should show A->C->D->E (weight 5) if it's the only shortest. If another path also has weight 5, show it too.

    print("\nShortest path from A to all others:")
    paths_A_to_all = graph.getShortestPath("A", None, showMultiPath=True)
    # Sort paths by their end node for easier reading
    paths_A_to_all.sort(key=lambda p: p[-1] if p else "")
    print(paths_A_to_all)

    print("\nPageRank calculation:")
    pagerank_scores = graph.getPageRank()
    print(pagerank_scores)

    # Example with a node having no outgoing links (dangling node)
    graph_pr_dangling = Graph()
    graph_pr_dangling.addNode("A")
    graph_pr_dangling.addNode("B")
    graph_pr_dangling.addNode("C")
    graph_pr_dangling.addEdge("A", "B", 1)
    graph_pr_dangling.addEdge("B", "C", 1)
    # C is a dangling node

    print("\nPageRank with dangling node:")
    pagerank_scores_dangling = graph_pr_dangling.getPageRank()
    print(pagerank_scores_dangling)
