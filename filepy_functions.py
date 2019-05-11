import platform


def create_filename(filename, file_extension):
    assert isinstance(filename, str), 'filename must be a string'
    assert isinstance(file_extension, str), 'file_extension must be a string'
    # Linux has less characters that aren't allowed in filenames
    if platform.system() == 'Linux':
        disallowed_characters = ['/', '\\', '%', ':']
    else:
        disallowed_characters = ['/', '\\', '?', '%', '*', ':', '|', '"', '<', '>']
    for character in disallowed_characters:
        filename = filename.replace(character, '')
        filename = file_extension.replace(character, '')
    if file_extension[0] != '.':
        file_extension = '.' + file_extension
    if len(filename) < len(file_extension) + 2:
        add_extension = True
    elif filename[:-len(file_extension)] != file_extension:
        add_extension = True
    else:
        add_extension = False
    if add_extension:
        filename = filename+file_extension
    return filename