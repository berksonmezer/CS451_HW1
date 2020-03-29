class DFS:
    def __init__(self, graph, root):
        self.graph = graph
        self.visited = dict()
        self.stack = list()
        self.stack.append(root)
        self.counter = 0


    def run(self, target):
        """ YOUR CODE HERE """

        self.visited.clear()
        root = self.stack[0]
        self.stack.clear()
        match_found = False
        depth = 0

        match_found = self.dfs(root, target)

        # while len(self.stack) != 0:
        #     counter = counter + 1
        #     current_node = self.stack[0]
        #     depth = current_node.step
        #     children_nodes_list = self.graph.reveal_neighbors(current_node)
        #     self.visited[current_node.UID] = current_node
        #
        #     has_unique_child_node = False
        #     for child_node in children_nodes_list:
        #         if self.visited.get(child_node.UID) is None:
        #             self.stack.insert(0, child_node)
        #             self.visited[child_node.UID] = child_node
        #             has_unique_child_node = True
        #
        #     if has_unique_child_node is False:
        #         if current_node.is_equal(target):
        #             match_found = True
        #             break
        #         else:
        #             self.stack.pop(0)

        # return 3 items
        # a: bool (match found or not)
        # b: int (counter)
        # c: int (depth)
        return match_found, self.counter, depth

    def dfs(self, node, target):
        self.counter = self.counter + 1
        if self.visited.get(node.UID) is None:
            self.stack.insert(0, node)
            self.visited[node.UID] = node
        children_nodes_list = self.graph.reveal_neighbors(node)

        has_unique_child_node = False
        for child_node in children_nodes_list:
            if self.visited.get(child_node.UID) is None:
                has_unique_child_node = True
                return self.dfs(child_node, target)

        if has_unique_child_node is False:
            self.stack.pop(0)
            if node.is_equal(target):
                depth = node.step
                match_found = True
                return True
            else:
                return self.dfs(self.stack[0], target)




