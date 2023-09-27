from lib._03_exercise_diary import Diary
from lib._03_exercise_secret_diary import SecretDiary
import pytest

# Initialises with instance of Diary() as diary and lock status as True
def test_initialises_mock_diary_and_True_lock_status():
    diary = Diary("Some contents")
    secret_diary = SecretDiary(diary)
    assert secret_diary.diary == diary
    assert secret_diary.locked == True

# read() method returns error "Go away!" if secret_diary locked
def test_read_returns_contents_if_unlocked():
    diary = Diary("Some contents") 
    secret_diary = SecretDiary(diary)
    with pytest.raises(Exception) as e:
        secret_diary.read()
    error_message = str(e.value)
    assert error_message == "Go away!"

# unlock() changes self.locked status to False
def test_unlock_method_changes_lock_status_to_False():
    diary = Diary("Some contents") 
    secret_diary = SecretDiary(diary)
    secret_diary.unlock()
    assert secret_diary.locked == False

# read() method returns diary contents if secret_diary unlocked
def test_read_returns_contents_if_unlocked():
    diary = Diary("Some contents") 
    secret_diary = SecretDiary(diary)
    secret_diary.unlock()
    assert secret_diary.read() == "Some contents"

# lock() changes self.locked to True
def test_lock_method_changes_lock_status_to_True():
    diary = Diary("Some contents") 
    secret_diary = SecretDiary(diary)
    secret_diary.unlock()
    assert secret_diary.read() == "Some contents"
    secret_diary.lock()
    with pytest.raises(Exception) as e:
        secret_diary.read()
    error_message = str(e.value)
    assert error_message == "Go away!"