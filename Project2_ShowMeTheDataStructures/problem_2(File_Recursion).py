def find_files(suffix, path):
    import os
    
    if os.path.isdir(path):
        if suffix == '':
            return []
        
        elements = os.listdir(path)
        files = [file for file in elements if (suffix) in file]
        folders = [folder for folder in elements if '.' not in folder]
    
        for folder in folders:
            files.extend(find_files(suffix, path + '/' + folder))
    
        return files
    else:
        return 'Unable to find specified path'


# Testing preparation
path_base = os.getcwd() + '/testdir'

# Test Case 1:
print(find_files(suffix='c', path=path_base))
# [a.c', 'b.c', 'a.c', 't1.c']

#Test Case 2:
print(find_files(suffix='h', path=path_base))
# ['a.h', 'b.h', 'a.h', 't1.h']

#Test Case 3:
print(find_files(suffix='z', path=path_base))
# []

# Test Case 4 (Edge case):
print(find_files(suffix='', path=path_base))
# []

# Test Case 5 (Edge case):
print(find_files(suffix='', path='gghd'))
# Unable to find specified path