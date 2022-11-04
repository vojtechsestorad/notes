import os

source_folder = 'c:/Users/vojte/Documents/coding/notes'
for item in os.listdir(source_folder):
    if os.path.isfile(os.path.join(source_folder, item)):
        if item.endswith('.md'):
            os.rename(
                os.path.join(source_folder, item),
                os.path.join(source_folder, 'README.md')
                )