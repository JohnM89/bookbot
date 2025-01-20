



def main():
    with open("./books/frankenstein.txt") as f:
        file_contents = f.read()
        words = file_contents.lower()
        print(len(words))
        char_dict = char_duplicates(words)
        print(char_dict)

def char_duplicates(words):
    char_count = {}
    for letter in words:
        if letter in char_count:
            char_count[letter] += 1
        else:
            char_count[letter] = 1
    return char_count

main()


