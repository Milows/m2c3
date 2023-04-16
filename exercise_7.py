#Get the first word from your string using indexes. 
#Use the upper function to transform the letters into uppercase. 
#Create a new string that takes the uppercase word and the rest of the original string.

sentence = 'The quick brown fox jumped over the lazy dog.'
first_word = sentence[:3].upper()
new_sentence = first_word + sentence[3:]
print(new_sentence)
