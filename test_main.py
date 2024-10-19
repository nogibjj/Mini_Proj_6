from main import add


def test_add():
    """testing  out add function"""
    assert add(2, 2) == 4
    assert add(1, 3) == 4
    assert add(1, 5) == 6


if __name__ == "__main__":
    test_add()
