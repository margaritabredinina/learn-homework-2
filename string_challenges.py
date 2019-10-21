# Вывести последнюю букву в слове 
word = 'Архангельск' 
print(word[-1])

# Вывести количество букв "а" в слове
word = 'Архангельск'.lower() 
letter_a = 0
for letter in word:
    if letter == 'а':
       letter_a += 1
    else:
       letter_a 
print(letter_a)

# Вывести количество гласных букв в слове 
word = 'Архангельск'.lower()
letter_a = 0
for letter in word:
    if letter in ['а','у','е','ы','о','э','я','и','ю']:
        letter_a += 1
    else:
        letter_a
print(letter_a)
     
 # Вывести количество слов в предложении 
sentence = 'Мы приехали в гости'.split() 
print(len(sentence))
  
 # Вывести первую букву каждого слова на отдельной строке 
sentence = 'Мы приехали в гости'.split()
for word in range(len(sentence)):
    print(sentence[word][0])
    
# Вывести усреднённую длину слова. 
sentence = 'Мы приехали в гости'.split()
len_word = 0
for word in range(len(sentence)):
    len_word += (len(sentence[word]))
avg_word = len_word / len(sentence)
print(avg_word)