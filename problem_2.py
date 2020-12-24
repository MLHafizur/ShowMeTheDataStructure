import os
def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.
    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.
    There are no limit to the depth of the subdirectories can be.
    Args:
    suffix(str): suffix if the file name to be found
    path(str): path of the file system
    Returns:
    a list of paths
    """
    if suffix == 'c':
        paths_list.append(path)
    try:
        for f in os.listdir(path):
            if os.path.isfile(os.path.join(path, f)):
                suffix = f.split('.')[-1]
                paths_list.append(os.path.join(path, f))
            if os.path.isdir(os.path.join(path, f)):
                find_files('c', os.path.join(path, f))
    except FileNotFoundError:
        return 'Path does not exist.'
    return [i for i in paths_list if i.endswith('.c')]#filter .c file extensions

if __name__ == '__main__':
    print('-----------------TEST1-------------------')
    paths_list = []
    print(find_files('c', 'testdir'))

    print('-----------------TEST-2-------------------')
    paths_list = []
    print(find_files('c', 'testdir2')) #returns empty because there is no *.c file in the directory `testdir2`

    print('-----------------TEST-3-------------------')
    paths_list = []
    print(find_files('c', 'testdir3'))#returns testdir3/subdir1/subdir2/huffman.c

    print('-----------------TEST-4-------------------')
    paths_list = []
    print(find_files('c', 'testdir4'))#returns error message saying path doesn't exist.