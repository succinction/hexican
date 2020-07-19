'''
>>> _hexicon()
{'a': 'a', 'b': 'b', 'c': 'c', 'd': 'd', 'e': 'e', 'f': 'f', 'g': '6', 'h': '4', 'i': '1', 'j': '1', 'k': '4', 'l': '1', 'm': '3', 'n': '2', 'o': '0', 'p': '9', 'q': '6', 'r': '2', 's': '5', 't': '7', 'u': '2', 'v': '7', 'w': '3', 'x': '8', 'y': '7', 'z': '2', ' ': '1', '0': '0', '1': '1', '2': '2', '3': '3', '4': '4', '5': '5', '6': '6', '7': '7', '8': '8', '9': '9'}

>>> in_hexican('word')
'302d'

>>> in_hexican('hello')
'4e110'

>>> in_hexican('hello spaces')
'4e110159ace5'

>>> in_hexican('hello spaces AND UPPER')
'4e110159ace51a2d1299e2'

>>> in_hexican('not in lexicon !@#@#$%#$%^')
'not in lexicon !@#@#$%#$%^'
'''

def _hexicon():
    '''returns a hex letter alphabet dictionary'''
    # 0123456789abcdef # hex alphabet
    return dict(zip(list('abcdefghijklmnopqrstuvwxyz 0123456789'), 
                    list('abcdef6411413209625727387210123456789')))

def in_hexican(word):
    '''returns a word transformed into a hex letter alphabet'''
    hexicon = _hexicon()
    new_word = ''
    try:
        for L in word.lower():
            new_word = new_word + hexicon[L]
    except:
        new_word = word.lower()
    return new_word


if __name__ == '__main__':
    import doctest
    doctest.testmod()

