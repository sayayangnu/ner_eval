# coding: utf-8

from nltk import pos_tag, ne_chunk
import argparse

# borrowed from wnuteval.py
# splits data that is separated with an extra newline
def get_sents(lines):
    """
    Args:
        lines (Iterable[str]): the lines

    Yields:
        List[str]: sentences as list
    """
    sents = []
    sent = []
    stripped_lines = (line.strip() for line in lines)
    for line in stripped_lines:
        if line == '':
            sents.append(sent)
            sent = []
        else:
            sent.append(line)
    sents.append(sent)
    return sents


def main(wnut_data):

    # open data and read sentences out
    with open(wnut_data, 'r') as od:
        orig_lines = od.readlines()



if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("--wnut_file", type=str,
                        default="../emerging_entities_17/emerging.dev.conll",
                        help="wnut tsv file including annotations")

    args = parser.parse_args()

    main(args.wnut_file)
