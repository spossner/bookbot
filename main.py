def count_words(book):
    words = book.split()
    return len(words)

def count_letters(book):
    counter = {}
    for c in book:
        if not c.isalpha():
            continue
        key = c.lower()
        if not key in counter:
            counter[key] = 0
        counter[key] += 1
    return reversed(sorted(counter.items(), key=lambda item:item[1]))

def create_report(name):
    with open(name) as f:
        book = f.read()
        print(f"--- Begin report of {name} ---")
        print(f"{count_words(book)} words found in document")
        print()
        for letter, qty in count_letters(book):
            print(f"The '{letter}' character was found {qty} times")
        print("--- End report ---")


create_report("books/frankenstein.txt")
