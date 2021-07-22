import streamlit as st
import warnings
from pathlib import Path
warnings.filterwarnings("ignore")
st.set_option('deprecation.showfileUploaderEncoding', False)

import os 
import time

from NepaliOCR import NepaliOCR
ocr = NepaliOCR()


def read_markdown_file(markdown_file):
    return Path(markdown_file).read_text()


intro_markdown = read_markdown_file("main.md")
st.markdown(intro_markdown, unsafe_allow_html=True)

datafile = st.file_uploader("Upload", type="pdf")

def save_uploadedfile(uploadedfile):
	filename = str(int(time.time()))
	pdfFileName = filename + ".pdf"
	with open(os.path.join("demofiles",pdfFileName),"wb") as f:
		f.write(uploadedfile.getbuffer())
	return st.success("Saved File:{} to demofiles".format(pdfFileName)), pdfFileName


def main():
	if datafile is not None:
		_, pdfFileName = save_uploadedfile(datafile)

		pdfLocation = "/home/prajin/nepalicor/demofiles" + "/" + pdfFileName
		print(pdfLocation)
		images = ocr.pdf_to_image(pdfLocation)
		text_data, word2cord, sent= ocr.image_to_text_with_coordinates(images)
		st.write("Extracted text: ", text_data)
		st.write("Sentences", sent)
		st.write("Word Co-ordinates", word2cord)
		os.remove(pdfLocation)
	
main()


