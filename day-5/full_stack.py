# Join the following lists:
# front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
# back_end = ['Node','Express', 'MongoDB']
# After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack, then insert Python and SQL after Redux.

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
print(f"THE FRONT END LIST : \n {front_end}")
back_end = ['Node','Express', 'MongoDB']
print(f"THE BACK END LIST : \n {back_end}")

full_stack = front_end + back_end

print(f"THE FULL STACK  LIST : \n {full_stack}")
full_stack.insert(5 , "python")
full_stack.insert(6, "SQL")

print(f"THE  FINAL FULL STACK  LIST : \n {full_stack}")

