from xml.etree import ElementTree


def cubes_count(root):
    value = 0
    cnt_dict = {"red": 0, "green": 0, "blue": 0}

    def deep_first_traverse(elem):
        global value
        value += 1
        for child in elem:
            cnt_dict[child.attrib["color"]] += value
            deep_first_traverse(child)
        value -= 1

    deep_first_traverse(root)

    print("{} {} {}".format(cnt_dict["red"], cnt_dict["green"], cnt_dict["blue"]))


xml = '<cube color="blue"><cube color="red"><cube color="green"></cube></cube><cube color="red"></cube></cube>'
root = ElementTree.Element("root").append(ElementTree.fromstring(xml))

cubes_count(root)
