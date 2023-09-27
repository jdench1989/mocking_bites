from lib._03_exercise_secret_diary import SecretDiary
from unittest.mock import Mock
import pytest

def create_fake_diary(contents):
    fake_diary = Mock()
    fake_diary.contents = contents
    fake_diary.read.return_value = fake_diary.contents
    return fake_diary

# Initialises with Diary mock as diary and lock status as True
def test_initialises_mock_diary_and_True_lock_status():
    fake_diary = create_fake_diary("Some contents") 
    secret_diary = SecretDiary(fake_diary)
    assert secret_diary.diary == fake_diary
    assert secret_diary.locked == True

# read() method returns "Go away!" if secret_diary locked
def test_read_returns_contents_if_unlocked():
    fake_diary = create_fake_diary("Some contents") 
    secret_diary = SecretDiary(fake_diary)
    assert secret_diary.read() == "Go away!"

# unlock() changes self.locked status to False
def test_unlock_method_changes_lock_status_to_False():
    fake_diary = create_fake_diary("Some contents") 
    secret_diary = SecretDiary(fake_diary)
    secret_diary.unlock()
    assert secret_diary.locked == False

# read() method returns diary contents if secret_diary unlocked
def test_read_returns_contents_if_unlocked():
    fake_diary = create_fake_diary("Some contents") 
    secret_diary = SecretDiary(fake_diary)
    secret_diary.unlock()
    assert secret_diary.read() == "Some contents"

# lock() changes self.locked to True
def test_lock_method_changes_lock_status_to_True():
    fake_diary = create_fake_diary("Some contents") 
    secret_diary = SecretDiary(fake_diary)
    secret_diary.unlock()
    assert secret_diary.read() == "Some contents"
    secret_diary.lock()
    with pytest.raises(Exception) as e:
        secret_diary.read()
    error_message = str(e.value)
    assert error_message == "Go away!"
