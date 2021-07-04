import os
import sys


def get_files_with_extension(path, ext='*'):
    files = os.listdir(path)
    if ext != '*':
        return list(filter(lambda x: x.endswith("." + ext), files))
    return files


def rename_extension(path, dest_ext='', source_ext='*'):
    print('Converting Extension... ')
    file_names = get_files_with_extension(path, source_ext)
    if len(dest_ext) != 0:
        dest_ext = '.' + dest_ext
    for filename in file_names:
        base = os.path.splitext(filename)[0]
        new_file_name = base + dest_ext
        print(filename + ' -> ' + new_file_name)
        os.rename(os.path.join(path, filename), os.path.join(path, new_file_name))


if __name__ == '__main__':
    args = sys.argv[1:]
    option = args[0]
    if len(args) == 3 and option == '--all':
        rename_extension(args[1], args[2])
    elif len(args) == 3 and option == '--remove':
        rename_extension(args[1], '', args[2])
    else:
        rename_extension(args[0], args[2], args[1])
