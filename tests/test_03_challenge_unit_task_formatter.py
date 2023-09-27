from lib._03_challenge_task_formatter import *
from unittest.mock import Mock

def test_task_if_format_complete():
    task = Mock(complete=True)
    task.title = "Task title 1"
    task_formatter = TaskFormatter(task)
    actual = task_formatter.format() 
    assert actual == "[x] Task title 1"

def test_task_if_format_incomplete():
    task = Mock(complete=False, title="Task title 1")
    task_formatter = TaskFormatter(task)
    actual = task_formatter.format() 
    assert actual == "[ ] Task title 1"