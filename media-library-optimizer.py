import os
import glob
import argparse
import re

# Default library placeholder
default_library_path = "/mnt/HDD/Movies2"

def get_files(directory):
  mkv_paths = glob.glob(os.path.join(directory, "*/*.mkv"))
  mp4_paths = glob.glob(os.path.join(directory, "*/*.mp4"))
  avi_paths = glob.glob(os.path.join(directory, "*/*.avi"))
  nfo_paths = glob.glob(os.path.join(directory, "*/*.nfo"))
  return [mkv_paths, mp4_paths, avi_paths, nfo_paths]

def get_folders(directory):
  folders = [folder for folder in os.listdir(directory) if os.path.isdir(os.path.join(directory, folder))]
  return folders

def library_analyzer(library_path):
  file_paths = get_files(library_path)
  print("MKV Files   : ", len(file_paths[0]))
  print("MP4 Files   : ", len(file_paths[1]))
  print("AVI Files   : ", len(file_paths[2]))
  print("Total Files : ", len(file_paths[0]) + len(file_paths[1]) + len(file_paths[2]))

def remove_orphaned_files(library_path):
  file_paths = get_files(library_path)
  formats = ("nfo", "jpg", "png")
  mkv_files = set([os.path.splitext(file)[0] for file in file_paths[0]])
  mp4_files = set([os.path.splitext(file)[0] for file in file_paths[1]])
  avi_files = set([os.path.splitext(file)[0] for file in file_paths[2]])
  nfo_files = set([os.path.splitext(file)[0] for file in file_paths[3]])
  orphaned_nfo_files = nfo_files - (mkv_files | mp4_files | avi_files)
  if len(orphaned_nfo_files):
    for orphaned_nfo_file in orphaned_nfo_files:
      for format in formats:
        if os.path.exists(orphaned_nfo_file + "." + format):
          os.remove(orphaned_nfo_file + "." + format)
    print(f"🔥 {len(orphaned_nfo_files)} files removed 🔥")
  else:
    print("😎 no orphaned files 😎")

def rename_folders(directory):
  # Regex to match a website url 
  regex_pattern = r'www\.[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}\s*-*\s'
  folders = get_folders(directory)
  for folder in folders:
        new_folder = re.sub(regex_pattern, '', folder)
        old_path = os.path.join(directory, folder)
        new_path = os.path.join(directory, new_folder)
        if old_path == new_path:
          print(f'Skipped: {folder}')
        else:
          # Prompt user for confirmation
          user_input = input(f'Rename "{folder}" --> "{new_folder}"? (y/N): ').lower()
          if user_input == 'y':
              os.rename(old_path, new_path)
              print(f'{folder} --> {new_folder}')
          else:
              print(f'Skipped: {folder}')

def main():
  parser = argparse.ArgumentParser(description="Media Library Optimizer")
  parser.add_argument("-l", "--location", default=default_library_path, help="Path to the media location")
  parser.add_argument("-a", "--analyze", action="store_true", help="Perform library analysis")
  parser.add_argument("-r", "--remove-orphaned", action="store_true", help="Remove orphaned files")
  parser.add_argument("-re", "--rename-folders", action="store_true", help="Remove URL prefix folders")

  args = parser.parse_args()
  if os.path.isdir(args.location):
    library_path = args.location
  else:
     print("⚠️ Library path not exist ⚠️")
     exit(1)

  if args.analyze:
      library_analyzer(library_path)

  if args.remove_orphaned:
      remove_orphaned_files(library_path)

  if args.rename_folders:
      rename_folders(library_path)

if __name__ == "__main__":
    main()
