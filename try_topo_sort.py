from graphlib import TopologicalSorter

if __name__ == "__main__":
    # From https://docs.python.org/3/library/graphlib.html#graphlib.TopologicalSorter
    graph = {"D": {"B", "C"}, "C": {"A"}, "B": {"A"}}
    ts = TopologicalSorter(graph)
    print(tuple(ts.static_order()))  # ('A', 'C', 'B', 'D')