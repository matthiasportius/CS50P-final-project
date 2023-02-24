import argparse
import datetime
import os
import sys
from re import fullmatch


def main() -> None:
    args = parse_arguments()
    files = get_files(args.path)
    if args.type and args.nottype:
        sys.exit("Only specify one of the following: -t/--type or -nt/--nottype")
    if args.type:
        files = filter_files_include(args.type, files)
    elif args.nottype:
        files = filter_files_exclude(args.nottype, files)
    print(get_oldest_file(files))
    if args.olderthen or args.olderthen == 0:
        print(get_olderthen_files(args.olderthen, files))


def parse_arguments() -> tuple[str, str]:
    parser = argparse.ArgumentParser(description="search for oldest files in directory")
    parser.add_argument("-p", "--path", default=os.path.expanduser("~"), help="specify root directory to search in:  C:\\full_path", type=str)
    parser.add_argument("-t", "--type", help="specify filetype: .extension", type=str)
    parser.add_argument("-nt", "--nottype", help="specify filetype to exclude: .extension", type=str)
    parser.add_argument("-ot", "--olderthen", default=None, help="show files older than specified days:  int", type=int)

    args = parser.parse_args()

    return args


def get_files(path: str) -> list[str]:
    if not os.path.exists(path) or not os.path.isdir(path):
        sys.exit("Path does not exist")

    files = []
    for dirpath, _, filenames in os.walk(path):
        filenames = [os.path.join(dirpath, file) for file in filenames]
        files += filenames

    if not files:
        sys.exit("No files in this directory")

    return files


def filter_files_include(extension: str, files: list[str]) -> list[str]:
    if not fullmatch(r"\.[a-zA-Z0-9]+", extension):
        sys.exit("Not a valid file extension")
    return [file for file in files if file.endswith(extension.lower())]


def filter_files_exclude(extension: str, files: list[str]) -> list[str]:
    if not fullmatch(r"\.[a-zA-Z0-9]+", extension):
        sys.exit("Not a valid file extension")
    return [file for file in files if not file.endswith(extension.lower())]


def get_oldest_file(files: list[str]) -> str:
    if files:
        files = sorted(files, key=os.path.getatime)
        return f"File least used:   {files[0]}\n"
    else:
        return "File least used:   No file found\n"


def get_olderthen_files(older_then: int, files: list[str]) -> str:
    older = []

    if older_then:
        now = datetime.datetime.now()
        span = datetime.timedelta(days=older_then)

        for file in files:
            atime = os.path.getatime(file)
            date = datetime.datetime.fromtimestamp(atime)
            if now - span > date:
                older.append(file)
    else:
        older = files

    out = f"Files not used for {older_then} "
    out += "day:   " if older_then == 1 else "days:   "
    if older:
        for file in older:
            out += f"{file}\n{'':29}"
    else:
        out += "None\n"

    return out


if __name__ == "__main__":
    main()
