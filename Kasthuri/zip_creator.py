import zipfile as zp
import pathlib

def make_archieve(filePaths,dest_dir):
    dest_path = pathlib.Path(dest_dir,'compressed.zip')
    with zp.ZipFile(dest_path,'w') as zip:
        for filepath in filePaths:
            filepath = pathlib.Path(filepath)
            zip.write(filepath,arcname=filepath.name)

if __name__ == "__main__":
    make_archieve(filePaths=["report.txt","presentation.txt"],dest_dir="files")

