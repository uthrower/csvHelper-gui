from io import StringIO

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