def main():
    import os
    import shutil

    folder = os.path.dirname(os.path.realpath(__file__))

    for file in os.listdir(folder):
        if not os.path.exists('Documents'):
            os.mkdir('Documents')
        if file.endswith(('.txt','.doc','.docx','.pdf','.odt','.rtf','.tex')):
            shutil.copy(file,'Documents')
            os.remove(file)

        if not os.path.exists('Videos'):
            os.mkdir('Videos')
        if file.endswith(('.mp4','.webm','.mkv','.flv',
                            '.wmv','.avi','.rmvb')):
            shutil.copy(file,'Videos')
            os.remove(file)

        if not os.path.exists('Music'):
            os.mkdir('Music')
        if file.endswith(('.mp3','.raw','.3gp','.aa','.aax','.aiff')):
            shutil.copy(file,'Music')
            os.remove(file)

        if not os.path.exists('Compressed'):
            os.mkdir('Compressed')
        if file.endswith(('.rar','.tar','.zip','.7z','.bz2','.gz')):
            shutil.copy(file,'Compressed')
            os.remove(file)

        if not os.path.exists('Images'):
            os.mkdir('Images')
        if file.endswith(('.jpg','.tiff','.png','.gif','.psd','.ai')):
            shutil.copy(file,'Images')
            os.remove(file)

if __name__ == "__main__":
    main()