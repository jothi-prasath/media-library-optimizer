import os
import glob
import argparse


movies_location = "/mnt/HDD/Movies"
series_location = "/mnt/HDD/Series"

def get_files(movies_location):
  mkv_paths = glob.glob(os.path.join(movies_location, "*/*.mkv"))
  mp4_paths = glob.glob(os.path.join(movies_location, "*/*.mp4"))
  avi_paths = glob.glob(os.path.join(movies_location, "*/*.avi"))
  nfo_paths = glob.glob(os.path.join(movies_location, "*/*.nfo"))
  return [mkv_paths, mp4_paths, avi_paths, nfo_paths]

def library_analyzer(file_paths):
  print("MKV Files   : ", len(file_paths[0]))
  print("MP4 Files   : ", len(file_paths[1]))
  print("AVI Files   : ", len(file_paths[2]))
  print("Total Files : ", len(file_paths[0]) + len(file_paths[1]) + len(file_paths[2]))

def remove_orphaned_files(file_paths):
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

def main():
  parser = argparse.ArgumentParser(description="Jellyfin Library Tool")
  parser.add_argument("-l", "--location", default=movies_location, help="Path to the media location")
  parser.add_argument("-a", "--analyze", action="store_true", help="Perform library analysis")
  parser.add_argument("-r", "--remove-orphaned", action="store_true", help="Remove orphaned files")

  args = parser.parse_args()
  file_paths = get_files(args.location)

  if args.analyze:
      library_analyzer(file_paths)

  if args.remove_orphaned:
      remove_orphaned_files(file_paths)

if __name__ == "__main__":
    main()