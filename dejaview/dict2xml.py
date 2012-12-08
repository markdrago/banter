def dict2xml(d, pretty=False, indent=0):
    accumulator = ''
    for key in d.keys():
        if pretty:
            if indent != 0:
                accumulator += "\n" + (" " * indent)
            elif accumulator != '':
                accumulator += "\n"

        accumulator += '<%s>' % (key,)

        if isinstance(d[key], dict):
            accumulator += dict2xml(d[key], pretty, indent + 4)
            if pretty:
                accumulator += "\n"
        else:
            accumulator += str(d[key])

        accumulator += '</%s>' % (key,)
    return accumulator
