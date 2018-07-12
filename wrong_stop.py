# find disorderly commas and dots!
import glob, os
import string


# def find_tex():
#     tex_files = []
#     for file in glob.glob('*.tex'):
#         tex_files.append(file)
#     return tex_files

def find_footnote(filename):

    words = []
    footnotes = [] 
    line_number_list = []

    for line_number, line in enumerate(input_file, 1):
        split_lines = line.split()

        for word in split_lines:
            if word != "'\n'":
                lowercase_word = word.lower()
                words.append(lowercase_word)
                line_number_list.append(line_number)

    word_number = 1
    previous_word = None
    for i in range(len(words)):

        if i == len(words) - 1:
            break
        # modify the following, how can you find the \footnote{} substrings?
        if "footnote{" in word in words:
            print("footnote found! Appended in 'footnotes'.")
            # footnotes.append([line_number_list[i], words[i]])
            previous_word = words[i]

        else:
            previous_word = words[i]

        word_number += 1

    print(footnotes)
    '\n'

    # print("Footnote list")
    # print("[line, word number]")
    # for k in footnotes:
    #     print(k)


if __name__ == '__main__':
    input_file = open("test_text.tex", 'r')
    find_footnote(input_file)    

# if __name__ == '__main__':
    
#     os.chdir('/home/ana/thesis')
#     for file in find_tex():
#         print(file)
#         input_file = open(file, 'r')
#         find_footnote(input_file)