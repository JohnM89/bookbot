import sys
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
#using re to provide regex operations on splitting words
import re


def main():
    #define path; use open with to ensure proper closure
    if len(sys.argv) != 2:
        print("please provide path to text as argument")
        exit()
    path = sys.argv[1]
    comment_words = ''
    stopwords = set(STOPWORDS)

    with open(path) as f:
        file_contents = f.read()
        #lowercase all characters
        words = file_contents.lower()
        #split by words to determine word count 
        book_length = len(words.split())
        char_dict = char_duplicates(words)
        print_out(path, book_length, char_dict, words)
        #word_count(words)
#setup wordcloud canvas
def plot_wordcloud(words, path):
    wordcloud = WordCloud(width = 800, height = 800, background_color = 'white', stopwords = set(STOPWORDS), min_font_size = 8).generate(words)
    plt.figure(figsize = (8, 8), facecolor = None)
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.tight_layout(pad = 0)
    plt.savefig(f"{path}.png")

def char_duplicates(words):
    #determine character count
    char_count = {}
    for letter in words:
        if letter in char_count:
            char_count[letter] += 1
        else:
            char_count[letter] = 1
    return char_count

def word_count(words):
    #replce the newline characters with a space
    cleaned_text = re.sub(r'\n+', ' ', words)
    #split the text using regex pattern matching
    #using positive lookahread and lookbehind assertion to match \s, ?, !, ., (, or )
    tokens = re.split(r'(?<=[\s?!.,()\'\"])|(?=[\s?!.,()\'\"])', cleaned_text.strip())
    word_dict = {}
    for word in tokens:
        if word in word_dict:
            word_dict[word] += 1     
        else:
            word_dict[word] = 1
    return word_dict
    
        



def print_out(path, book_length, char_dict, words):
    # prepare and print out alaphabtic characters only and sort by appearnce number
    # #likewise for word instances (omitting alaphabtic character filter for now)
    ordered_list = []
    ordered_word_list = []
    sort_key = []
    sort_word_key = []
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
    def print_report():
        print(f"--- Static Analysis of {path} ---\n{book_length} words found in the document")
        for item in ordered_list:
            for key in item:
                
                print(f"The '{key}' character was found {item[key]} times")
        print("--- Preparing Word Analysis ---")
    
    #call print_report
    print_report()
    final_print_word_dict = word_count(words)
    for key in final_print_word_dict:
        sort_word_key.append(key)
        ordered_word_list.append({key:final_print_word_dict[key]})
    
    ordered_word_list.sort(reverse=True, key=create_sorter(sort_word_key))
    #funciton to print word count (does not expluce spaces and special characters as words due to limitations of current regex implementation)
    def print_final_report():
        count = 20
        print(f" Top {count} words in {path}")
        for item in ordered_word_list:
            for key in item:
                if count > 0:
                    print(f"The word '{key}' was found {item[key]} times")
                    count -= 1
    print_final_report()

    #call wordcloud canvas (saved to .png)
    plot_wordcloud(words, path)
main()


