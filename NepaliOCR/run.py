from NepaliOCR import NepaliOCR

import argparse 
my_parser = argparse.ArgumentParser()
my_parser.add_argument('--input', action='store', type=str, required=True)
args = my_parser.parse_args()

file_location = str(args.input)
ocr = NepaliOCR()
images = ocr.pdf_to_image(file_location)

text_data, word2cord, sent = ocr.image_to_text_with_coordinates(images)

print("\n Text Data \n", text_data)
print("\n Word Co-ordinates \n", word2cord)
print("\n Sentences List \n", sent)