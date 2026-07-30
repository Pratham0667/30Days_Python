#Write a function which count number of lines and number of words in a text. All the files are in the data the folder:
#Read obama_speech.txt file and count number of lines and words
#Read michelle_obama_speech.txt file and count number of lines and words
#Read donald_speech.txt file and count number of lines and words
#Read melina_trump_speech.txt file and count number of lines and words

import os

def count_lines_and_words(filename, folder="data"):
    file_path = os.path.join(folder, filename)
    
    line_count = 0
    word_count = 0
    
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                line_count += 1
                words = line.split()
                word_count += len(words)
                
        return line_count, word_count
    
    except FileNotFoundError:
        return f"Error: The file '{filename}' was not found in the '{folder}' folder."
    except Exception as e:
        return f"An error occurred: {e}"

speech_files = [
    "obama_speech.txt",
    "michelle_obama_speech.txt",
    "donald_speech.txt",
    "melina_trump_speech.txt"
]


print(f"{'File':<30} | {'Lines':<10} | {'Words':<10}")
print("-" * 55)

for file_name in speech_files:
    result = count_lines_and_words(file_name)
    
    if isinstance(result, tuple):
        lines, words = result
        print(f"{file_name:<30} | {lines:<10} | {words:<10}")
    else:
        print(f"{file_name:<30} | {result}")   
