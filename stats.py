def get_num_words(text):
    words = text.split()
    return len (words)

def get_characters_dict(text):
    characters = text.lower()
    char = {}
    for character in characters:
       char[character] = char.get(character,0) + 1
    return char