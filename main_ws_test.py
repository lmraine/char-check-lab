import main

def test_main():
    word = "word or two"
    index = 7
    assert main.check_character(word, index) == "white space"