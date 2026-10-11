import codecs
import sys


def rot13(original):
    return codecs.encode(original, "rot_13")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        input_text = sys.argv[1]
    else:
        input_text = "Vg'f n frperg!"
    encoded_text = rot13(input_text)
    print(encoded_text)
