def get_book_text (filepath):
        with open(filepath) as f:
                text = f.read()
        return text
def words_list (text):
        words = text.split()
        return words
def word_count (words):
        count = len(words)
        return count 
def main ():
        filepath = "books/frankenstein.txt"
        text = get_book_text(filepath)
        words = words_list(text)
        count = word_count(words)
        print(f"{count} words found in the document")

if __name__ == "__main__":
        main()