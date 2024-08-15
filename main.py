def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    number = get_number_of_words(text)
    character_dictionary = get_character_dictionary(text)
    chars_sorted_list = sorted_list_converter(character_dictionary)

    print(f"--- Begin report of {book_path} ---")
    print(f"{number} words found in the document")
    print()

    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")

    print("--- End report ---")
    

def get_number_of_words(text):
    words = text.split()
    return len(words)


def get_character_dictionary(text):
    characters = {}
    for i in text:
        lowered = i.lower()
        if lowered in characters:
            characters[lowered] += 1
        else:
            characters[lowered] = 1
    return characters


def get_book_text(path):
    with open(path) as f:
        return f.read()

def sort_on(d):
    return d["num"]


def sorted_list_converter(character_dictionary):
    sorted_list = []
    for c in character_dictionary:
        sorted_list.append({"char": c, "num": character_dictionary[c]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

main()