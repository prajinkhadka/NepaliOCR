from NepaliOCR import NepaliOcr 

ocr = NepaliOcr()
images = ocr.pdf_to_image("/home/prajin/nepalicor/Streamlitdemo/uploadedfile.pdf")

ocr.image_to_text_with_coordinates(images)
