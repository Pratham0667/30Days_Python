len_py = len("python")
len_dr = len("dragon")

print(len_py is not len_dr)

print( "on"in "python")

string = "I hope this course is not full of jargon"

print("jargon" in  string)

check_dragon = "on" not in "dragon"
check_python = "on" not in "python"

both_dont_have_it = ("on" not in "dragon") and ("on" not in "python")

print(f"Is 'on' missing from dragon? {check_dragon}")
print(f"Is 'on' missing from python? {check_python}")
print(f"Statement 'There is no on in both': {both_dont_have_it}")