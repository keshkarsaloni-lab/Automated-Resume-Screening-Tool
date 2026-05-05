import os

# 🔹 Read text file safely
def read_file(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return f.read()
    except Exception as e:
        print(f"Error reading file: {e}")
        return ""


# 🔹 Load skills from file
def load_skills(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return [line.strip().lower() for line in f.readlines()]
    except Exception as e:
        print(f"Error loading skills: {e}")
        return []


# 🔹 Ensure folder exists
def create_folder(folder_path):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)