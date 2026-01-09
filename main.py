from stats import num_words, count_letters,sorted_list
import sys

def get_book_text(book):
    with open(book) as f:
        return f.read()
    

def main():

    if len(sys.argv) != 2 :
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    text = get_book_text(sys.argv[1])
    word_count = num_words(text)
    letter_count = count_letters(text)
    
    
    
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f'Found {word_count} total words')
    print("--------- Character Count -------")

    #print(letter_count)

    lists = sorted_list(text)
    for dic in lists:
        if dic['char'].isalpha():
            print(f"{dic['char']}: {dic['num']}")


if __name__ == "__main__":
    main()

