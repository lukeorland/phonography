# encoding: utf-8
from __future__ import unicode_literals
from __future__ import print_function
import csv
import sys
import unicodedata

filename = 'phonography_lib.csv'

if sys.version < '3': 
    infile = open(filename, 'rb')
else:
    infile = open(filename, 'r', newline='', encoding='utf8')

dataMaps = []
with infile as csvfile:
    reader = csv.DictReader(csvfile, delimiter=str(','), quoting=csv.QUOTE_NONE)
    for row in reader:
        #print(row)
        dataMaps.append(row)


def convert_format(input_value, input_type_key, output_type_key):
    """ Specify the input_value (using ascii), input_type_key and
    output_type_key (match the key names in phonography_lib.yaml).
    The output is the input string converted to the specified output format

        >>> convert_format('m', 'timit', 'ipa number')
        '114'
    """
    result = None
    for entry in dataMaps:
        if input_type_key in entry:
            if entry[input_type_key] == input_value:
                if output_type_key in entry:
                    result = entry[output_type_key]
    return result


if __name__ == "__main__":
    """
        >>> print convert_format('t_d', 'xsampa', 'unicode symbol')
        t̪

    """
    import doctest
    doctest.testmod()


