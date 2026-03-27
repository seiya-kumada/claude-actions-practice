def add(a, b):
    return a + b


if __name__ == "__main__":
    assert add(1, 2) == 3
    assert add(-1, 1) == 0
    assert add(0, 0) == 0
    assert add(1.5, 2.5) == 4.0
    print("All tests passed!")
