from stats import get_num_words
from stats import get_characters_dict


def main():
    book_path ="books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    char_counts = get_characters_dict(text)
    print (f"{num_words} words found in the document")
    print (char_counts)

def get_book_text(path):
    with open(path) as f:
        return f.read()

main() 
     
