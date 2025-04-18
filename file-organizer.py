import os
import shutil
from dotenv import load_dotenv

load_dotenv()

DESKTOP_PATH = os.environ.get('DESKTOP_PATH', os.path.join(os.path.expanduser("~"), "Desktop"))
DOWNLOADS_PATH = os.environ.get('DOWNLOADS_PATH', os.path.join(os.path.expanduser("~"), "Downloads"))

DIRECTORIES_TO_ORGANIZE = [
    DESKTOP_PATH,
    DOWNLOADS_PATH
]

file_types = {
    "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".pptx"],
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".heic"],
    "Videos": [".mp4", ".avi", ".mov"],
    "Audio": [".mp3", ".wav"],
    "Archives": [".zip", ".rar", ".tar", ".gz"],
    "Applications": [".exe", ".apk", ".dmg", ".lnk", ".url"],
    "Scripts": [".py", ".js", ".sh"],
    "Miscellaneous": []
}

def analyze_directory(directory_path):
    print(f"\nAnalyzing {directory_path}...")
    
    stats = {folder_name: {"count": 0, "size": 0} for folder_name in file_types}
    stats["Other"] = {"count": 0, "size": 0}
    
    for filename in os.listdir(directory_path):
        file_path = os.path.join(directory_path, filename)
        
        if os.path.isdir(file_path):
            continue
            
        file_extension = os.path.splitext(filename)[1].lower()
        
        file_category = "Other"
        for category, extensions in file_types.items():
            if file_extension in extensions:
                file_category = category
                break
        
        stats[file_category]["count"] += 1
        stats[file_category]["size"] += os.path.getsize(file_path)
    
    print("\nCurrent directory contents:")
    print("-" * 50)
    total_files = 0
    total_size = 0
    
    for category, data in stats.items():
        if data["count"] > 0:
            size_mb = data["size"] / (1024 * 1024)  # Convert bytes to MB
            print(f"{category}: {data['count']} files ({size_mb:.2f} MB)")
            total_files += data["count"]
            total_size += data["size"]
    
    print("-" * 50)
    print(f"Total: {total_files} files ({total_size / (1024 * 1024):.2f} MB)")
    
    return stats

def preview_organization(directory_path):
    print(f"\nPreview of organization for {directory_path}:")
    print("-" * 50)
    
    moves = {folder_name: [] for folder_name in file_types}
    moves["Other"] = []
    
    for filename in os.listdir(directory_path):
        file_path = os.path.join(directory_path, filename)
        
        if os.path.isdir(file_path):
            continue
            
        file_extension = os.path.splitext(filename)[1].lower()
        
        file_category = "Other"
        for category, extensions in file_types.items():
            if file_extension in extensions:
                file_category = category
                break
        
        moves[file_category].append(filename)
    
    for category, files in moves.items():
        if files:
            print(f"\n{category} folder would contain {len(files)} files:")
            for i, file in enumerate(files):
                if i < 5:  # Limit to first 5 files per category to avoid cluttering the display
                    print(f"  - {file}")
                elif i == 5:
                    print(f"  - ... and {len(files) - 5} more files")
    
    print("-" * 50)
    return moves

def organize_directory(directory_path):
    print(f"\nOrganizing {directory_path}...")
    
    moved_files = {folder_name: [] for folder_name in file_types}
    moved_files["Other"] = []
    
    for filename in os.listdir(directory_path):
        file_path = os.path.join(directory_path, filename)
        
        if os.path.isdir(file_path):
            continue
            
        file_extension = os.path.splitext(filename)[1].lower()
        
        file_category = "Other"
        for category, extensions in file_types.items():
            if file_extension in extensions:
                file_category = category
                break
        
        destination_folder = os.path.join(directory_path, file_category)
        if not os.path.exists(destination_folder):
            os.makedirs(destination_folder)
        
        destination_path = os.path.join(destination_folder, filename)
        if os.path.exists(destination_path):
            name, ext = os.path.splitext(filename)
            i = 1
            while os.path.exists(os.path.join(destination_folder, f"{name} ({i}){ext}")):
                i += 1
            destination_path = os.path.join(destination_folder, f"{name} ({i}){ext}")
            
        try:
            shutil.move(file_path, destination_path)
            moved_files[file_category].append(filename)
        except Exception as e:
            print(f"Error moving {filename}: {e}")
    
    print("\nOrganization complete:")
    print("-" * 50)
    total_moved = 0
    
    for category, files in moved_files.items():
        if files:
            print(f"Moved {len(files)} files to {category} folder")
            total_moved += len(files)
    
    print("-" * 50)
    print(f"Total: {total_moved} files organized")
    
    return moved_files

def main():
    for directory in DIRECTORIES_TO_ORGANIZE:
        if not os.path.exists(directory):
            print(f"Directory not found: {directory}")
            continue
            
        analyze_directory(directory)
        
        preview_organization(directory)
        
        choice = input(f"\nDo you want to organize {directory}? (y/n): ").lower()
        if choice == 'y':
            organize_directory(directory)
        else:
            print("Organization skipped.")

if __name__ == "__main__":
    main()