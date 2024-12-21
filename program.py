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
    return characters
def sort_on(dict):
    return dict["num"]
def report():
    characters_list = []
    charac = count_characters()
    for character in charac:
        if character.isalpha():
            characters_list.append({"char": character, "num": charac[character]})
    characters_list.sort(reverse=True, key=sort_on)
    print("--- Begin report of books/frankenstein.txt ---")
    print(len(wordcount()),  "words were found in the document")
    for dicti in characters_list:
        print(f"The '{dicti['char']}' character was found {dicti['num']} times" )
    print("--- End report ---")
report()