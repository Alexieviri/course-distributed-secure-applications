#!/usr/bin/env python3
def generate_start(m: int, n: int, i: int) -> int:
    # (n + 2^i) % (2 % m)
    return (n + (1 << i)) % (1 << m)