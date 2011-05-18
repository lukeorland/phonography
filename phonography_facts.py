# encoding: utf-8
import csv

dataMaps = []
with open('phonography_lib.csv', 'rb') as f:
    reader = csv.DictReader(f, delimiter=',', quoting=csv.QUOTE_NONE)
    for row in reader:
        # print row
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
        if entry.has_key(input_type_key):
            if entry[input_type_key] == input_value:
                if entry.has_key(output_type_key):
                    result = entry[output_type_key]
    return result


if __name__ == "__main__":
    """
        >>> print convert_format('t_d', 'xsampa', 'unicode symbol')
        t̪

    """
    import doctest
    doctest.testmod()


