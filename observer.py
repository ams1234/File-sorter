from .subject import subject
import os, shutil
class observer(object):
    USER_NAME = 'ams'
    def __init__(self):
        self.fileType_dict_map = {
            ".exe": "D:\\downloaded_Softwares",
            ".zip":"D:\\downloaded_zipfiles",
            ".pdf":"D:\\downloaded_pdf"
        }
        self.DOWNLOAD_DIR = "D:\\userdata\\{}\\Downloads".format(observer.USER_NAME)

    def update(self, state):
        if state:
            self.state_change_action()
        else:
            print("Something went wrong")

    def state_change_action(self):
        try:
            for f in os.listdir(self.DOWNLOAD_DIR):
                if f.endswith(".exe"):
                    print("i am here")
                    self.file_sorter(f, ".exe")
                elif f.endswith(".zip"):
                    print("i am here")
                    self.file_sorter(f, ".zip")
                elif f.endswith(".pdf"):
                    print("i am here")
                    self.file_sorter(f, ".pdf")
                else:
                    self.file_sorter(f)
        except Exception():
            print("Error in handling directories")

    def file_sorter(self,  file, filetype=""):
        if not os.path.exists(self.fileType_dict_map[filetype]):
            os.mkdir(self.fileType_dict_map[filetype])
        shutil.move(self.DOWNLOAD_DIR+"\\{}".format(file),self.fileType_dict_map[filetype]+"{}".format(file))

