def find_files(suffix, path):
    import os
    
    if suffix == '' or len(os.listdir(path)) == 0:
        return []
    
    elements = os.listdir(path)
    files = [file for file in elements if (suffix) in file]
    folders = [folder for folder in elements if '.' not in folder]
    
    for folder in folders:
        files.extend(find_files(suffix, path + '/' + folder))
    
    return files  


# Testing preparation
path_base = os.getcwd() + '/testdir'

# Normal Cases:
print(find_files(suffix='c', path=path_base))
# [a.c', 'b.c', 'a.c', 't1.c']

print(find_files(suffix='h', path=path_base))
# ['a.h', 'b.h', 'a.h', 't1.h']

print(find_files(suffix='z', path=path_base))
# []

# Edge Cases:
print(find_files(suffix='', path=path_base))
# []