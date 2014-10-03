import os,glob,argparse
parser=argparse.ArgumentParser()
parser.add_argument("-path",help="Path of where you want to search",type=str)
parser.add_argument("-types",help="Which types you want to search for",type=str)
parser.add_argument("-v",help="Viggo mode",action="store_true")
args=parser.parse_args()
if args.v:
    print("Launching in VIGOO-MODE!!!")
print("Directory scanner, at your service!")
if not args.path:
    print("Please enter the full path to the directory, you want to scan:")
    found=False
    while not found:
       try:
            os.chdir(input())
            found=True
       except:
            print("Not found!")
else:
    print("Finding directory via commandline input:")
    try:
        os.chdir(args.path)
    except:
        print("Fatal error: couldn't find path ("+args.path+")")
        exit()
print("Succesfully opened directory!")
if args.v:
    print("Filetypes via VIGGO-MODE")
    search=["txt","py"]
elif not args.types:
    print("Write each filetype, you want to search for on a new line:")
    print("(Send an empty line to stop)")
    tmp="meh"
    search=[]
    while True:
        tmp=input()
        if tmp=="":
            break
        search.append(tmp)
else:
    print("Inputting file types via commandline!")
    search=args.types.split()
print("Seacrhing for filetypes:",search)
files=[]
for f in search:
    files.append(glob.glob("*."+f))
print("Found",len(files)," of the file types!")
print("Files found:")
print("------------")
for t in search:
    print(t+": (Total",str(len(files[search.index(t)]))+")")
    for f in files[search.index(t)]:
        print("\t"+f)
print("------------")
input("Press enter to continue!")