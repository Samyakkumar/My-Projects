alphabets = dict()

for i in range(97, 123):
	alphabets[chr(i)] = 0

text = input("Enter the text")

for word in text.split(' '):
	for letter in word:
		if letter.isalpha():
			alphabets[letter.lower()] += 1

print(alphabets)
