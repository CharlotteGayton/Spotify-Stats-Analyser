import shutil
import pandas as pd
from analysis_scripts.removeUnwantedFiles import RemoveFiles

def main():
    # Import user data
    # shutil.unpack_archive("my_spotify_data.zip")

    # Remove unwanted files 
    FilesRemove = RemoveFiles()
    FilesRemove.FileProcessor()

    Identity = pd.read_json("MyData/Identity.json", typ='Series')
    Playlists = pd.read_json("MyData/Playlist1.json", typ='Series')
    StreamingHistory = pd.read_json("MyData/StreamingHistory0.json", typ='Series')

    print(Playlists.columns.toList())

if __name__ == "__main__":
    main()