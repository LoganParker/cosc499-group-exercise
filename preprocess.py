import re


def read_text(filename: str) -> str:
    """
        This function reads a file given a file path and converts contents into a string. 
    """
    with  open(filename, 'r', encoding='utf-8', newline='\n') as file:
        file_string = file.read()

        return file_string


# Helper functions for preproc_text()
def __remove_new_line(string: str) -> str:
    """
    Return a copy of the string with new lines replaced with a single space.
    """
    return string.replace("\n", " ")


def __remove_contractions(string: str) -> str:
    """
    Return a copy of the string with English contractions replaced.
    WARNING: will change word count.
    """
    string = re.sub(r'\'s', ' is', string)
    string = re.sub(r'n\'t', ' not', string)
    string = re.sub(r'\'ve', ' have', string)
    string = re.sub(r'\'re', ' are', string)
    string = re.sub(r'\'m', ' am', string)
    string = re.sub(r'\'ll', ' will', string)
    return string


def __remove_punctuation(string: str) -> str:
    """
    Return a copy of the string without punctuation or special characters.
    """
    return re.sub(r'[^a-z\n ]', '', string)


def __remove_whitespaces(string: str) -> str:
    """
    Return a copy of the string after converting any multiple spaces to one space and removing leading and trailing whitespaces.
    """
    string = re.sub(r'\s+', ' ', string)
    return string.strip()


def preproc_str(string: str, replaceContractions: bool = False) -> str:
    """
    Returns a copy of the string after converting it to lowercase without punctuation, whitespace, or contractions (optional).
    string: the string to convert.
    replaceContractions: boolean to indicate if you want contractions replaced (default is set to False).
    WARNING: if replaceContractions is False, this may result in non-words (i.e., don't -> dont).
    """
    string = string.lower()
    string = __remove_new_line(string)
    if (replaceContractions):
        string = __remove_contractions(string)
    string = __remove_punctuation(string)
    string = __remove_whitespaces(string)
    return string


def get_word_count(string: str) -> int:
    """
    Returns an integer indicating the number of words in the string.
    Uses preproc_str() first to ensure special characters are not counted as words.
    """
    arr_str = preproc_str(string).split(" ")
    return len(arr_str)


def sort_text(text: str) -> list:
    """
    This function sorts the inputted text string
    :param text: A preprocessed string
    :return: sorted list
    """
    text = preproc_str(text)
    text_array = text.split()
    text_array.sort()
    return text_array
