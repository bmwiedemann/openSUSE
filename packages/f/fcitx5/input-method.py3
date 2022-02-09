#!/usr/bin/python3

from os import listdir
from os.path import isdir, isfile, join

def get_input_methods():
  mypath = "/etc/X11/xim.d/en"
  files = []
  if isdir(mypath):
    files = [f for f in listdir(mypath) if isfile(join(mypath, f))]
  if not files:
    mypath = "/usr/etc/X11/xim.d/en"
    if isdir(mypath):
      files = [f for f in listdir(mypath) if isfile(join(mypath, f))]
  return files

def get_current_input_method():
  i = 0
  j = 0
  s = ""
  m = get_input_methods()
  if not m:
    return s
  for im in m:
    arr = im.split('-')
    if j == 0:
      i = arr[0]
      s = arr[1]
      j+=1
      continue
    if int(arr[0]) < i:
      i = arr[0]
      s = arr[1]
      j+=1
  return s

print("INPUT_METHOD={}".format(get_current_input_method()))
