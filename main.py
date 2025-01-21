



def main():
    #define path; use open with to ensure proper closure
    path = "./books/frankenstein.txt"
    with open(path) as f:
        file_contents = f.read()
        #lowercase all characters
        words = file_contents.lower()
        #split by words to determine word count 
        book_length = len(words.split())
        char_dict = char_duplicates(words)
        print_out(path, book_length, char_dict)
        
def char_duplicates(words):
    #determine character count
    char_count = {}
    for letter in words:
        if letter in char_count:
            char_count[letter] += 1
        else:
            char_count[letter] = 1
    return char_count

def print_out(path, book_length, char_dict):
    # prepare and print out alaphabtic characters only and sort by appearnce number
    ordered_list = []
    sort_key = []
    for key in char_dict:
        #filter by alaphabtic char only append them to the sort key and ordered_list
        if key.isalpha():
            sort_key.append(key)
            ordered_list.append({key : char_dict[key]})
    #function to pass to .sort()
    #included a factory function to pass sort_key list 
    def create_sorter(sort_key):
        def sort_on(item):
            for key in sort_key:
                if key in item:
                    return item[key]
            else:
                return None
        return sort_on

    ordered_list.sort(reverse=True, key=create_sorter(sort_key))
    #print output
    def final_print_report():
        print(f"--- Static Analysis of {path} ---\n{book_length} words found in the document")
        for item in ordered_list:
            for key in item:
                print(f"The '{key}' character was found {item[key]} times")
        print("--- End Report ---")
    #call final_print_report
    final_print_report()
main()


