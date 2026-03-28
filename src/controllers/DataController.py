from .BaseController import BaseController
from .ProjectController import ProjectController
from fastapi import UploadFile
from models import ResponseSignal
import re 
import os 

class DataController(BaseController):
    def __init__(self):
        super().__init__()
        self.size_scale = 1024 * 1024  # 1 MB in bytes
    
    def validate_uploaded_file(self, file: UploadFile):

        # Check file type
        if file.content_type not in self.app_settings.FILE_ALLOWED_TYPES:

            return False, ResponseSignal.FILE_TYPE_ERROR.value
        
        # Check file size
        if file.size > self.app_settings.FILE_MAX_SIZE * self.size_scale:
            return False, f"{ResponseSignal.FILE_SIZE_ERROR.value} {self.app_settings.FILE_MAX_SIZE} MB."

        return True, ResponseSignal.FILE_UPLOAD_SUCCESS.value
    

    def generate_unique_filename(self, original_filename: str,project_id: str) -> str:

        random_key = self.generate_random_string()

        project_path = ProjectController().get_project_path(project_id=project_id)

        cleaned_filename = self.get_clean_filename(original_filename=original_filename)

        new_file_path = os.path.join(project_path, f"{random_key}_{cleaned_filename}")

        while os.path.exists(new_file_path):
            random_key = self.generate_random_string()
            new_file_path = os.path.join(project_path, f"{random_key}_{cleaned_filename}")

        
        return new_file_path


    def get_clean_filename(self, original_filename: str) -> str:

        # Remove special characters and spaces, keep only alphanumeric and underscores
        cleaned_filename = re.sub(r'[^\w\.-]', '', original_filename.strip())

        # replace spaces with underscore and remove leading/trailing spaces
        cleaned_filename = cleaned_filename.replace(' ', '_')

        return cleaned_filename