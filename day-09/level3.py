person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

# Check if 'skills' key exists
if 'skills' in person:
    skills = person['skills']

    # Print the middle skill
    middle = len(skills) // 2
    print("Middle skill:", skills[middle])

    # Check if Python is a skill
    if 'Python' in skills:
        print("Python skill: Yes")
    else:
        print("Python skill: No")

    # Check developer type
    if skills == ['JavaScript', 'React']:
        print("He is a front end developer")
    elif all(skill in skills for skill in ['Node', 'Python', 'MongoDB']):
        print("He is a backend developer")
    elif all(skill in skills for skill in ['React', 'Node', 'MongoDB']):
        print("He is a fullstack developer")
    else:
        print("Unknown title")

# Check marital status and country
if person['is_married'] and person['country'] == 'Finland':
    print(
        f"{person['first_name']} {person['last_name']} lives in "
        f"{person['country']}. He is married."
    )