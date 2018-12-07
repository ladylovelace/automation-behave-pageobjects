import os


def directory_iterator(directory):
    '''Iterate over a directory infinitely'''
    xml_files = []
    for root, dirs, files in os.walk(directory):
        for name in files:
                xml_files.append(os.path.join(root, name))
    return xml_files