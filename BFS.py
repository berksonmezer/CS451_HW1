class BFS:
    def __init__(self, graph, root):
        self.graph = graph
        self.visited = dict()
        self.queue = list()
        self.counter = 0
        self.visited[root.UID] = root
        self.queue.append(root)

    def run(self, target):
        """ YOUR CODE HERE """
        match_found = False
        counter = 0
        depth = 0
        while len(self.queue) != 0:
            counter = counter + 1
            candidate_node = self.queue.pop()
            if candidate_node.is_equal(target):
                match_found = True
                depth = candidate_node.step
                break

            children_nodes_list = self.graph.reveal_neighbors(candidate_node)
            for child_node in children_nodes_list:
                self.queue.insert(0, child_node)

        # return 3 items
        # a: bool (match found or not)
        # b: int (counter)
        # c: int (depth)
        # return False, 0, 0
        return match_found, counter, depth
