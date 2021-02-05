import json

def write_json(name, age, filename = 'Json test/test.json'):
    with open (filename) as json_file:
        data = json.load(json_file)
        temp = data['pet']
        y = {'name': name, 'age': age}
        temp.append(y)

    with open (filename, 'w') as f:
        json.dump(data, f, indent = 4)

run = True
while run:
    name = input('\nName: ')
    age = int(input('\nAge: '))

    inp = input('\nContinue? ')
    if inp == '1':
        pass
    elif inp == '0':
        run = False

    write_json(name, age)