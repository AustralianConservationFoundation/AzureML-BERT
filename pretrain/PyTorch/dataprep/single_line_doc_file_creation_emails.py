import glob
import os
import sys
import re

sys.path.append("..")

# import importlib
# emailclean = importlib.import_module("emailclean", "../emailclean.pyc")
import email_clean
from tqdm import tqdm
import fileinput

output_file = '/mnt/d/bert-pretrain/emails/97f0f7a9-a894-4697-860f-c30ba34ce916/emails2.txt'

with open(output_file, "w") as ofile:
  for dirname in glob.glob('/mnt/d/bert-pretrain/emails/97f0f7a9-a894-4697-860f-c30ba34ce916/Extracted_text_files/*/', recursive=False):
    for filename in glob.glob(dirname + '*', recursive=True):
      print(filename)
      article_lines = []
      article_open = False
      
      with open(filename, "r") as file:
        lines = file.readlines()
        mystr = email_clean.clean_email(' '.join([line.rstrip() for line in lines if line.rstrip()]))
        if mystr:
            # processes_string = re.sub(' +', ' ', mystr.strip())
            ofile.write(mystr)
            ofile.write("\n\n")

          # else:
          #   if article_open:
          #     article_lines.append(line)
