from stats import get_num_words, character_count
def main():
	text = get_book_text("books/frankenstein.txt")
	counter = character_count(text)
	print(f"Found {get_num_words(text)} total words")
	print(counter)	
def get_book_text(filepath):
        try:
                with open(filepath) as file:
                        return file.read()
        except FileNotFoundError as error:
                raise FileNotFoundError(f"Missing file at {filepath}") from error	
	
	
main()
