# import shutil
# import os

# def _save_file_to_server(uploaded_img, path=".", save_as="default"):
#     extension = os.path.splitext(uploaded_img.filename)[-1]
#     temp_file = os.path.join(path, save_as + extension)
#     with open(temp_file, "wb") as buffer:
#         shutil.copyfileobj(uploaded_img.file, buffer)

#     return temp_file

import requests as req

def call_text_analytics_api(headers, document, endpoint):
    response = req.post('https://fastapi.cognitiveservices.azure.com/text/analytics/v3.1/' + endpoint, headers=headers,json=document)
    return response.json()