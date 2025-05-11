
from langchain_text_splitters import RecursiveCharacterTextSplitter

class Chunk:
    """
    This class is to deal with chunking. The pdf and word classes inherit from it. It has a static method 'chunk' that takes in a list of strings and returns it in chunks using langchain recursive text splitter.
    """
    @staticmethod 
    def chunk(text:str, chunk_size=1000, chunk_overlap=100):
        text_splitter = RecursiveCharacterTextSplitter(
        separators=["\n\n", "\n", ".", " "],
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap
        )
        texts = text_splitter.create_documents([text])
        return texts
                
