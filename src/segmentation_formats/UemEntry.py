class UemEntry:
    def __init__(self, file_id, channel_id, time_start, time_end):
        """
        Initialises the Un-partitioned evaluation map (UEM) entry
        :param file_id: file name; basename of the recording minus extension(e.g., rec1_a)
        :param channel_id: channel(1 - indexed) that scoring region is on; ignored by score.py
        :param time_start: onset of scoring region in seconds from beginning of recording
        :param time_end: offset of scoring region in seconds from beginning of recording
        """
        self.file_id = file_id
        self.channel_id = channel_id
        self.time_start = time_start
        self.time_end = time_end

    def get_as_string(self):
        """
        Gets a string representation of the entry
        :return: a string
        """
        return " ".join([str(self.file_id), str(self.channel_id), '{:.3f}'.format(float(self.time_start)), '{:.3f}'.format(float(self.time_end))])
