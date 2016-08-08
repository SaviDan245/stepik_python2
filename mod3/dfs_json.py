from json import loads


def children_count(inptut_str):
    prt_chds = input_handling(inptut_str)
    cnt_dict = {cls: deep_first_traverse(prt_chds, cls, set()) for cls in prt_chds}

    for cls, num in sorted(cnt_dict.items()):
        print("{} : {}".format(cls, num))


def input_handling(inptut_str):
    # Create `child -> parents` dict
    chd_prts = {child["name"]: child["parents"] for child in loads(inptut_str.strip())}

    # Create `parent -> children` dict
    prt_chds = {cls: [] for cls in chd_prts}
    for child, parents in chd_prts.items():
        for parent in parents:
            prt_chds[parent].append(child)

    return prt_chds


def deep_first_traverse(graph, start, visited=set()):
    visited.add(start)
    for nxt in set(graph[start]) - visited:
        deep_first_traverse(graph, nxt, visited)

    return len(visited)


inptut_str1 = """
    [{"name": "A", "parents": []}, {"name": "B", "parents": ["A", "C"]}, {"name": "C", "parents": ["A"]}]
"""
inptut_str2 = """
    [{"name": "A", "parents": ["B", "C", "D"]},
    {"name": "E", "parents": ["F", "G"]},
    {"name": "I", "parents": ["E", "F", "Y", "D", "G"]},
    {"name": "B", "parents": ["I", "Y", "D", "G"]},
    {"name": "F", "parents": ["D", "Z"]},
    {"name": "C", "parents": ["Y", "G", "Z"]},
    {"name": "Y", "parents": []},
    {"name": "D", "parents": []},
    {"name": "G", "parents": ["Y", "D"]},
    {"name": "Z", "parents": ["D", "G"]}]
"""

children_count(inptut_str2)
