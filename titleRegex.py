#!/bin/bash

import re
import subprocess
from subprocess import Popen, PIPE, STDOUT

list = open("./businessTitlesShort.txt", "r")
newList = open("./newList.txt", "w")

articles = re.compile(r"\bof \b|\bby \b|\bat \b|\bthe \b|\bat \b|\ban \b|\bas \b|\bbefore \b|\bbut \b|\bby \b|\bfor \b|\bfrom \b|\bis \b|\bin \b|\binto \b|\blike \b|\w\bof\b\w|\boff \b|\bon \b|\bonto \b|\bper \b|\bsince \b|\bthan \b|\bthis \b|\bthat \b|\bto \b|\bup \b|\bvia \b|\bwith \b|[\.\(\):\!'+|&@\/]", re.IGNORECASE)
spaces = re.compile(r"\s|,\s")
dashes = re.compile(r"\b---\b|\b--\b|\b-&-\b|\b- \b|-\|-")

def writeNewList(t):
    newList.write(t + "\n")
    return

with open("businessTitles.txt") as list:
  for line in list:
      orgLine = line.split("\n")[0]
      title = line.split(",", 1)[1]
      newTitle = articles.sub("", title)
      newTitle = spaces.sub("-", newTitle)
      newTitle = dashes.sub("-", newTitle)
      newLine = orgLine + "," + newTitle[:-1]
      writeNewList(newLine)

list.close()
newList.close()
