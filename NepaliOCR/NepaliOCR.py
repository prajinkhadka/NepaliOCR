import streamlit

# import cv2
import numpy as np
import pdf2image
import pytesseract


import gdown
url = 'https://drive.google.com/uc?id=1kvFJ7plR95lfwzWLcJWthMWrW8GIRNfS'

output = 'Devanagari.traineddata'
# gdown.download(url, output, quiet=False)

# file 
# https://drive.google.com/file/d/1B90BS3cFlJcDDSUP_YxGBhLuVX_Uj7ai/view?usp=sharing


from pytesseract import Output
import string 
import numpy as np 
import itertools


class NepaliOCR:
    def pdf_to_image(self,pdf_path):
        img = pdf2image.convert_from_path(pdf_path, dpi=100, grayscale=True)
        return img

    def image_to_text_with_coordinates(self, images):
        sent =  list()
        word2cord = list()
        count = len(images)

        for page in range(count):
            img = images[page]
            page_data = pytesseract.image_to_data(img, output_type=Output.DICT, config='--psm 6', lang='Devanagari')

            words2Coirdinates = self.words2Coordinates(page_data, page)
            word2cord.append(words2Coirdinates)
            # print("word2cord", word2cord)
            
            text_data = " " .join(page_data['text'])

            # Sentence Splitter 
            sentences = self.sentence_splitter(text_data)
            sent.append(sentences)

            # actual text data 

        return text_data, word2cord, sent
 
 

    def words2Coordinates(self, extracted_data, page_num):
        test_wr_parser_d = list()
        for i in range(len(extracted_data['text'])):
            single_tuple = [extracted_data['left'][i], extracted_data['top'][i], extracted_data['width'][i], extracted_data['height'][i], 
                            extracted_data['text'][i], page_num, extracted_data['block_num'][i], extracted_data['line_num'][i], extracted_data['word_num'][i]]
            
            if single_tuple[4] != '':
                test_wr_parser_d.append(single_tuple)
            else:
                # add logging.
                pass
        # print(test_wr_parser_d)
        return test_wr_parser_d

    def sentence_splitter(self, text_data):
        # Sentence splitter 
        sentences = text_data.strip().split(u"।")
        sentences = [sentence.translate(str.maketrans('', '', string.punctuation)) for sentence in sentences]
        return sentences 