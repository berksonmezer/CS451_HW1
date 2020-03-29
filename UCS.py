import queue as Q


class UCS:
    def __init__(self, graph, root):
        self.graph = graph
        self.visited = dict()
        self.queue = Q.PriorityQueue()
        self.counter = 0
        self.visited[root.UID] = root
        self.queue.put((root.UID, root, root.step))

    def run(self, target):
        """ YOUR CODE HERE """
        match_found = False
        while not self.queue.empty():
            self.counter = self.counter + 1
            current_node = self.queue.get()[1]
            self.visited[current_node.UID] = current_node
            depth = current_node.step
            if current_node.is_equal(target):
                match_found = True
                break

            children_nodes_list = self.graph.reveal_neighbors(current_node)
            for child_node in children_nodes_list:
                if self.visited.get(child_node.UID) is None:
                    priority_number = current_node.step
                    self.queue.put((child_node.UID, child_node, priority_number))

        # return 3 items
        # a: bool (match found or not)
        # b: int (counter)
        # c: int (depth)
        return match_found, self.counter, depth
