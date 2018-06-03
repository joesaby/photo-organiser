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
    return sorted_list

def read_and_sort_files_from_dir(root_dir, trip_key):
    file_date_list = []
    for folder, subs, files in os.walk(root_dir):
        for read_file in files:
            f = open("{}{}".format(root_dir, read_file), 'rb')
            tags = exifread.process_file(f)
            datetime_original = tags.get("EXIF DateTimeOriginal")
            if datetime_original is not None:
                photo_timestamp=datetime.strptime('{}'.format(datetime_original),'%Y:%m:%d %H:%M:%S')
                file_date_list.append(PhotoFile(read_file,
                                                photo_timestamp,
                                                trip_key))
    return sort_fn(file_date_list)

def reformat_files(sorted_list):
    count = 1
    for photo_file in sorted_list:
        photo_file.set_new_name(count)
        count += 1

def prepare_linux_script(root_dir, sorted_list):
    lnx_command_list = []
    for photo_file in sorted_list:
        cmd =  "cp {}{} {}{}/{}.jpg".format(root_dir,
                                           photo_file.get_filename(),
                                           root_dir,
                                           photo_file.get_dir_name(),
                                           photo_file.get_new_filename())
        lnx_command_list.append(cmd)
    return lnx_command_list


def main(argv):
    if argv == []:
        print "Expected args - folder_name, trip_name"
        sys.exit(0)
    print argv
    trip_name = argv[0]
    root_dir = argv[1]

    sorted_list = read_and_sort_files_from_dir(root_dir, trip_name)
    reformat_files(sorted_list)
    cmd_list = prepare_linux_script(root_dir, sorted_list)


if __name__ == "__main__":
    main(sys.argv[1:])