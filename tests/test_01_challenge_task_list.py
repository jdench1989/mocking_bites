from lib.task_list import TaskList
from unittest.mock import Mock


def test_task_list_initially_empty():
    task_list = TaskList()
    assert task_list.tasks == []


def test_tasks_initially_not_all_complete():
    task_list = TaskList()
    assert task_list.all_complete() == False

# Unit test `#tasks` and `#all_complete` behaviour

def test_with_mocking_all_returns_list_of_tasks():
    task_list = TaskList()
    mock_task_1 = Mock()
    mock_task_2 = Mock()
    task_list.add(mock_task_1)
    task_list.add(mock_task_2)
    assert task_list.all() == [mock_task_1, mock_task_2]

def test_with_mocking_all_complete_returns_True_if_tasks_complete():
    task_list = TaskList()
    mock_task_1 = Mock()
    mock_task_2 = Mock()
    mock_task_1.is_complete.return_value = True
    mock_task_2.is_complete.return_value = True
    task_list.add(mock_task_1)
    task_list.add(mock_task_2)
    assert task_list.all_complete() == True

def test_with_mocking_all_complete_returns_False_if_all_incomplete():
    task_list = TaskList()
    mock_task_1 = Mock()
    mock_task_2 = Mock()
    mock_task_1.is_complete.return_value = False
    mock_task_2.is_complete.return_value = False
    task_list.add(mock_task_1)
    task_list.add(mock_task_2)
    assert task_list.all_complete() == False

def test_with_mocking_all_complete_returns_False_if_mixed():
    task_list = TaskList()
    mock_task_1 = Mock()
    mock_task_2 = Mock()
    mock_task_1.is_complete.return_value = False
    mock_task_2.is_complete.return_value = True
    task_list.add(mock_task_1)
    task_list.add(mock_task_2)
    assert task_list.all_complete() == False