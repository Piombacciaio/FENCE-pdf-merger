try:
  from colorama import Fore
  from PyPDF2 import PdfMerger
  from tkinter.filedialog import askdirectory
  from tkinter.messagebox import showerror
  import os, PySimpleGUI as PSG, shutil, webbrowser
except ImportError:
  import sys, os, subprocess
  for package in ["colorama", "tabulate", "PyPDF2", "PySimpleGUI"]:
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])
  os.system("cls")
  os.execv(sys.executable, ["python"] + sys.argv)

__filenames__ = ["Finale.pdf","ED32.pdf","ED64.pdf","ED128.pdf","ED256.pdf","Classifica gironi.pdf","Gironi.pdf","Rank.pdf","Società.pdf"]
valid_names = [["Finale.pdf","ED32.pdf","ED64pdf"], ["ED128.pdf","ED256.pdf","Classifica gironi.pdf"], ["Gironi.pdf","Rank.pdf","Società.pdf"]]
headers = [" "*15, "Valid File Names", " "*16]

def main():
  output = window["-OUTPUT-TERMINAL-"]

  merger = PdfMerger()
  category = src_path.split("/")[-1]
  path_original = src_path.rsplit("/", maxsplit=1)[0]
  path_complete = path_original + "/Exports"

  output.update(f"Merging {category}\n", text_color_for_value="green", append=True)
  for pdf in __filenames__:
    file = src_path + "/" + pdf 
    try: merger.append(file, import_outline=False)
    except FileNotFoundError:
      output.update(f"{pdf} does not exists in {category}\n", text_color_for_value="red", append=True)

    except Exception as e: showerror(e)
  
  merger.write(f"{export_path}/{category.upper()}.pdf")
  merger.close()
  
  if not os.path.exists(path_complete): os.mkdir(path_complete)
  shutil.move(src_path, path_complete)
  output.update(f"Merging completed\n", text_color_for_value="green", append=True)


if __name__ == '__main__': 
  #window setup
  PSG.theme("DarkBlack")
  default_view = [
    [
      [PSG.Table(valid_names, headers, justification="left", auto_size_columns=True,header_border_width=0, hide_vertical_scroll=True, num_rows=(3))],
      [PSG.Push()],
      [PSG.Push()],
      [PSG.Text("Export directory "), PSG.InputText(expand_x=True, key="-EXP-DIR-TXT-"), PSG.Button("Choose directory", key="-EXP-DIR-BTN-")],
      [PSG.Text("Source directory"), PSG.InputText(expand_x=True, key="-EXP-SRC-TXT-"), PSG.Button("Choose directory", key="-EXP-SRC-BTN-")],
      [PSG.Push()],
      [PSG.Button("Export", key="-EXP-BTN-"), PSG.Button("Open Export Folder", key="-OPN-EXP-"), PSG.Push(), PSG.Button("Source", key="-OPN-SRC-")],
      [PSG.Push()],
      [PSG.Text("Output")],
      [PSG.Multiline(disabled=True, no_scrollbar=True, autoscroll=True, expand_x=True, auto_refresh=True, size=(1, 5), key="-OUTPUT-TERMINAL-")],
      [PSG.Button("Clear output", key="-CLR-OUT-")]
    ]
  ]

  #path setup
  export_path = os.path.expanduser("~/Desktop").replace("\\", "/")
  src_path = ""
  
  window = PSG.Window(f"Fence Merger | by Piombo Andrea", default_view, finalize=True)
  window["-EXP-DIR-TXT-"].update(export_path)
  
  while True:

    events, values = window.read()

    if events == PSG.WIN_CLOSED: break

    if events == "-EXP-DIR-BTN-":
      export_path = askdirectory(title="Choose export path")
      window["-EXP-DIR-TXT-"].update(export_path)

    if events == "-EXP-SRC-BTN-":
      src_path = askdirectory(title="Choose competition")
      window["-EXP-SRC-TXT-"].update(src_path)

    if events == "-OPN-SRC-":
      webbrowser.open("https://github.com/Piombacciaio/FENCE-pdf-merger")

    if events == "-OPN-EXP-":
      os.startfile(export_path)

    if events == "-CLR-OUT-":
      window["-OUTPUT-TERMINAL-"].update("")

    if events == "-EXP-BTN-":
      export_path = values["-EXP-DIR-TXT-"].strip()
      src_path = values["-EXP-SRC-TXT-"].strip()
      if export_path == "" or src_path == "":
        showerror("", "Paths can't be empty")
      else: main()
