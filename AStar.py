import queue as Q


class AStar:
    def __init__(self, graph, root):
        self.graph = graph
        self.root = root
        self.visited = dict()
        self.queue = Q.PriorityQueue()
        self.counter = 0

    def run(self, target):
        """ YOUR CODE HERE """
        self.queue.put(self.root)
        match_found = False
        while not self.queue.empty():
            self.counter = self.counter + 1
            current_node = self.queue.get()
            self.visited[current_node.UID] = current_node
            depth = current_node.step
            if current_node.is_equal(target):
                match_found = True
                break

            children_nodes_list = self.graph.reveal_neighbors(current_node)
            for child_node in children_nodes_list:
                if self.visited.get(child_node.UID) is None:
                    priority_number = self.manhattan_distance(current_node, target) + current_node.step
                    self.queue.put(child_node, priority_number)

        # return 3 items
        # a: bool (match found or not)
        # b: int (counter)
        # c: int (depth)
        return match_found, self.counter, depth

    def manhattan_distance(self, node, end):
        arr = [0] * (self.graph.size + 1)
        brr = [0] * (self.graph.size + 1)
        for i in range(len(node.g_node)):
            for j in range(len(node.g_node[i])):
                arr[node.g_node[i][j]] = [i, j]

        for i in range(len(end.g_node)):
            for j in range(len(end.g_node[i])):
                brr[end.g_node[i][j]] = [i, j]
        dist = 0
        for i in range(1, len(arr)):
            dist += abs(arr[i][0] - brr[i][0]) + abs(arr[i][1] - brr[i][1])
        return dist
