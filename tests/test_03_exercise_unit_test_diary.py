from lib._03_exercise_diary import Diary
import pytest

# Initialises with contents stored in self.contents attribute
def test_initialises_with_contents_stored():
    diary = Diary("Some contents")
    assert diary.contents == "Some contents"

# Throws error if contents are not a string
def test_contents_must_be_string_or_error_thrown():
    with pytest.raises(Exception) as e:
        diary = Diary(123)
    error_message = str(e.value)
    assert error_message == "Contents must be a string"

# read() method returns the contents of the diary
def test_read_method_returns_contents_correctly():
    diary = Diary("These are the contents")
    assert diary.read() == "These are the contents"
