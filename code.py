import os
import shutil

EXTENSIONS = {
    "Images": [".jpg",".jpeg",".png",".gif",".bmp",".webp",".tiff",".svg"],
    "Documents": [".pdf",".doc",".docx",".txt",".ppt",".pptx",".xls",".xlsx",".csv"],
    "Videos": [".mp4",".mkv",".avi",".mov",".wmv",".flv",".webm"],
    "Audio": [".mp3",".wav",".aac",".flac",".ogg",".m4a"],
    "Archives": [".zip",".rar",".7z",".tar",".gz",".bz2"],
    "Code": [".py",".js",".java",".c",".cpp",".cs",".html",".css",".json",".xml",".php",".ts",".sh"]
}

def get_category(ext):
    for category, exts in EXTENSIONS.items():
        if ext.lower() in exts:
            return category
    return "Others"

def organize(folder):
    if not os.path.isdir(folder):
        return
    for item in os.listdir(folder):
        path = os.path.join(folder, item)
        if os.path.isfile(path):
            _, ext = os.path.splitext(item)
            category = get_category(ext)
            target_dir = os.path.join(folder, category)
            os.makedirs(target_dir, exist_ok=True)
            target_path = os.path.join(target_dir, item)
            count = 1
            while os.path.exists(target_path):
                name, extension = os.path.splitext(item)
                target_path = os.path.join(target_dir, f"{name}_{count}{extension}")
                count += 1
            shutil.move(path, target_path)

if __name__ == "__main__":
    directory = input("Enter folder path: ").strip()
    organize(directory)
    print("Organization complete")
