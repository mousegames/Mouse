main = []

while True:
    line = input('')
    if line == 'add:':
        main.append(input(''))
    elif line == 'delete:':
        main.pop(int(input('')))
    elif line == 'pr:':
        print(f'---{main[int(input(''))]}---')
    elif line == 'if:':
        if main[int(input(''))] == input(''): 
                print('---True---')
        else:
            print('---False---')
    elif line == 'count:':
        for i in range(int(input(''))):
            print(f'---{i}---')
    elif line == 'EXIT':
        exit = input('do you want to exit y/n ')
        if exit == 'y':
             break
        