#!/usr/bin/env python3
import utils


class Finger:
    start: int
    interval_start: int
    interval_end: int
    node = None

    def  __init__(self, m: int, n: int, i: int, node):
        self.start = utils.generate_start(m, n, i)
        self.interval_start = self.start
        self.interval_end = utils.generate_start(m, n, i+1)
        self.node = node
