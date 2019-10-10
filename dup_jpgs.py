import sys
import csv
import os
import shutil

def get_csv_as_list(path):
    with open(path, 'r') as f:
        reader = csv.reader(f)
        l = list(reader)
        flat_list = [item for sublist in l for item in sublist]
        for sublist in l:
            for item in sublist:
                flat_list.append(item)
        return flat_list

def main():
    arg_len = len(sys.argv)
    ext = ".jpg"
    if arg_len > 1 and arg_len < 5 and sys.argv[1][-4:] == ext:
        src_path = sys.argv[1]
        csv_path = sys.argv[2]
        dest_path = sys.argv[3] if arg_len == 4 else "."
        if not os.path.isfile(csv_path):
            print("Error: no such file path for csv")
            exit(1)
        if dest_path != "." and not os.path.isdir("/".join(sys.argv[2].split("/")[:-1])):
            print("Error: should be directory path")
            exit(1)
        if dest_path[-1] != "/":
            dest_path = dest_path + "/"
        if not os.path.isdir(dest_path + "photo_dump/"):
            dest_path = dest_path + "photo_dump/"
            os.mkdir(dest_path)
        files = get_csv_as_list(csv_path)
        for f in files:
            shutil.copy(src_path, dest_path + f + ext)
        print("\033[92mSuccess!\033[4m")
    else:
        print("usage: [srcfile] [csv] optional: [destpath]")
        exit(1)

if __name__ == "__main__":
    main()
