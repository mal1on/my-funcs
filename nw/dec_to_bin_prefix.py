def binary_prefix(prefix):
    return ''.join(format(o, '08b') for o in map(int, prefix.split('.')))
