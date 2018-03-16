import argparse
from TexSoup import TexSoup


def make_markdown_table(array):
    markdown = str("|")
    title_length = []
    for e in array[0]:
        title_length.append(len(e))
        to_add = " " + str(e) + str(" |")
        markdown += to_add
    markdown += "\n"
    markdown += '|'
    for size in title_length:
        markdown += (size+2) * '-' + '|'
    markdown += "\n"
    for entry in array[1:]:
        markdown += str("| ")
        for e in entry:
            to_add = str(e) + str(" | ")
            markdown += to_add
        markdown += "\n"
    return markdown


def line_to_list(line):
    line = line.lstrip()
    e = line.find('\\')
    line = line[:e]
    return list(map(lambda x: x.strip(), line.split('&')))


parser = argparse.ArgumentParser()
parser.add_argument("-o", "--output", help="Directs the output to a name of\
                    your choice", default='stdout')
parser.add_argument("-f", "--file", help="Input file", required=True)
parser.add_argument("--header", dest="header", action="store_true")
args = parser.parse_args()

with open(args.file, 'r') as f:
    contents = f.readlines()

if args.header:
    with open(args.file, 'r') as f:
        soup = TexSoup(f.read())
        markdown_table = "# " + soup.tabular.multicolumn.args[2] + '\n'

matches = [line for line in contents if '&' in line]

table = list(map(line_to_list,matches))

markdown_table += make_markdown_table(table)

with open(args.output, 'w') as f:
    f.write(markdown_table)
