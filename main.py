import os, sys
import exifread
from datetime import datetime
from photo_file import PhotoFile

def sort_fn(unsorted_list):
    sorted_list = unsorted_list
    for outer_idx, outer_val in enumerate(sorted_list):
        min_val = outer_val
        min_val_idx = outer_idx
        for inner_idx, inner_value in enumerate(sorted_list[outer_idx:]):
            if inner_value < min_val:
                min_val_idx = outer_idx + inner_idx
                min_val = inner_value
        sorted_list[min_val_idx] = outer_val
        sorted_list[outer_idx] = min_val

    for tr in sorted_list:
        print tr


def read_files_from_dir(root_dir, trip_key):
    file_date_list = []
    for folder, subs, files in os.walk(root_dir):
        for file in files:
            f = open("{}{}".format(root_dir, file), 'rb')
            tags = exifread.process_file(f)
            dT = tags.get("EXIF DateTimeOriginal")
            if dT is not None:
                photo_timestamp=datetime.strptime('{}'.format(dT),'%Y:%m:%d %H:%M:%S')
                file_date_list.append(PhotoFile(file,
                                                photo_timestamp,
                                                trip_key))
    sort_fn(file_date_list)


def main(argv):
    if argv == []:
        print "Expected args - folder_name, trip_name"
        sys.exit(0)
    print argv
    trip_name = argv[0]
    root_dir = argv[1]
    read_files_from_dir(root_dir, trip_name)



if __name__ == "__main__":
    main(sys.argv[1:])