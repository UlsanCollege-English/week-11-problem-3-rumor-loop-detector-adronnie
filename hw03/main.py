"""
HW03 — Rumor Loop Detector (Cycle in Undirected Graph)
"""

def has_cycle(graph):
    """Return True if the undirected graph has any cycle; else False."""
    visited = set()

    def dfs(u, parent):
        visited.add(u)
        for v in graph.get(u, []):
            if v == u:
                # Self-loop counts as a cycle
                return True
            if v not in visited:
                if dfs(v, u):
                    return True
            elif v != parent:
                # Found a back edge -> cycle
                return True
        return False

    for node in graph:
        if node not in visited:
            if dfs(node, None):
                return True
    return False


def find_cycle(graph):
    """Return a list of nodes forming a simple cycle (first==last), or None if no cycle."""
    visited = set()
    parent = {}

    def dfs(u, par):
        visited.add(u)
        parent[u] = par
        for v in graph.get(u, []):
            if v == u:
                # Self-loop detected
                return [u, u]
            if v not in visited:
                res = dfs(v, u)
                if res:
                    return res
            elif v != par:
                # Found a back edge u->v
                # Reconstruct cycle from u to v
                cycle = [v, u]
                p = u
                while parent[p] != v:
                    p = parent[p]
                    cycle.append(p)
                cycle.append(v)
                cycle.reverse()
                return cycle
        return None

    for node in graph:
        if node not in visited:
            cycle = dfs(node, None)
            if cycle:
                return cycle

    return None


if __name__ == "__main__":
    # Manual test examples
    g1 = {
        'A': ['B'],
        'B': ['A','C'],
        'C': ['B','D'],
        'D': ['C','A']
    }
    g2 = {
        'X': ['X']  # self-loop
    }
    g3 = {
        'P': ['Q'],
        'Q': ['P','R'],
        'R': ['Q']
    }

    print(has_cycle(g1))  # True
    print(find_cycle(g1)) # e.g., ['A','B','C','D','A']
    print(has_cycle(g2))  # True
    print(find_cycle(g2)) # ['X','X']
    print(has_cycle(g3))  # False
    print(find_cycle(g3)) # None
