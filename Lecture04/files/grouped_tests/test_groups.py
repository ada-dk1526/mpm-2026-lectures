# Test math operations
class TestMathOperations:
    
    def test_addition(self):
        assert 1 + 2 == 3

    def test_subtraction(self):
        assert 5 - 3 == 2

    def test_multiplication(self):
        assert 2 * 3 == 6

    def test_division(self):
        assert 10 / 2 == 5


# Test string operations
class TestStringOperations:
    
    def test_uppercase(self):
        assert "hello".upper() == "HELLO"

    def test_lowercase(self):
        assert "HELLO".lower() == "hello"

    def test_split(self):
        assert "hello world".split() == ["hello", "world"]

    def test_contains(self):
        assert "world" in "hello world"

