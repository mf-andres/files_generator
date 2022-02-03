def get_word_end_index(str_: str, word: str):
    word_end_index = str_.find(word) + len(word) - 1
    return word_end_index
