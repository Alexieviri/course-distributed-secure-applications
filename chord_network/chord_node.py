#!/usr/bin/env python3
from __future__ import annotations
from typing import *
from finger import Finger

import random


class ChordNode:
    _id: int
    finger_table: List[Finger]
    predecessor: ChordNode

    def __init__(self, m: int, n: int):
        self._id = n
        self.finger_table = [Finger(m, n, i, self) for i in range(m)]
        self.predecessor = self

    def get_successor(self) -> ChordNode:
        return self.finger_table[0].node

    def set_successor(self, successor: ChordNode):
        self.finger_table[0].node = successor

    def find_successor(self, _id: int) -> ChordNode:
        return self.find_predecessor(_id).get_successor()

    def find_predecessor(self, _id: int) -> ChordNode:
        node = self
        while not (self.id_in_range(_id, node._id, node.get_successor()._id) or _id == node.get_successor()._id):
            node = node.closest_preceding_finger(_id)

        return node

    def closest_preceding_finger(self, j: int) -> ChordNode:
        m: int = len(self.finger_table)
        for i in range(m - 1, -1, -1):
            node: ChordNode = self.finger_table[i].node
            if self.id_in_range(node._id, self._id, j):
                return node
        return self

    def join(self, node: ChordNode):
        if node is not None:
            self.init_finger_table(node)
            self.update_others()
        else:
            for finger in self.finger_table:
                finger.node = self
            self.predecessor = self

    def init_finger_table(self, node: ChordNode):
        successor: ChordNode = self.get_successor()
        self.finger_table[0].node = node.find_predecessor(self.finger_table[0].start)
        self.predecessor = successor.predecessor
        successor.predecessor = self

        m: int = len(self.finger_table)
        for i in range(m - 1):
            if self._id == self.finger_table[i + 1].start or self.id_in_range(self.finger_table[i + 1].start, self._id,
                                                                              self.finger_table[i].node._id):
                self.finger_table[i + 1].node = self.finger_table[i].node
            else:
                self.finger_table[i + 1].node = node.find_successor(self.finger_table[i + 1].start)

    def update_others(self):
        m: int = len(self.finger_table)
        for i in range(m):
            # j = _id - 2^i
            j: int = self._id - (1 << i)
            if j < 0:
                j += 1 << m
            p: ChordNode = self.find_predecessor(j)
            p.update_fingertable(self, i)

    def update_fingertable(self, s: ChordNode, i: int):
        if self._id == s._id or self.id_in_range(s._id, self._id, self.finger_table[i].node._id):
            self.finger_table[i].node = s
            p: ChordNode = self.predecessor
            p.update_fingertable(s, i)

    def join2(self, node: ChordNode):
        if node is not None:
            self.predecessor = None
            self.set_successor(node.find_successor(self._id))
        else:
            for finger in self.finger_table:
                finger.node = self
            self.predecessor = self

    def stabilize(self):
        x: ChordNode = self.get_successor().predecessor
        if self.id_in_range(x._id, self._id, self.get_successor()._id):
            self.set_successor(x)
        self.get_successor().notify(self)

    def notify(self, node: ChordNode):
        if self.predecessor is None or self.id_in_range(node._id, self.predecessor._id, self._id):
            self.predecessor = node

    def fix_fingers(self):
        i: int = random.randrange(len(self.finger_table))
        self.finger_table[i].node = self.find_successor(self.finger_table[i].start)

    def find_by_id(self, i: int) -> Optional[ChordNode]:
        node: ChordNode = self
        visited: set = set()
        while node._id != i:
            visited.add(node)
            for finger in self.finger_table:
                if i == finger.node._id:
                    return finger.node
                if finger.interval_start == i or self.id_in_range(i, finger.start, finger.interval_end):
                    node = finger.node
            if node in visited:
                return None
        return node

    def _delete(self):
        self.predecessor.set_successor(self.get_successor())
        self.get_successor().predecessor = self.predecessor

        m: int = len(self.finger_table)
        for i in range(m):
            # j = _id - 2^i
            j: int = self._id - (1 << i)
            if j < 0:
                j += 1 << m
            p: ChordNode = self.find_predecessor(j)
            p.update_fingertable(self.get_successor(), i)

    def id_in_range(self, i: int, a: int, b: int) -> bool:
        end: int = b
        ii: int = i
        m: int = len(self.finger_table)

        if a >= b:
            end += 1 << m
            if a > i:
                ii += 1 << m

        return a < ii and ii < end

    def __repr__(self):
        res: str = ""
        res += f"{self._id}\n"
        res += f"| start | interval | node|"
        res += "\n"
        res += "--------------------------"
        res += "\n"
        for finger in self.finger_table:
            res += f"|   {finger.start}   |  [{finger.interval_start}, {finger.interval_end})  |   {finger.node._id}\n"
        res += "--------------------------"
        return res
