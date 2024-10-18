import os
import shutil
import sys


def copy_files_by_extension(src_dir, dest_dir):
    try:
        for item in os.listdir(src_dir):
            item_path = os.path.join(src_dir, item)

            if os.path.isdir(item_path):
                copy_files_by_extension(item_path, dest_dir)
            elif os.path.isfile(item_path):
                file_extension = os.path.splitext(item)[1].lstrip('.').lower()

                dest_subdir = os.path.join(dest_dir, file_extension if file_extension else 'unknown')
                os.makedirs(dest_subdir, exist_ok=True)

                dest_file_path = os.path.join(dest_subdir, item)

                shutil.copy2(item_path, dest_file_path)

    except Exception as e:
        print(f"Error, files was not copied: {e}")


def main():
    if len(sys.argv) < 2:
        print("Incorrect arguments.")
        sys.exit(1)

    src_dir = sys.argv[1]
    if len(sys.argv) >= 3:
        dest_dir = sys.argv[2]
    else:
        dest_dir = "dist"

    if not os.path.isdir(src_dir):
        print(f"Path {src_dir} does not exits.")
        sys.exit(1)

    os.makedirs(dest_dir, exist_ok=True)
    copy_files_by_extension(src_dir, dest_dir)

    print(f"Files was successfully copied.")


if __name__ == "__main__":
    main()