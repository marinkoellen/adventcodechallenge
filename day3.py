text_file = open("day3_input.txt",'r').read().split('\n')
print(len(text_file))
if "" in str(text_file):
    text_file.remove("")

