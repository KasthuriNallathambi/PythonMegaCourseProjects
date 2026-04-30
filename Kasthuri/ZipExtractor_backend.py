import zipfile

def extract(archive_path, destination_path):
  with zipfile.ZipFile(archive_path, "r") as zip_ref:
      zip_ref.extractall(destination_path)