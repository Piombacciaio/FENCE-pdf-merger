from colorama import Fore
from PyPDF2 import PdfMerger
from tabulate import tabulate
from tkinter.filedialog import askdirectory
from tkinter.messagebox import showinfo
import colorama, ctypes, os, shutil

__filenames__ = ["Finale.pdf","ED32.pdf","ED64.pdf","ED128.pdf","ED256.pdf","Classifica gironi.pdf","Gironi.pdf","Rank.pdf","Società.pdf"]
valid_names = [["Finale.pdf","ED32.pdf","ED64.pdf"],["ED128.pdf","ED256.pdf","Classifica gironi.pdf"],["Gironi.pdf","Rank.pdf","Società.pdf"]]
def main():
  
  merger = PdfMerger()
  showinfo("", "Choose directory of finished competition or press 'cancel' to quit")
  path = askdirectory(title="Choose competition")
  if path == "": quit(0)
  category = path.split("/")[-1]
  path_original = path.rsplit("/", maxsplit=1)[0]
  path_complete = path_original + "/Classifiche Complete"

  print(f"[{Fore.GREEN}+{Fore.RESET}] Merging {category}")
  for pdf in __filenames__:
    file = path + "/" + pdf 
    try: merger.append(file, import_outline=False)
    except FileNotFoundError: print(f"[{Fore.RED}-{Fore.RESET}] {pdf} does not exists in {category}")
    except Exception as e: print(f"[{Fore.GREEN}-{Fore.RESET}] Error: {e}")
  
  merger.write(f"{website_path}/{category}.pdf")
  merger.close()
  
  if not os.path.exists(path_complete): os.mkdir(path_complete)
  shutil.move(path, path_complete)

if __name__ == '__main__': 
  #window setup
  colorama.init()
  ctypes.windll.kernel32.SetConsoleTitleW(f'Fence Merger')
  #prints
  print(f"[{Fore.GREEN}+++{Fore.RESET}] Fence Merger | by Piombo Andrea [{Fore.GREEN}+++{Fore.RESET}]\n")
  print(tabulate(valid_names, [f"{Fore.GREEN}Valid File Names{Fore.RESET}", "", ""], "fancy_grid") + "\n")
  #path setup
  showinfo("", "Choose directory for web publication of results")
  website_path = askdirectory(title="Choose web publishing path")

  while True:
    main()
    print(f"[{Fore.GREEN}+{Fore.RESET}] Merge completed\n")
    