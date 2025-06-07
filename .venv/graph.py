class Node:
    def __init__(self, label):
        self.label = label
        self.adjacency = {}
    def add_connection(self, node, cost):
        edge = Edge(cost)
        self.adjacency[node] = edge

class Edge:
    def __init__(self, cost):
        self.cost = cost


class Map:
    def __init__(self):
        self.nodes = {}

    def add_new_node(self, label):
        if label not in self.nodes:
            self.nodes[label] = Node(label)

    def lookup_node(self, label):
        return self.nodes.setdefault(label, Node(label)) # Mimicing autovivification to avoid multiple lookups

    def add_connection(self, node1_label, node2_label, cost):
        node1 = self.lookup_node(node1_label)
        node2 = self.lookup_node(node2_label)
        node1.add_connection(node2, cost)
        node2.add_connection(node1, cost) # Adding connection for both nodes as the graph is undirected

    def __repr__(self):
        output = ""
        for label, node in self.nodes.items():
            edges = ", ".join(f"{n.label}({w.cost})" for n, w in node.adjacency.items())
            output += f"{label}: {edges}\n"
        return output