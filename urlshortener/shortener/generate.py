from random import choice

from string import ascii_letters, digits

CHARS = ascii_letters + digits
def rand_string(chars = CHARS):
    return ''.join([choice(chars) for _ in range(9)])

def shorten(class_object):
    str1 = rand_string()
    
    model_class = class_object.__class__
    
    if model_class.objects.filter(short_url = str1).exists():
        return shorten(class_object)
    
    return str1