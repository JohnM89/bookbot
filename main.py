



def main():
    with open("./books/frankenstein.txt") as f:
        file_contents = f.read()
        words = len(file_contents.split())
        print(words)
main()
