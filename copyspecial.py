#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

import sys
import re
import os
import shutil
import subprocess

"""Copy Special exercise
"""

# +++your code here+++
# Write functions and modify main() to call them

def get_path(directory):
  result = []
  paths = os.listdir(directory)
  for filename in paths:
    match = re.search(r'__(\w+)__', filename)
    if match:
      result.append(os.path.abspath(os.path.join(directory, filename)))
  return (result)


def Copy(paths, to_dir):
  print("Poda")
  if not os.path.exists(to_dir):
    os.mkdir(to_dir)
  for path in paths:
    fname = os.path.basename(path)
    new_p = os.path.join(to_dir, fname)
    shutil.copy(path, new_p)

def Zip(paths, zipfile):
  print("Poda")
  Copy(paths, zipfile)
  print("Poda")
  Command = ('powershell.exe Compress-Archive -LiteralPath '+ zipfile + ' -DestinationPath ' + zipfile  )
  os.system(Command)

def main():
  # This basic command line argument parsing code is provided.
  # Add code to call your functions below.

  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]
  if not args:
    print("usage: [--todir dir][--tozip zipfile] dir [dir ...]")
    sys.exit(1)

  # todir and tozip are either set from command line
  # or left as the empty string.
  # The args array is left just containing the dirs.
  todir = ''
  if args[0] == '--todir':
    todir = args[1]
    del args[0:2]

  tozip = ''
  if args[0] == '--tozip':
    tozip = args[1]
    del args[0:2]

  if len(args) == 0:
    print("error: must specify one or more dirs")
    sys.exit(1)

  # +++your code here+++
  # Call your functions
  paths = []
  for directory in args:
    paths.extend(get_path(directory))

  if todir:
    Copy(paths, todir)
  elif tozip:
    Zip(paths, tozip)
  else:
    print('\n'.join(paths))

if __name__ == "__main__":
  main()
