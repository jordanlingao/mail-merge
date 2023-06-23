# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".
    
# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("Input/Letters/starting_letter.txt", "w") as starting_letter_file:
    starting_letter_file.write("Dear [name],\n\n"
                               "You are invited to my birthday this Saturday.\n\n"
                               "Hope you can make it!\n\n"
                               "Jordan")

with open("Input/Letters/starting_letter.txt") as starting_letter_file:
    starting_letter = starting_letter_file.read()

with open('Input/Names/invited_names.txt') as names_file:
    names = names_file.read().split()

for name in names:
    with open(f'Output/ReadyToSend/letter_for_{name}.txt', "w") as new_letter_file:
        new_letter_file.write(starting_letter.replace('[name]', name))
