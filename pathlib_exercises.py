"""1. Scrie un script care creeaza un fisier text. In fisierul text trebuie sa se regaseasca
o lista cu toate fisierele dll din directoru C:\Windows\System32"""

from pathlib import Path
#
# ROOT = Path("C:\Windows\System32")
#
# with open("exercitiul1.txt", "w") as fisier:
#     for path in ROOT.glob("**/*.dll"):
#         fisier.write(f"{path}\n")


"""2. Scrie un script care afiseaza cu cate secunde in urma a fost adaugat ceva in folderul Downloads."""

# DOWNLOADS_DIR = Path.home() / "Downloads"
#
# initial_time_delta = DOWNLOADS_DIR.stat().st_mtime
#
# while True:
#     if DOWNLOADS_DIR.stat().st_mtime != initial_time_delta:
#         initial_time_delta = DOWNLOADS_DIR.stat().st_mtime
#         print("s-a modificat")



"""3. Scrie o functie care afiseaza un mesaj de salut. Mesajul de salut trebuie sa contina numele utilzatorului
curent (se obtine cu modulul os) si cati GB (cu doua zecimale) ocupa directorul home. Ex: Salut mdinu!
Spatiu utilizat de tine: 4.55 GB"""

# import os
#
#
# def say_hello():
#     """Returns the `directory` size in gigabytes."""
#
#     USER_ROOT = Path("C:\\Users\\" + os.getlogin())
#     size = 0
#     for path in USER_ROOT.glob("**\*"):
#         size += path.stat().st_size
#
#     print(f"Salut {os.getlogin()}! Spatiul utilizat de tine: {round(size/10**9,2)} GB.")
#
# say_hello()


"""4. Scrie un script care face curatenie pe desktop. Cand executi scriptul toate fisierele (mai putin shortcuts)
vor fi mutate intr-un folder denumit de forma 2022-10-30_11-20 (ora data curenta). Noul folder creat
va sta intr-un folder definit de utilizator intr-un fisier de configurare. Fisierul de config se gaseste
pe acelasi nivel ca si scriptul si contine pe prima linie calea catre folderul parinte al arhivei."""


# from datetime import datetime
# import shutil
#
# DESKTOP_PATH = Path(r"C:\Users\Cristi\Desktop\New desktop")
# ROOT = Path(__file__).parent
# CONFIG_PATH = ROOT / "config.txt"
# current_date = datetime.now()
# folder_name = current_date.strftime("%Y-%m-%d_%H-%M-%S")
#
# try:
#     with CONFIG_PATH.open() as fin:
#         content = fin.readline()
#         content = content.strip("\n")
# except OSError as err:
#     ARCHIVE_PATH = Path(r"C:\Archive")
#     print(f"Error {err}")
# else:
#     ARCHIVE_PATH = Path(content)
#
# ARCHIVE_PATH.mkdir(exist_ok=True)
#
# FOLDER_PATH = ARCHIVE_PATH / folder_name
#
#
# try:
#     shutil.copytree(DESKTOP_PATH,FOLDER_PATH)
# except FileExistsError:
#     print("Backup-ul a fost deja efectuat! Incearca peste 1 minut!")
# else:
#     print("Backup complet!")


"""5. Afiseaza cate ore au trecut din acest an."""

# from datetime import datetime
#
# initial_date = "01/01/2022"
# delta_time = datetime.now()-datetime.strptime(initial_date, "%d/%m/%Y")
# print(delta_time.total_seconds()/3600)


"""7. PROIECT: Downloads folder watcher
Pe acelasi nivel cu directorul Downloads se creeaza un director DownloadsClean, in el se creeaza
folderele Music, Pictures, Videos, Documents, Executables, Others. (automat la pornirea scriptului)
Scriptul urmareste folderul Downloads al uilizatorul curent.
La fiecare modificare se citeste continutul si apoi se face clasificarea si mutarea."""


import shutil
from pathlib import Path
import time
import os

DOWNLOAD_CLEAN =  Path.home() / "Downloads Clean"
DOWNLOAD_DIR = Path.home() / "Downloads"
MUSIC_DIR = DOWNLOAD_CLEAN / "Music"
PICTURE_DIR = DOWNLOAD_CLEAN / "Pictures"
VIDEO_DIR = DOWNLOAD_CLEAN / "Video"
EXE_DIR = DOWNLOAD_CLEAN / "Apps"
OTHERS_DIR = DOWNLOAD_CLEAN / "Others"

DOWNLOAD_CLEAN.mkdir(exist_ok=True, parents=True)
MUSIC_DIR.mkdir(exist_ok=True, parents=True)
PICTURE_DIR.mkdir(exist_ok=True, parents=True)
VIDEO_DIR.mkdir(exist_ok=True, parents=True)
EXE_DIR.mkdir(exist_ok=True, parents=True)
OTHERS_DIR.mkdir(exist_ok=True, parents=True)


initial_time_delta = DOWNLOAD_DIR.stat().st_mtime
initial_size = 0
final_size = 0


while True:
    if DOWNLOAD_DIR.stat().st_mtime != initial_time_delta:
        initial_time_delta = DOWNLOAD_DIR.stat().st_mtime
        for path in DOWNLOAD_DIR.glob("**/*"):
            while True:
                for path in DOWNLOAD_DIR.glob("**/*"):
                    initial_size = path.stat().st_size
                    time.sleep(2)
                for path in DOWNLOAD_DIR.glob("**/*"):
                    final_size = path.stat().st_size
                print(initial_size, final_size)
                if initial_size != final_size:
                    continue
                else:
                    break
            if path.suffix in [".mp3", ".wma", ".aac"]:
                shutil.move(path, MUSIC_DIR)
            elif path.suffix in [".jpg", ".jpeg", ".png"]:
                shutil.move(path, PICTURE_DIR)
            elif path.suffix in [".mpg", ".mkv", ".flv", ".avi", ".gif", ".mov", ".wmv", ".mp4"]:
                shutil.move(path, VIDEO_DIR)
            elif path.suffix in [".exe"]:
                shutil.move(path, EXE_DIR)
            else:
                shutil.move(path, OTHERS_DIR)
