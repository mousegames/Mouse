main = []

while True:
    line = input('')
    if line == 'add: s':
        main.append(input(''))
    elif line == 'add: b':
        main.append(bool(input('')))
    elif line == 'add: i':
        main.append(int(input('')))
    elif line == 'add: f':
         main.append(float(input('')))
    elif line == 'add:':
            add = main[int(input(''))] + main[int(input(''))]
            print(f'---{add}---')
    elif line == 'mult:':
        mult = main[int(input(''))] * main[int(input(''))]
        print(f'---{mult}---')
    elif line == 'sub:':
        sub = main[int(input(''))] - main[int(input(''))]
        print(f'---{sub}---')
    elif line == 'div:':
        div = main[int(input(''))] / main[int(input(''))]
        print(f'---{div}---')
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
        
