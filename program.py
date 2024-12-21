def main():
    with open("books/frankenstein.txt") as f:
        file_content = f.read()
        return file_content
def wordcount():
    count = 0
    content = main()
    words = content.split()
    print(len(words))
wordcount()