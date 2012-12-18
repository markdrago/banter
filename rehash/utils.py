def combine_url_components(*args):
    pieces = []
    for arg in args:
        while arg[-1:] == '/':
            arg = arg[:-1]

        while arg[:1] == '/':
            arg = arg[1:]

        pieces.append(arg)

    return '/'.join(pieces)
