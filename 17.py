words = {
    1:'one',
    2:'two',
    3:'three',
    4:'four',
    5:'five',
    6:'six',
    7:'seven',
    8:'eight',
    9:'nine',
    10:'ten',
    11:'eleven',
    12:'twelve',
    13:'thirteen',
    14:'fourteen',
    15:'fifteen',
    16:'sixteen',
    17:'seventeen',
    18:'eighteen',
    19:'nineteen',
    20:'twenty',
    30:'thirty',
    40:'forty',
    50:'fifty',
    60:'sixty',
    70:'seventy',
    80:'eighty',
    90:'ninety',
}

hundred = "{0} hundred"
hundreds = "{0} hundred and {1}"
thousand = "one thousand"

def to_word(num):
    if num in words:
        return words[num]
    elif num < 100:
        tens = (num/10)*10
        return words[tens]+" "+words[num%tens]
    elif num < 1000:
        i = num%100
        if i == 0:
            return hundred.format(to_word(num/100))
        return hundreds.format(words[num/100], to_word(i))
    else:
        return thousand
        
count = 0
stop = 0
for i in xrange(1, 1001):
    try:
        w = to_word(i)
        print w
        stop += 1
        if stop == 9:
            #raw_input("Press enter to continue")
            stop = 0
        count += len(w.replace(' ', ''))
    except:
        print "Failed on", i
        raise
    
print count