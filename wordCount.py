#!/usr/bin/env python3


import sys        # command line arguments
import re         # regular expression tools
import os         # checking if file exists
import subprocess # executing program

def count_words(input_file):
    word_counts = {}
    with open(input_file, 'r') as file:
        text = file.read().lower()  # Convert the text to lowercase for consistent processing

    # Replace hyphens and apostrophes with spaces
    modified_text = text.replace("-", " ").replace("'", " ")

    # Use regex to find words in the modified text
    words = re.findall(r'\b\w+\b', modified_text)

    # Count each word
    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1

    return word_counts

def write_output(word_counts, output_file):
    # Write the word counts to the output file
    with open(output_file, 'w') as file:
        for word, count in sorted(word_counts.items()):
            file.write(f"{word} {count}\n")

def main():

    # set input and output files
    if len(sys.argv) !=  3:
        print("Correct usage: wordCount.py <input text file> <output text file>")
        exit()

    inputFname = sys.argv[1]
    outputFname = sys.argv[2]

    #make sure text files exist
    if not os.path.exists(inputFname):
        print ("Text file input %s doesn't exist! Exiting" % inputFname)
        exit()

    #make sure text files exist
    if not os.path.exists(outputFname):
        print ("Text file output %s doesn't exist! Exiting" % outputFname)
        exit()

    # Count words in the input file
    word_counts = count_words(inputFname)

    # Write the counts to the output file
    write_output(word_counts, outputFname)
    print(f"Word counts written to {outputFname}")

if __name__ == "__main__":
    main()


