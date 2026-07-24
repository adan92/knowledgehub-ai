from pathlib import Path

from fastapi import (
    APIRouter,
    UploadFile,
    File,
    HTTPException
)

from fastapi.responses import FileResponse

router = APIRouter()

DOCUMENTS_PATH = Path("data/documents")


@router.get("")
def list_documents():

    return [
        pdf.name
        for pdf in DOCUMENTS_PATH.glob("*.pdf")
    ]


@router.get("/{filename}")
def get_document(filename: str):

    pdf = DOCUMENTS_PATH / filename

    if not pdf.exists():

        raise HTTPException(
            status_code=404,
            detail="Documento no encontrado"
        )

    return FileResponse(
        pdf,
        media_type="application/pdf"
    )


@router.post("")
async def upload_document(
    file: UploadFile = File(...)
):

    destination = DOCUMENTS_PATH / file.filename

    with destination.open("wb") as f:

        f.write(
            await file.read()
        )

    return {
        "message": "Documento cargado correctamente."
    }


@router.delete("/{filename}")
def delete_document(filename: str):

    pdf = DOCUMENTS_PATH / filename

    if not pdf.exists():

        raise HTTPException(
            status_code=404,
            detail="Documento no encontrado"
        )

    pdf.unlink()

    return {
        "message": "Documento eliminado."
    }
