from pyQubit import math
import numpy as np

test: dict = {
    "rated_ndarray": {
        "func": math.array.rated_ndarray,
        "args": {
            "size": 4
        },
        "expect": {
            "func": np.sum,
            "result": 1
        }
    }
}

rated = test["rated_ndarray"]["func"](**test["rated_ndarray"]["args"])
print(np.sum(rated) == 1)
