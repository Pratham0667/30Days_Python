age = [22, 19, 24, 25, 26, 24, 25, 24]

new_age = set(age)
length_List  = len(age)
Length_set = len(new_age)

print(f"THE AGE IN LIST : {age}")
print(f"THE AGE IN SET : {new_age}")

if length_List > Length_set:
    print("List is bigger.")
elif Length_set > length_List:
    print("Set is bigger.")
else:
    print("Both have the same length.")


# String : Immutable sequence of characters.
# List   : Mutable ordered collection.
# Tuple  : Immutable ordered collection.
# Set    : Mutable unordered collection with unique elements.

sentence = "I am a teacher and I love to inspire and teach people."

words = sentence.split()
unique_words = set(words)

print("Unique words:", unique_words)
print("Number of unique words:", len(unique_words))




