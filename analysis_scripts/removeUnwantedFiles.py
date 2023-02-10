from os import listdir, remove
from os.path import isfile, join
import re

class RemoveFiles:
    def __init__(self):
        self.DataPath = 'MyData'
        self.delete = ['Follow.json', 'Identifiers.json', 'Inferences.json', 'Payments.json', 'Read_Me_First.pdf', 'SearchQueries.json', 'Userdata.json', 'YourLibrary.json']
        # self.FilesToKeep = ['StreamingHistory*.json', 'Playlist*.json', 'Identity*.json']
        # self.FilesToKeepCombined = "/\b(?:StreamingHistory.*\.json|Playlist.*\.json|Identity.*\.json)\b/gi"

    def FileNameReader(self):
        files = [f for f in listdir(self.DataPath) if isfile(join(self.DataPath, f))]
        return files

    def FileProcessor(self):
        files = self.FileNameReader()
        for each in files:
            if each in self.delete:
                remove(f"MyData/{each}")
            # if re.search(self.FilesToKeepCombined, each) != None:
            #     print("hello")