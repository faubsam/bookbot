
def main():
    book = "books/frankenstein.txt"
    contents = read_file(book)
    word_count = count_words(contents)
    char_count = count_chars(contents)
    
    print(f"--- Being report of {book} ---")
    print()
    print(f"The document contains {word_count} words")
    print()
    for c in char_count:
        print(f"The character {c} was found {char_count[c]} times")
    

    
def read_file(path):
    with open(path) as f:
        file_contents = f.read()
    return file_contents
    
def count_words(text):
    words = text.split()
    return len(words)

def count_chars(text):
    char_count = {}
    for char in text:
        if char.lower() not in char_count and char.isalpha():
            char_count[char.lower()] = 1
        else:
            if char.lower().isalpha():
                char_count[char.lower()] += 1
    return char_count
    
main()
    