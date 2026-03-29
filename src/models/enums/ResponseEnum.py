from enum import Enum

class ResponseSignal(Enum):
    FILE_UPLOAD_SUCCESS = "File uploaded successfully"
    FILE_TYPE_ERROR = "File type is not allowed"
    FILE_SIZE_ERROR = "File size exceeds the maximum allowed limit"
    PROCESSING_SUCCESS = "File processed successfully"
    PROCESSING_FAILED = "Error processing the file"
