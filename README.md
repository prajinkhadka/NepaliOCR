# NepaliOCR
Nepali OCR on printed documents.

## [DEMO](http://52.177.21.44:8501/)

* Install requirements : ```pip3 install -r requirements.txt```

* Install these apt packages :
    - ```sudo apt-get install poppler-utils```
    - ```sudo apt install tesseract-ocr```

* Download Devanagari.traineddata : 
    - ```gdown --id 1kvFJ7plR95lfwzWLcJWthMWrW8GIRNfS```

* Move Devnagari.traineddata to : ```/usr/share/tesseract-ocr/4.00/tessdata/```

* Run locally, ```python3 NepaliOCR/run.py --input "/home/prajin/NepaliOCR/NepaliOCR/doc2.pdf"```

* Demo