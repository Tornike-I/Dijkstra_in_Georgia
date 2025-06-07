import heapq

# Node Class Used for creating new nodes with labels (names)
class Node:
    def __init__(self, label):
        self.label = label
        self.adjacency = {} # Stores all adjacency information of a node in form of {Node: Edge}

    def add_connection(self, node, cost): # Creates a connection between itself and another node
        edge = Edge(cost)
        self.adjacency[node] = edge

    def __lt__(self, other): # This method determines tiebreakers when adding two edges of the same cost.
        return self.label < other.label

class Edge: # Class for future scaling, storing information about road damage, accessability, etc.
    def __init__(self, cost):
        self.cost = cost


class Map: # Main Class
    def __init__(self):
        self.nodes = {} # Stores all nodes as {Node_label : Node_instance}

    def add_new_node(self, label):
        if label not in self.nodes:
            self.nodes[label] = Node(label)

    def lookup_node(self, label):
        return self.nodes.setdefault(label, Node(label)) # Mimicing autovivification to avoid multiple lookups

    def lookup_node(self, label):
        if self.nodes[label]:
            return self.nodes[label]
        return Node(label)

    def add_connection(self, node1_label, node2_label, cost):
        node1 = self.lookup_node(node1_label)
        node2 = self.lookup_node(node2_label)
        node1.add_connection(node2, cost)
        node2.add_connection(node1, cost) # Adding connection for both nodes as the graph is undirected

    def dijkstra(self, start_label, end_label):
        start = self.nodes.get(start_label) # Start Node
        end = self.nodes.get(end_label) # End Node
        if start is None or end is None:
            raise ValueError("Start or end node not found in the map.") # Rais error if entered node is wrong

        distances = {start: 0}
        previous = {} # To reconstruct path for displaying
        heap = [(0, start)] # The underlying data structure
        visited = set() # Set of uneque visisted nodes

        while heap: # Main loop
            current_dist, current_node = heapq.heappop(heap)
            if current_node in visited:
                continue
            visited.add(current_node)

            if current_node == end: # If the final destenation has been reached
                # Reconstruct path
                path = []
                while current_node: # Recustructs the path
                    path.append(current_node.label)
                    current_node = previous.get(current_node)
                path.reverse()
                return current_dist, path
            # Iteratively search and visist the available neighbours with shortest paths
            for neighbor, edge in current_node.adjacency.items():
                if neighbor in visited: # So that we dont traverse back
                    continue
                new_dist = current_dist + edge.cost
                if new_dist < distances.get(neighbor, float('inf')):
                    distances[neighbor] = new_dist
                    previous[neighbor] = current_node
                    heapq.heappush(heap, (new_dist, neighbor))

        return float('inf'), [] # In case a path does not exist

    def __repr__(self):
        output = ""
        for label, node in self.nodes.items():
            edges = ", ".join(f"{n.label}({w.cost})" for n, w in node.adjacency.items())
            output += f"{label}: {edges}\n"
        return output