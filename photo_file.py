class PhotoFile(object):
    def __init__(self, filename, date_time, trip_key):
        self.filename = filename
        self.date_time = date_time
        self.trip_key = trip_key

    def get_filename(self):
        return self.filename

    def get_new_filename(self):
        return self.new_name

    def get_dir_name(self):
        ret_val =  self.date_time.__str__().split(" ")[0].replace('-', '_')
        return ret_val

    @property
    def reformat_date_time(self):
        ret_str = ""
        count = 1
        split_arr = self.date_time.__str__().split(" ")
        for this_str in split_arr:
            new_str = this_str.replace(':','_')
            new_str = new_str.replace('-', '_')
            ret_str = ret_str + new_str
            if count < len(split_arr):
                ret_str += "_"
            count += 1

        return ret_str

    def set_new_name(self, number):
        self.new_name = "{}_{}_{}".format(self.trip_key,
                                          number,
                                          self.reformat_date_time)

    def __lt__(self, other):
        return self.date_time < other.date_time

    def __gt__(self, other):
        return self.date_time > other.date_time

    def __str__(self):
        return "Filename: {}, DateTime: {}, NewName: {}".format(self.filename,
                                                                self.date_time,
                                                                self.new_name)