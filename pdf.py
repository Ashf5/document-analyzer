
import pymupdf

class PdfDoc:
    def __init__(self, path):
        self.doc = pymupdf.open(path)

    def read(self):
        """
        Returns a string with all the text in the pdf
        """
        texts = []
        for page in self.doc:
            texts.append(page.get_text())
        return " ".join(texts).strip()
    

# if __name__ == "__main__":
#     doc = PdfDoc('../sample_project.pdf')
#     print(doc.read())