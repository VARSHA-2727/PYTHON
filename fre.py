def display_first_N_lines (file_name,N):
 with open(file_name,'r') as file:
    for i  in range (N):
        line=file.readline(). strip()
        if line:
            print(line)
        else:
            print("End of the file reached")
            break
def find_word_frequency (file_name, word):
    with open(file_name, 'r') as file:
        content = file.read()
        word_count = content.lower().Count(word.lower())
        print(f" The word '{ word}'occurs{word_count}times in the file")
file_name=input("EnTER  the file name")
N=int(input("Enter the number of lines to display"))
print("first n lines of the file:")
display_first_N_lines(file_name,N)
word=input("Enter the lord to find its frequeny?")
find_word_frequency(file_name,word)
