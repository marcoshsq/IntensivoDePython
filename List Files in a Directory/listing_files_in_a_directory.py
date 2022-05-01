from os import listdir
from os.path import isfile, join

list_file =  [f for f in listdir("\Users") if isfile(join("\Users", f))]
