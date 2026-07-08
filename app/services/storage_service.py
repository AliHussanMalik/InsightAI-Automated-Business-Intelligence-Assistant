from pathlib import Path
from uuid import uuid4

from fastapi import UploadFile


class StorageService:

    UPLOAD_DIR = Path("storage/uploads")

    @classmethod
    async def save_file(cls, file: UploadFile):

        cls.UPLOAD_DIR.mkdir(parents=True, exist_ok=True)

        extension = Path(file.filename).suffix

        stored_filename = f"{uuid4()}{extension}"

        file_path = cls.UPLOAD_DIR / stored_filename

        contents = await file.read()

        with open(file_path, "wb") as buffer:
            buffer.write(contents)

        await file.seek(0)

        return {
            "original_filename": file.filename,
            "stored_filename": stored_filename,
            "file_path": str(file_path),
            "file_size": len(contents)
        }