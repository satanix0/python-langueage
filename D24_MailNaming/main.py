# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the   with the actual name.
# Save the letters in the folder "ReadyToSend".

PLACEHOLDER = '[name]'


f1 = open('Projects/D24_MailNaming/Input/Names/invited_names.txt','r')
for line in f1:
    names = f1.read().split("\n")


f2 = open('Projects/D24_MailNaming/Input/Letters/starting_letter.txt','r')
letter = f2.read()
for name in names:
    new_mails = letter.replace(PLACEHOLDER, name)
    f3 = open(f'Projects/D24_MailNaming/Output/ReadyToSend/{name}.txt','w')
    f3.write(new_mails)


print("Letters Sent Successfully!!")
