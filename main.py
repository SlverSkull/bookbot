def main():
    book_path = "books/frankenstein.txt"
    file_contents = book(book_path)
    full_report = report(book_path, file_contents)

def book(file):
    with open(file) as f:
        return f.read()

def count(text):
    words = text.split()
    return len(words)

def character_count(text):
    lowered_text = text.lower()
    text_dictionary = {}
    for c in lowered_text:
        if c in text_dictionary:
            text_dictionary[c] += 1
        else:
            text_dictionary[c] = 1
    return text_dictionary

def report(path, text):
    word_count = count(text)
    dictionary = character_count(text)
    letter_dictionary = {}
    aplphabet = "abcdefghijklmnopqrstuvwxyz"
    
    for c in aplphabet:
        letter_dictionary[c] = dictionary[c]
    
    print("--- " + path + " ---\nTotal Word Count: " + str(word_count))
    for c in letter_dictionary:
        print("\nTotal '" + c + "' Count: " + str(letter_dictionary[c]))
    print("\n--- End Report ---")

main()