def intToInternational(n):
    s = ''
    a = str(n)
    numbers= {
        0: '',
        1: 'one',
        2: 'two',
        3: 'three',
        4: 'four',
        5: 'five',
        6: 'six',
        7: 'seven',
        8: 'eight',
        9: 'nine'
    }
    morphemes = {
        1: '',
        2: 'thousand ',
        3: 'million ',
        4: 'billion ',
        5: 'trillion ',
        6: 'quadrillion ',
        7: 'quintillion '
    }
    tens = ['', ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen'], 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
    if len(a) % 3 != 0:
        a = '0' * ((3 - len(a) % 3)) + a
    div = ''
    l = []
    for i in range(len(a)):
        if (i + 1) % 3 == 0:
            div += a[i]
            l.append(div)
            div = ''
            continue
        div += a[i]

    for k in range(len(l)):
        i = []        
        for un in l[k]:
            i.append(int(un))
        three = ''
        for j in range(3):
            if i[j] == 0:
                three += ' '
                continue
            if j == 0:
                three += numbers[i[j]] + ' hundred '
            if j == 1:
                if i[j] == 1:
                    three += tens[1][i[j + 1]] + ' '
                    break
                else:
                    three += tens[i[j]] + ' '
            if j == 2:
                three += numbers[i[j]] + ' '
            
        s += three + morphemes[len(l) - k]
    
    return s

a = (14142641234539456712)
print(a, '\n', intToInternational(a))