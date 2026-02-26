# 1. String Concatenation

string1 = "Hello "
name = input("Enter your Name: ")

# Concatenate string1 and name
result = string1 + name
print(result)

# Add third string
string3 = ", welcome to Python programming"
result = result + string3
print(result)
# 2. String Slicing and Indexing

print("\n--- String Slicing and Indexing ---")

# Using previously concatenated string
full_string = result

# a. First character
print("First character:", full_string[0])

# b. Last character
print("Last character:", full_string[-1])

# c. First 5 characters
print("First 5 characters:", full_string[:5])

# d. Last 11 characters
print("Last 11 characters:", full_string[-11:])

# e. Reverse string
print("Reversed string:", full_string[::-1])

# f. Print the word 'Python'
start_index = full_string.find("Python")
end_index = start_index + len("Python")
print("Word 'Python':", full_string[start_index:end_index])
# 3. String Methods

print("\n--- String Methods ---")

strM = "Python beginner tutorial"

# a. Uppercase
print("Uppercase:", strM.upper())

# b. Lowercase
print("Lowercase:", strM.lower())

# c. Capitalize
print("Capitalized:", strM.capitalize())

# d. Count occurrences of 't'
print("Count of 't':", strM.count('t'))

# e. Replace 'Python' with 'Machine Learning'
print("Replaced String:", strM.replace("Python", "Machine Learning"))
# 4. Tuples

print("\n--- Tuples ---")

tuple1 = (10, 20, 30)
tuple2 = (40, 50, 60)

# a. Concatenate tuples
t_combine = tuple1 + tuple2
print("Concatenated Tuple:", t_combine)

# b. Repeat tuple 3 times
print("Repeated Tuple:", t_combine * 3)

# c. Access 3rd element
print("3rd Element:", t_combine[2])

# d. First three elements
print("First 3 Elements:", t_combine[:3])

# e. Last three elements
print("Last 3 Elements:", t_combine[-3:])
