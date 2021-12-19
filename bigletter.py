letters = {
    ' ' : ['   ', '   ', '   ', '   ', '   '],
    'a' : ['****', '*  *', '****', '*  *', '*  *'],
    'b' : ['****', '*  *', '*** ', '*  *', '****'],
    'c' : [' ***', '*   ', '*   ', '*   ', ' ***'],
    'd' : ['*** ', '*  *', '*  *', '*  *', '*** '],
    'e' : ['****', '*   ', '*** ', '*   ', '****'],
    'f' : ['****', '*   ', '*** ', '*   ', '*   '],
    'g' : [' ** ', '*   ', '*   ', '*  *', ' ** '],
    'h' : ['*  *', '*  *', '****', '*  *', '*  *'],
    'i' : ['****', '  * ', '  * ', '  * ', '****'],
    'j' : ['****', '  * ', '  * ', '* * ', ' *  '],
    'k' : ['*  *', '* * ', '**  ', '* * ', '*  *'],
    'l' : ['*   ', '*   ', '*   ', '*   ', '****'],
    'm' : ['*   *', '** **', '* * *', '*   *', '*   *'],
    'n' : ['*   *', '**  *', '* * *', '*  **', '*   *'],
    'o' : [' ** ', '*  *', '*  *', '*  *', ' ** '],
    'p' : ['****', '*  *', '*** ', '*   ', '*   '],
    'q' : [' ** ', '*  *', '*  *', ' ** ', '   *'],
    'r' : ['****', '*  *', '*** ', '*  *', '*  *'],
    's' : [' ***', '*   ', ' ** ', '   *', '*** '],
    't' : ['****', '  * ', '  * ', '  * ', '  * '],
    'u' : ['*  *', '*  *', '*  *', '*  *', ' ** '],
    'v' : ['*  *', '*  *', '* * ', '**  ', '*   '],
    'w' : ['*   *', '*   *', '* * *', '* * *', ' * * '],
    'x' : ['*   *', ' * * ', '  *  ', ' * * ', '*   *'],
    'y' : ['*   *', ' * * ', '  *  ', '  *  ', '  *  '],
    'z' : ['*****', '   * ', '  *  ', ' *   ', '*****'],
    '/' : ['    *', '   * ', '  *  ', ' *   ', '*    '],
    '?' : [' ** ', '*  *', '  * ', '    ', '  * '],
    '.' : ['    ', '    ', '    ', '    ', ' *  '],
    ',' : ['    ', '    ', '    ', '  * ', ' *  ']

}
string = input('Entré: ')
denoter = input('Enter le symbol: ')
empty_space = input('Enter l\'empty space: ')
if not denoter:
    denoter = '*'
if not empty_space:
    empty_space = ' '
for i in range(5):
    for j in string:
        print(letters[j.lower()][i].replace('*', denoter).replace(' ', empty_space), end = empty_space)
    print()