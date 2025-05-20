import os
import fitz  # PyMuPDF

def extract_text_from_file(path: str) -> str:
    """
    Extrait le texte d'un fichier .pdf ou .txt.
    """
    if path.endswith(".pdf"):
        doc = fitz.open(path)
        return "\n".join([page.get_text() for page in doc])
    elif path.endswith(".txt"):
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    else:
        raise ValueError(f"Format non supporté : {path}")


def load_documents_from_data_folder(data_dir="data") -> list[str]:
    """
    Parcourt tous les fichiers dans le dossier data/ et retourne le texte extrait.
    """
    documents = []
    for filename in os.listdir(data_dir):
        filepath = os.path.join(data_dir, filename)
        try:
            text = extract_text_from_file(filepath)
            documents.append(text)
        except Exception as e:
            print(f"Erreur lors du traitement de {filename} : {e}")
    return documents
