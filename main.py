def main():
    file_path = "books/frankenstein.txt"
    with open(file_path) as f:
        
        file_contents = f.read()
        words_count = get_char_count(file_contents)
        char_count = get_word_count(file_contents)
        chars_sorted = chars_dict_sorted_list(words_count)
        
        print(f"--- Begin report of {file_path} ---\n")
        print(f"{char_count} words found in the document\n")

        for item in chars_sorted:
            if not item['char'].isalpha():
                continue
            print(f"The '{item['char']}' character was found {item['num']} times")
        
        print("\n--- End report ---")

    
def get_word_count(string: str) -> int:
    return len(string.split())

def get_char_count(string: str) -> dict[str: int]:
    count = {}
    for c in string:
        lowered = c.lower()
        if lowered not in count:
            count[lowered] = 1
        else:
            count[lowered] += 1
    return count

def chars_dict_sorted_list(num_chars_dict):
    sorted_list = []
    for c in num_chars_dict:
        sorted_list.append({'char': c, 'num': num_chars_dict[c]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

def sort_on(d):
    return d["num"]

if __name__ == '__main__':
    main()