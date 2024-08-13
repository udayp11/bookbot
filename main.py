#print("hello world")
def main():
    with open("books/frankenstein.txt") as f:
        book_text = f.read()
        word_count = words_number(book_text)
        dict_count = count_characters(book_text)
        
        report_print(dict_count,word_count)

def words_number(book_text):
    words_count = book_text.split()
    return len(words_count)

def count_characters(book_text):
    lowered_book_text = book_text.lower()
    dict = {}
    for char in lowered_book_text:
        if char in dict:
            pass
        else:
            count = lowered_book_text.count(char)
            dict[char] = count
    return dict

def report_print(dictonary_count,words_count):
    def sort_on(dict):
        return dict["count"]

    list_of_dict = []
    
    for key,value in dictonary_count.items():
        
        list_of_dict.append({"character": key, "count":value})
    
    list_of_dict.sort(reverse=True, key=sort_on)
    
    
    print("--- Begin report of books/frankenstein.txt ---")

    print(f"{words_count} words found in the document")
    for key in list_of_dict:
        if key["character"].isalpha():
            print(f"The '{key['character']}' character was found {key['count']} times")

    print("--- End report ---")

    



main()
