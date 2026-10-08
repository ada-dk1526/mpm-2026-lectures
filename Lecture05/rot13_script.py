import codecs
import sys

if len(sys.argv) > 1:
    input_text = sys.argv[1]
else:
    input_text = "Vg'f n frperg!"

encoded_text = codecs.encode(input_text, "rot_13")
print(encoded_text)
