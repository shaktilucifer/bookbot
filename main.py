from stats import get_words, get_char_map, printReport
import sys

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")

bookFilePath=sys.argv[1];


dict = get_char_map(get_words(bookFilePath))

printReport(len(get_words(bookFilePath)), dict, bookFilePath)

