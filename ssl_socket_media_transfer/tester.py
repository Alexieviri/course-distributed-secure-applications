import os
import numpy as np

def test(path_client, path_server):
    size_img_client = os.path.getsize(path_client)
    size_img_server = os.path.getsize(path_server)
    assert size_img_client == size_img_server, "Not equal"

if __name__ == "__main__":
    test("example.jpg","server-example.jpg")