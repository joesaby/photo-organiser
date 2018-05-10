import os
import datetime

root_dir = "/Users/joseseba/Photos/2018_May_Swiss/"

def print_date(ts_epoch):
    ts = datetime.datetime.fromtimestamp(ts_epoch).strftime('%Y-%m-%d %H:%M:%S')
    return ts

def main():
    for folder, subs, files in os.walk(root_dir):
        print "folder: {}".format(folder)
        print "subs: {}".format(subs)
        print "files: {}".format(files)
        for file in files:
            st = os.stat(root_dir.format(file))
            print "file: [{}], st_atime: [{}], st_mtime: [{}], st_ctime: [{}]".format(file,
                                                                                      print_date(st.st_atime),
                                                                                      print_date(st.st_mtime),
                                                                                      print_date(st.st_ctime))

if __name__ == "__main__":
    main()