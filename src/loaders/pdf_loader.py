from pathlib import Path

from langchain_community.document_loaders import PyPDFLoader

__all__ = ['load_pdf']

all_loaded_documents = []


def get_directory_documents():
    # 1. Obtiene la ruta de este archivo (pdf_loader.py)
    ruta_actual = Path(__file__).resolve()

    # 2. Sube 3 niveles en los directorios: de 'loaders' -> 'src' -> a la raíz del proyecto
    raiz_proyecto = ruta_actual.parents[2]

    # 3. Define la ruta hacia la carpeta data/documents
    return raiz_proyecto / "data" / "documents"


def get_files_pdf():
    dir_path = Path(get_directory_documents())
    file_names = [dir_path / file.name for file in dir_path.iterdir() if file.is_file() and file.suffix == ".pdf"]
    return file_names


def load_pdf():
    pdf_array = get_files_pdf()
    for pdf_path in pdf_array:
        try:
            loader = PyPDFLoader(pdf_path)
            all_loaded_documents.append({"archivo": pdf_path.name, "documentos": loader.load()})
        except Exception as e:
            print(f"Error loading {pdf_path}: {e}")
    return all_loaded_documents
