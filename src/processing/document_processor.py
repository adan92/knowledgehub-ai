from langchain_text_splitters import RecursiveCharacterTextSplitter


class DocumentProcessor:

    def __init__(
            self,
            chunk_size: int = 1000,
            chunk_overlap: int = 200
    ):
        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap
        )

    def process(self, filename: str, pages):
        chunks = self.text_splitter.split_documents(pages)
        for index, chunk in enumerate(chunks):
            chunk.metadata.update({
                "filename": filename,
                "chunk_id": index,
                "total_chunks": len(chunks)

            })
        return chunks
