'''
1.Write a  Python program that accepts the users first and last name and prints them in reverse order with a space between them.



name = input('give me your name: ')
last_name = input('give your lastname: ')


full_name = name + ' ' + last_name

print(f'your name is {full_name}')
print(f'here is what you asked for {last_name + " " + name}')



2.  Write a  Python function that takes a sequence of numbers and determines 
whether all the numbers are different from each other.





n_numbers = int(input('how many numbers would you like to add?: '))

nlist = []

while len(nlist) < n_numbers:
    number = int(input('add a number: '))
    nlist.append(number)

nlist.sort()
print(nlist)

ocurrences = []
prev_num = None
max_occur = 0

for n in nlist:
    if n == prev_num:
        max_occur += 1
    else:
        max_occur = 1
    if max_occur == 2:
        ocurrences.append(n)
    prev_num = n

print(f'we found the following occurrences {ocurrences}')



3.  Write a Python program that removes and prints every
 third number from a list of numbers until the list is empty.




n_numbers = int(input('how many numbers would you like to add?: '))

nlist = []

while len(nlist) < n_numbers:
    number = int(input('add a number: '))
    nlist.append(number)

while len(nlist) > 2:
    print(nlist[2])
    nlist.remove(nlist[2])



4.Find unique triplets whose three elements gives the sum of zero from an array of n integers




n_numbers = int(input('how many numbers would you like to add?: '))

t1 = []

while len(t1) < n_numbers:
    number = int(input('add a number: '))
    t1.append(number)


triplets = 0

while len(t1) >= 3:  # Corrected the loop condition
    if t1[0] + t1[1] + t1[2] == 0:
        triplets += 1
    t1.remove(t1[0])  # Corrected the syntax for removing the first element

print(f'We found {triplets} triplets')


5. Write a Python program to make combinations of 3 digits.



import random

t1 = []

while len(t1) < 3:
    number = int(input('add a number: '))
    t1.append(number)

print(t1)

choice = []

while len(t1) != 0:
    option = random.choice(t1)
    choice.append(option)
    t1.remove(option)  # Corrected the removal of the chosen option

# Convert the integers in choice to strings before joining
fulln = "".join(str(num) for num in choice)

print(f'tu numero es {fulln}')


6. Write a  Python program that prints long text, converts it to a list,
 and prints all the words and the frequency of each word.


long_text = """She swore she met a planet who looked suspiciously like her. And then she saw a planet that was, well… she wasn’t sure. One planet she discovered, had grown forests made of green. Another one was very shy, not fond of being seen. She flew right by a planet, that was frozen icy cold. And then she saw a planet that was made of jewels and gold! She had started to notice that each planet seemed brighter than the last. They were all so different and all so pretty. It became hard for her to decide where to go next. If each planet she visited was more beautiful than the one before it, then how could she decide which way to go next, and how could she decide where to stay. So she continued traveling, afraid to miss a single planet. Eventually she came upon the big blue planet that she had once circled, but she found that is was not the same. It was shining in a way that it never had before. It was more blue than it had ever been, and certainly more beautiful. This made her stop for a moment. “I do not know where I should go next” she said out loud. “Each direction is filled with wonderful planets. And I cannot stop, knowing that the next planet will be even more beautiful if I continue on. Even my big blue planet has grown more beautiful every day in my absence.” The big blue planet overheard this. “Can you not see why I am brighter?" it asked. "You are the brightest planet I have ever seen," she said, "but I do not know why you glow brighter today than you did when I left you." “You have brightened me,” it said. “But I am just a rock” she replied. “You are no longer just a rock like the day you left me,” said the big blue planet. “You have grown bold and bright. Now you are a shooting star, and you are the reason that I shine. And while you are worrying about which direction to go, all of the planets in space are hoping that you will come their way to brighten them.” And so the shooting star, who was no longer just a rock, finally understood. It did not matter where she went, the light was her own. So the rock sat there for a moment, by the bright blue planet and wondered."Should I keep traveling, or should I fly around the big blue planet and grow brighter with it each day.”She thought, until she knew exactly what to do."""

# Remove commas, periods, double quotes, and curly quotes from the text
cleaned_text = long_text.replace(",", "").replace(".", "").replace('"', '').replace('“', '').replace('”', '').replace('…', '')

# Convert the text to lowercase
cleaned_text = cleaned_text.lower()

# Split the text into words
word_list = cleaned_text.split()

word_list.sort()

word_dict = {}
while len(word_list) != 0:
    key = word_list[0]
    counter = 0
    for word in word_list:
        if word == key:
            counter += 1
    word_dict.update({key: counter})
    word_list = [word for word in word_list if word != key]  # Remove all occurrences of the current word from the list


for key, value in word_dict.items():
    print(key, ':', value)



7.Write a  Python program to find the median among three given numbers.
 '''

import math
a = int(input("what's the lenght of the first side? :"))
b = int(input("what's the lenght of the second side? :"))

c = (a*a)+(b*b)

print(f'the lenght of the side is equal to {math.sqrt(c)}')
