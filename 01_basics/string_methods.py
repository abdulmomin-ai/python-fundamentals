# String Basics 

name = "Python"
print("First Character:", name[0])  
print("Last Character:", name[-1]) 


# String Slicing
text = "Computer"
print(text[0:3])   
print(text[3:])    
print(text[:5])    
print(text[::-1])  # Reverse string


 
# Case Conversion
msg = "Python IS FuN"
print("Lowercase:", msg.lower())
print("Uppercase:", msg.upper())
print("Title case:", msg.title())
print("Capitalized:", msg.capitalize())


# Whitespace Handling
text = "   Hello   "
print("Strip:", text.strip())     
print("Left Strip:", text.lstrip())    
print("Right Strip:", text.rstrip())    



# Replace and Split
sentence = "I love dog"
print(sentence.replace("dog", "Programming"))

data = "apple,banana,grapes"
print("Split Data:", data.split(","))



# Join
items = ["Ali", "Momin", "Zain"]
print("Joined Names:", "-".join(items))


# Ends with / Start with
email = "user@gmail.com"
print("Ends with .com:", email.endswith(".com"))
name = "abdul"
print("Start with Abdul:", name.startswith("abdul"))



# Find and Count
msg = "bananaaaaa"
print("Index of na:", msg.find("na"))  
print("Count of a:", msg.count("a"))


# Validation Methods
text1 = "123"
text2 = "abc"
text3 = "abc123"
print(text1.isdigit())
print(text2.isalpha())
print(text3.isalnum())



# Palindrome Check
word = "level"
if word == word[::-1]:
    print("Palindrome")
else:
    print("Not palindrome")
    


# Count Vowels
text = "Programming"
vowels = "aeiouAEIOU"
count = 0
for char in text:
    if char in vowels:
        count += 1        
print("Vowels:", count)



# Clean Special Characters
import string

text = "He@ll#o!!"
clean = ""
for char in text:
    if char not in string.punctuation:  # Special characters in string.punctuation
        clean += char
print(clean)



# Remove spaces from string
text = input("Enter text: ")
clean = text.replace(" ", "")
print("Without spaces:", clean)






































