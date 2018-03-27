import sys


def file_character_frequencies(file_name):
    # Suggested helper
    return {}


class PriorityTuple(tuple):
    """A specialization of tuple that compares only its first item when sorting.
    Create one like this: PriorityTuple((x, y, z)) # note the doubled parens"""
    def __lt__(self, other):
        return self[0] < other[0]

    def __le__(self, other):
        return self[0] <= other[0]


def huffman_codes_from_frequencies(frequencies):
    # Suggested helper
    return {}


def huffman_letter_codes_from_file_contents(file_name):
    """WE WILL GRADE BASED ON THIS FUNCTION."""
    # Suggested strategy...
    #freqs = file_character_frequencies(file_name)
    #return huffman_codes_from_frequencies(freqs)
    return {}


def encode_file_using_codes(file_name, letter_codes):
    """Provided to help you play with your code."""
    contents = ""
    with open(file_name) as f:
        contents = f.read()
    file_name_encoded = file_name + "_encoded"
    with open(file_name_encoded, 'w') as fout:
        for c in contents:
            fout.write(letter_codes[c])
    print("Wrote encoded text to {}".format(file_name_encoded))


def decode_file_using_codes(file_name_encoded, letter_codes):
    """Provided to help you play with your code."""
    contents = ""
    with open(file_name_encoded) as f:
        contents = f.read()
    file_name_encoded_decoded = file_name_encoded + "_decoded"
    codes_to_letters = {v: k for k, v in letter_codes.items()}
    with open(file_name_encoded_decoded, 'w') as fout:
        num_decoded_chars = 0
        partial_code = ""
        while num_decoded_chars < len(contents):
            partial_code += contents[num_decoded_chars]
            num_decoded_chars += 1
            letter = codes_to_letters.get(partial_code)
            if letter:
                fout.write(letter)
                partial_code = ""
    print("Wrote decoded text to {}".format(file_name_encoded_decoded))


def main():
    """Provided to help you play with your code."""
    import pprint
    frequencies = file_character_frequencies(sys.argv[1])
    pprint.pprint(frequencies)
    codes = huffman_codes_from_frequencies(frequencies)
    pprint.pprint(codes)


if __name__ == '__main__':
    """We are NOT grading you based on main, this is for you to play with."""
    main()
