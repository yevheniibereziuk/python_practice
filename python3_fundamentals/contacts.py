contacts = {
    'number': 4,
    'students':
        [
            {'name':'Sarah Holderness', 'email':'sarah@gmail.com'},
            {'name':'Harry Swin', 'email':'harry@gmail.com'},
            {'name':'Hermione Gringer', 'email':'hermione@gmail.com'},
            {'name':'Ron Weakly', 'email':'ron@gmail.com'}
        ]
}

print('Student emails:')
for student in contacts['students']:
    print(student['email'])