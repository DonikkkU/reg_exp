#1
import re
str1 = 'KDeoALOklOOHserfLoAJSIskdsf'
print("string:")
print(str1)
print("result:")
remove_lower = lambda text: re.sub('[a-z]', '', text)
result = remove_lower(str1)
print(result)
#2
string = 'w3schools.com'
print('string:', string)
print('result:')
clean_string = re.sub('\w+','', string)
print(clean_string)

#3
s ='clearly, he has no excuse for such behavior'
print(re.findall(r'\b(\w+ly)\b',s))
#4
str_value = 'PythonTutorialAndExercises'
word_list = re.findall(r'[A-Z]?[^A-Z]*',str_value)
print(word_list)
#5
string_value = '**//Python Exercises// - 12.'
s = re.sub(r'[^a-zA-Z0-9]', '', string_value)
print(s)
