from io import StringIO
import pathlib


def print_lines(fname, print_limit=10, skip_rows=0, encoding='utf-8'):
    lines = StringIO()
    with open(fname, 'r', encoding=encoding) as f_in:
        for _ in range(skip_rows):
            next(f_in)
        print_limit = print_limit
        for line in f_in:
            lines.write(line)
            print_limit -= 1
            if print_limit <= 0:
                break
    return lines.getvalue()


def convert_encoding(path, frm_encoding:str, to_encoding:str)->None:
    path = pathlib.Path(path)
    fname = path.name
    fpath = path.parent
    with open(path, 'r', encoding=frm_encoding, errors='replace') as f_in:
        with open(f'{fpath}\{to_encoding}_{fname}', 'w', encoding=to_encoding, errors='replace') as f_out:
            for line in f_in:
                f_out.write(line)
