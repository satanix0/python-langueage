import os
import urllib.request

ft_choice = int(input(
    """Enter 1 to download a raw File \nEnter 2 to download a whole directory\nENTER: """))


def rawFile():
    file_path = input("Paste the file URL: ")
    try:
        name = file_path.split("/")[-1]
        urllib.request.urlretrieve(file_path, filename=name)
        print("Downloaded Successfully")
    except Exception:
        print("Download Failed Error occurred")
        print(Exception.__str__)


def directoryDownload():
    fldr_path = input("Paste the folder URL: ")
    try:
        os.system('gitdir ' + fldr_path)
        print("Downloaded Successfully")
    except Exception:
        print("Download Failed Error occurred")
        print(Exception.__str__)


match ft_choice:
    case 1:
        rawFile()
    case 2:
        directoryDownload()
    case default:
        print("Wrong Input")
