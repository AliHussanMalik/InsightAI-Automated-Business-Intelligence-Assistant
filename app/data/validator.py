from fastapi import HTTPException, UploadFile


class FileValidator:
    ALLOWED_EXTENSIONS = {".csv", ".xlsx", ".xls"}
    MAX_FILE_SIZE = 20 * 1024 * 1024  # 20 MB

    @classmethod
    async def validate(cls, file: UploadFile) -> None:
        filename = file.filename or ""

        if "." not in filename:
            raise HTTPException(
                status_code=400,
                detail="File has no extension."
            )

        extension = "." + filename.split(".")[-1].lower()

        if extension not in cls.ALLOWED_EXTENSIONS:
            raise HTTPException(
                status_code=400,
                detail=f"Unsupported file type: {extension}"
            )

        contents = await file.read()

        if len(contents) > cls.MAX_FILE_SIZE:
            raise HTTPException(
                status_code=400,
                detail="File exceeds the maximum size of 10 MB."
            )

        # Reset pointer so other code can read the file again
        await file.seek(0)