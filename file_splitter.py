import os
import argparse
import sys

def main():
    chunk_num = 1

    parser = argparse.ArgumentParser()
    parser.add_argument("file")
    parser.add_argument("-s", "--size", default=5)

    args = parser.parse_args()

    chunk_size = args.size * 1024 * 1024

    file_path = os.getcwd() + "\\" + args.file

    if not os.path.exists(file_path):
        print(f"Path {file_path} doesn't exist")
        sys.exit()

    with open(file_path, "rb") as f:
        while True:
            chunk = f.read(chunk_size)

            if not chunk:
                break

            with open(file_path + "(" + str(chunk_num) + ")" + ".chunk", "wb") as out:
                out.write(chunk)

            chunk_num += 1
    
if __name__ == "__main__":
    main()clipboard