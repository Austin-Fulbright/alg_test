#make_testcases.py
import cbor2


tests = [
        {"input": [[1, 3, 1], [1, 5, 1], [4, 2, 1]], "expected": 7},
        {"input":  [[1, 2, 3], [4, 5 ,6]], "expected": 12}
]


with open("testcases.cbor", "wb") as f:
    f.write(cbor2.dumps(tests))

