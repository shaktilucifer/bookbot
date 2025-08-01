from stats import get_words, get_char_map, printReport
# print(len(get_words('books/frankenstein.txt')))

dict = get_char_map(get_words('books/frankenstein.txt'))

printReport(len(get_words('books/frankenstein.txt')), dict, 'books/frankenstein.txt')