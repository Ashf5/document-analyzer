
import docx

class WordDoc:
    """
    creates a word doc object, which will have functionality to work with .docx file.
    """
    def __init__(self, path):
        self.doc = docx.Document(path)

    def read(self):
        """
        Returns all the text in the word document in one string.
        """

        secs = self.doc.iter_inner_content()
        text = ""
        for item in secs:
            if type(item) == docx.text.paragraph.Paragraph:
                text += f" {item.text}"
            elif type(item) == docx.table.Table:
                text += '\n'
                for row in item.rows:
                    for cell in row.cells:
                        text += f"{cell.text}\n"

        return text.strip()
    
# if __name__ == "__main__":
#     doc = WordDoc('../Malka_speech.docx')
#     print(doc.read())