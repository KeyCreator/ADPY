import hashlib


FILE_NAME = 'countries.txt'


def file_lines(path):

    with open(path, encoding='utf-8') as file:
        for line in file:
            line = line.strip()
            hash_object = hashlib.md5(line.encode())
            yield line, hash_object.hexdigest()


def main():

    file_name = input('Please enter file name (Enter = "countries.txt"): ')

    if not file_name:
        file_name = FILE_NAME

    print(f'md5 hash of each line in the file {file_name}:')

    for obj, hash_obj in file_lines(file_name):
        print(f'{obj}: {hash_obj}')


if __name__ == '__main__':

    main()