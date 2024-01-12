import main

def test_main():
    word = "word!"
    index = 4
    assert main.check_character(word, index) == "unknown"