def main():
    with open("books/frankenstein.txt") as f:
        file_content = f.read()
        return file_content

def wordcount():
    count = 0
    content = main()
    words = content.split()
    return words

def count_characters():
    content_2 = main()
    lowered_content = content_2.lower()
    characters = {}
    for letter in lowered_content:
        if letter not in characters:
            characters[letter] = 1
        else:
            characters[letter] += 1
    print(characters)
count_characters()