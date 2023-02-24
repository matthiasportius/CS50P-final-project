import pytest
from project import (get_files, filter_files_include, filter_files_exclude,
                     get_oldest_file, get_olderthen_files)


def test_get_files():
    with pytest.raises(SystemExit):
        get_files("invalid_path .?!")


def test_filter_files_include():
    files = ["test1.txt", "test2.txt", "test3.jpg", "test4.docx", "test5.mp3"]
    files_filtered = filter_files_include(".txt", files)
    assert files_filtered == ["test1.txt", "test2.txt"]
    with pytest.raises(SystemExit):
        filter_files_include("invalid_extension", files)


def test_filter_files_exclude():
    files = ["test1.txt", "test2.txt", "test3.jpg", "test4.docx", "test5.mp3"]
    files_filtered = filter_files_exclude(".txt", files)
    assert files_filtered == ["test3.jpg", "test4.docx", "test5.mp3"]
    with pytest.raises(SystemExit):
        filter_files_exclude("invalid_extension", files)


def test_get_oldest_file():
    oldest_file = get_oldest_file([])
    assert oldest_file == "File least used:   No file found\n"


def test_get_olderthen_files():
    older_then = 3
    olderthen_files = get_olderthen_files(older_then, [])
    assert olderthen_files == f"Files not used for {older_then} days:   None\n"
    older_then = 1
    olderthen_files = get_olderthen_files(older_then, [])
    assert olderthen_files == f"Files not used for {older_then} day:   None\n"
