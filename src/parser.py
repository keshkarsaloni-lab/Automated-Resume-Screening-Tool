import os
import pdfplumber
import docx


# 🔹 Extract text from PDF
def extract_text_from_pdf(file_path):
    text = ""
    try:
        with pdfplumber.open(file_path) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + "\n"
    except Exception as e:
        print(f"Error reading PDF {file_path}: {e}")
    return text


# 🔹 Extract text from DOCX
def extract_text_from_docx(file_path):
    text = ""
    try:
        doc = docx.Document(file_path)
        for para in doc.paragraphs:
            text += para.text + "\n"
    except Exception as e:
        print(f"Error reading DOCX {file_path}: {e}")
    return text


# 🔹 Extract text from TXT
def extract_text_from_txt(file_path):
    text = ""
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            text = file.read()
    except Exception as e:
        print(f"Error reading TXT {file_path}: {e}")
    return text


# 🔹 Detect file type
def extract_text(file_path):
    if file_path.endswith(".pdf"):
        return extract_text_from_pdf(file_path)
    elif file_path.endswith(".docx"):
        return extract_text_from_docx(file_path)
    elif file_path.endswith(".txt"):
        return extract_text_from_txt(file_path)
    else:
        print(f"Unsupported file format: {file_path}")
        return ""


# 🔹 Extract all resumes
def extract_all_resumes(resume_folder):
    resumes = {}

    for file_name in os.listdir(resume_folder):
        print("Found file:", file_name)  # Debug

        file_path = os.path.join(resume_folder, file_name)

        if os.path.isfile(file_path):
            text = extract_text(file_path)
            resumes[file_name] = text

    return resumes