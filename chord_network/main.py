#!/usr/bin/env python3
from typing import *
from chord_node import ChordNode


def StabilizeAndShow(nodes: List[ChordNode]):
    st_iterations: int = 15
    
    print('**** Stabilisation start, with:', st_iterations, ' iterations ****')
    for i in range(st_iterations):
        for node in nodes:
            node.stabilize()
            node.fix_fingers()

    for node in nodes:
        print(node)

    print("**** Stabilisation performed ****")


if __name__ == "__main__":
    m: int = 3

    nodes: List[ChordNode] = []

    head: ChordNode = ChordNode(3, 0) # create 0th
    head.join(None)
    nodes.append(head)

    for n in [1, 3]: # create 1 and 3th
        node: ChordNode = ChordNode(m, n)
        node.join2(head)
        nodes.append(node)

    StabilizeAndShow(nodes)

    anothernode: ChordNode = ChordNode(m, 6)
    anothernode.join2(head)
    nodes.append(anothernode)

    StabilizeAndShow(nodes)

    anothernode._delete()
    nodes.remove(anothernode)

    StabilizeAndShow(nodes)
'''
    #delete and remove 3th node
    print('++++++++++++')
    anothernode = nodes[2]
    anothernode._delete()
    nodes.remove(anothernode)
    StabilizeAndShow(nodes)
    '''