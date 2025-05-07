#make_testcases.py
import cbor2


tests = [
        {"input": [1,2], "expected": 3},
        {"input":  [10, 20], "expected": 30}
]


with open("testcases.cbor", "wb") as f:
    f.write(cbor2.dumps(tests))

