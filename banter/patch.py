import re

def clean(patch):
    patch = re.sub(r'^--- a\/', '--- ', patch, flags=re.MULTILINE)
    patch = re.sub(r'^\+\+\+ b\/', '+++ ', patch, flags=re.MULTILINE)
    return patch
