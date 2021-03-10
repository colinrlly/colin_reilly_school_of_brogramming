cool_stuff = [
    {
        'name': 'jose',
        'other': 'jose',
    },
    {
        'name': 'harper',
        'other': 'jose',
    },
    {
        'name': 'jose',
        'other': 'jose',
    },
    {
        'name': 'harper',
        'other': 'jose',
    },
]

comprehend = [x['name'] for x in cool_stuff]

print(comprehend)

stuff = []
for x in cool_stuff:
     stuff.append(x['name'])

operators = ['+', '-', '*']

word = '4+3'

print([(word.split(o), o) for o in operators if o in word][0])
