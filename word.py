import string

def count_words(text):
    # Remove punctuation using str.translate
    translator = str.maketrans('', '', string.punctuation)
    cleaned_text = text.translate(translator)
    
    # Convert text to lowercase
    cleaned_text = cleaned_text.lower()
    
    # Split text into words
    words = cleaned_text.split()
    
    return len(words)

def read_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        return None

def main():
    print("Welcome to the Word Counting Program!")
    
    while True:
        print("\nChoose an option:")
        print("1. Enter text manually")
        print("2. Load text from a file")
        print("3. Exit")
        
        choice = input("Enter your choice (1/2/3): ")
        
        if choice == '1':
            text = input("\nEnter your text: ")
            if text.strip():
                word_count = count_words(text)
                print(f"The text contains {word_count} words.")
            else:
                print("Error: The text entered is empty.")
        
        elif choice == '2':
            file_path = input("\nEnter the file path: ")
            text = read_from_file(file_path)
            if text:
                word_count = count_words(text)
                print(f"The text in the file contains {word_count} words.")
        
        elif choice == '3':
            print("Exiting the program. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please try again.")
        
        print("\nDo you want to input more text?")
        cont = input("Enter 'yes' to continue or any other key to exit: ")
        if cont.lower() != 'yes':
            print("Thank you for using the Word Counting Program. Goodbye!")
            break

if __name__ == "__main__":
    main()
