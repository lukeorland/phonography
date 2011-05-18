import yaml

f = open('phonography_lib.yaml')
dataMap = yaml.load(f)
f.close

def convert_format(input_value, input_type_key, output_type_key):
    """ Specify the input_value (using ascii), input_type_key and
    output_type_key (match the key names in phonography_lib.yaml).
    The output is the input string converted to the specified output format

        >>> convert_format('m', 'timit', 'ipa number')
        114
    """
    result = None
    for entry in dataMap:
        if entry.has_key(input_type_key):
            if entry[input_type_key] == input_value:
                if entry.has_key(output_type_key):
                    result = entry[output_type_key]
    return result


if __name__ == "__main__":
    import doctest
    doctest.testmod()

