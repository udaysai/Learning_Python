
"""This is the mc module.
This is a docstring for the module.

>>> m = Markov('ab')
>>> m.predict('a')
'b'

"""
import argparse
import random
import sys
import urllib.request as req


def fetch_url(url: str, fname: str):
    """Read data from a url and write to fname
    """
    fin = req.urlopen(url)
    data = fin.read()
    fout = open(fname, mode='wb')
    fout.write(data)
    fout.close()


def from_file(fname, size):
    fin = open(fname, mode='r', encoding='utf8')
    txt = fin.read()
    return Markov(txt, size)


class Markov:
    def __init__(self, txt, size=1):  # !!!#
        # self.table = get_table(txt)
        self.tables = []
        for i in range(1, 1 + size):
            self.tables.append(get_table(txt, size=i))

    def predict(self, txt):
        """
        >>> m = Markov('abc')
        >>> m.predict('b')
        'c'
        """
        # options = self.table.get(txt, {})
        table = self.tables[len(txt) - 1]  # !!!
        options = table.get(txt, {})  # !!!
        if not options:
            raise KeyError(f'{txt} not found')
        possibles = []
        for char in options:
            for i in range(options[char]):
                possibles.append(char)
        return random.choice(possibles)


def get_table(txt, size=1):  # !!!
    """
    This is the function docstring.
    >>> get_table('ab')
    {'a': {'b': 1}}
    """
    results = {}
    for i in range(len(txt)):
        chars = txt[i:i + size]  # !!!
        try:
            dst = txt[i + size]  # !!
        except IndexError:
            break
        char_dict = results.get(chars, {})  # !!!
        char_dict.setdefault(dst, 0)
        char_dict[dst] += 1
        results[chars] = char_dict  # !!!
    return results


def repl(m):
    print('Welcome to the REPL!')
    print('Hit ctl-C to exit')
    while True:
        try:
            txt = input('> ')
        except KeyboardInterrupt:
            print('Goodbye!')
            break
        try:
            res = m.predict(txt)
        except IndexError:
            print('Too long try again')
        except KeyError:
            print('Not found, try again')
        else:  # if no exception
            print(res)


def main(args):
    ap = argparse.ArgumentParser()
    ap.add_argument('-f', '--file', help='file to load')
    ap.add_argument('-s', '--size', help='Markov size (default 1)',
                    default=1, type=int)
    opt = ap.parse_args(args)
    if opt.file:
        m = from_file(opt.file, size=opt.size)
        repl(m)


if __name__ == '__main__':
    # m = from_file('pp.txt', 4)
    # repl(m)
    main(sys.argv[1:])
else:
    print('loading as library')


