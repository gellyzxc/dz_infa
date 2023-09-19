letters = {
    'A': 10,
    'B': 11,
    'C': 12,
    'D': 13,
    'E': 14,
    'F': 15
}
lettersReverseOrder = {
    10: 'A',
    11: 'B',
    12: 'C',
    13: 'D',
    14: 'E',
    15: 'F'
}

def main():
    number = str(input('Число '))
    firstBase = int(input('Основание сс числа '))
    secondBase = int(input('Основание сс в которую нужно перевести '))
    inTen = toTen(number=number, base=firstBase)
    print(fromTen(number=inTen, base=secondBase))

def fromTen(number, base):
    result = ''
    intPart = int(number)
    num = int(number)
    
    while intPart>=base:
        num = intPart
        intPart = num // base
        if (num % base >= 10):
            result+=lettersReverseOrder[num%base]
        else:
            result+=str(num % base)
            
    result+=str(intPart % base)    
    return result[::-1]


def toTen(number, base):       
    number = number[::-1]
    result = 0
    for i in range(len(number)):
        if (number[i].isalpha()):
            result+=int(letters[number[i]]) * base**i
        else:
            result+= int(number[i]) * base**i
        
    return result


if __name__ == "__main__":
    main()