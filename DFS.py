class DFS:
    def __init__(self, graph, root):
        self.graph = graph
        self.visited = dict()
        self.stack = list()
        self.stack.append(root)
        self.counter = 0

    def run(self, target):
        """ YOUR CODE HERE """
        # pre-order DFS algorithm
        self.visited.clear()
        match_found = False
        depth = 0

        while len(self.stack) != 0:
            self.counter = self.counter + 1
            current_node = self.stack.pop(0)
            depth = current_node.step
            children_nodes_list = self.graph.reveal_neighbors(current_node)
            self.visited[current_node.UID] = current_node

            if current_node.is_equal(target):
                match_found = True
                break

            for child_node in children_nodes_list:
                if self.visited.get(child_node.UID) is None:
                    self.stack.insert(0, child_node)

        # return 3 items
        # a: bool (match found or not)
        # b: int (counter)
        # c: int (depth)
        return match_found, self.counter, depth
