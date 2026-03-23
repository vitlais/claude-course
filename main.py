def add(a, b):
    """Add two numbers and return the result."""
    return a + b


def test_add():
    """Test function for the add function."""
    assert add(1, 2) == 3
    assert add(0, 0) == 0
    assert add(-1, 1) == 0
    assert add(10, -5) == 5
    print("All tests passed!")


def main():
    print("Hello from claude-course!")
    test_add()


if __name__ == "__main__":
    main()
