'''
>>> marked_uuid('123e4567-e89b-12d3-a456-426614174000', 'hello')
'4e110567-e89b-42d3-a456-426614174000'

>>> marked_uuid('123e4567-e89b-12d3-a456-426614174000', 'hello this is a message with spaces')
'4e110174-5115-413e-aa6e-3174159ace50'

>>> marked_uuid('123e4567-e89b-12d3-a456-426614174000', 'synthetic')
'57274e71-e89b-42d3-a456-426614174000'

>>> marked_uuid('123e4567-e89b-12d3-a456-426614174000', 'SYNTHETIC')
'57274e71-e89b-42d3-a456-426614174000'

>>> marked_uuid('123e4567-e89b-12d3-a456-426614174000', '11111111')
'11111111-e89b-42d3-a456-426614174000'

>>> marked_uuid('123e4567-e89b-12d3-a456-426614174000', '11111111111111111111111111111111111111111111111111111too many1')
'11111111-1111-4111-a111-111111111111'
'''

from hexican import in_hexican

def marked_uuid(unmarked_uuid, word):
    '''returns a uuid with definable watermark in Hexican, the hexidecimal alphabet'''
    s = list(in_hexican(word) + unmarked_uuid[len(word):])
    s[8] = '-'
    s[13] = '-'
    s[14] = '4'
    s[18] = '-'
    s[19] = 'a'
    s[23] = '-'
    return "".join(s)[:36]


if __name__ == '__main__':
    import doctest
    doctest.testmod()

