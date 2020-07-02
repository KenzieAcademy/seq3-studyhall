"""Prints a nicely-formatted summary of the name and attributes
of an HTML tag.
"""

import re


def get_atts(s):
    """Returns a dictionary of attribute names and their values."""
    return {n: v for n, v in [att.split('=') for att in s.strip().split()]}


def tag_summary(parts):
    """Prints a breakdown of an HTML tag."""
    print(f'Tag: {parts[0]}')
    if parts[1]:
        print('Attrs:')
        atts = get_atts(parts[1])
        for n, v in atts.items():
            print(f'\t{n}: {v}')
    if parts[2]:
        print('Body:')
        print(f'\t{parts[2]}')


def main():
    pattern = r'<([a-z0-9]+)([^<]+)*(?:>(.*)<\/\1>|\s+\/>)'
    match = re.search(pattern, '<img src="images/py.jpg" />')
    tag_summary(match.groups())


if __name__ == '__main__':
    main()
