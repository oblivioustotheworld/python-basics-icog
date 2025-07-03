def analyzer(txt):
    # Counters
    count_whitespace = 0
    count_char = 0

    # Convert all text to lowercase to normalize words like "Python" and "python"
    txt = txt.lower()

    # Split the sentence into a list of words
    words = txt.split()

    # Count words
    count_words = len(words)

    # Count characters and whitespaces
    for char in txt:
        if char == ' ':
            count_whitespace += 1
        else:
            count_char += 1

    # Word frequency dictionary
    frequency = {}

    for word in words:
        frequency[word] = frequency.get(word, 0) + 1

    # Find the most common word
    most_common = max(frequency, key=frequency.get)

    # Output
    print("\n📊 Text Analysis Results")
    print("--------------------------")
    print("Words List: ", words)
    print("Total Words:", count_words)
    print("Total Characters (excluding spaces):", count_char)
    print("Total Whitespaces:", count_whitespace)
    print("Word Frequencies:", frequency)
    print("Most Common Word:", most_common)

# Ask for user input
txt = input("Enter a sentence: ")
analyzer(txt)
