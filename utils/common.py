import gdown

def download_from_driver(path, location_path):
    print(f"Begin download...., path: {path}")
    gdown.download(path, location_path, quiet=False)
    print(f"Completed download!!!: {path}")