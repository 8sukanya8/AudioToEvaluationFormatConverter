
class RttmEntry:
    def __init__(self, file_id, time_start , duration, speaker_name , seg_type = 'SPEAKER', channel_id=1, ortho = "<NA>", conf_score = "<NA>", signal_look_ahead_time = "<NA>", speaker_type = "<NA>"):
        """
        Initialises the Rich Transcription Time Marked (RTTM) entry
        :param seg_type: segment type; should always by SPEAKER
        :param file_id: file name; basename of the recording minus extension (e.g., rec1_a)
        :param channel_id: channel (1-indexed) that turn is on; default can be 1
        :param time_start: onset of turn in seconds from beginning of recording
        :param duration: duration of turn in seconds (from time_start until end of segment)
        :param ortho: orthographic rendering (spelling) of the object for STT object types, should always by <NA>
        :param speaker_type: should always be <NA>
        :param speaker_name:name of speaker of turn; should be unique within scope of each file
        :param conf_score: system confidence (probability) that information is correct; should always be <NA>
        :param signal_look_ahead_time: the time of the last signal sample used in determining the values within the RTTM Object’s fields; should always be <NA>
        """
        self.file_id = file_id
        self.time_start = time_start
        self.duration = duration
        self.speaker_name = speaker_name
        self.seg_type = seg_type
        self.channel_id = channel_id
        self.ortho = ortho
        self.conf_score = conf_score
        self.signal_look_ahead_time = signal_look_ahead_time
        self.speaker_type = speaker_type

    def get_as_string(self):
        """
        Gets a string representation of the entry
        :return: a string
        """
        return " ".join([str(self.seg_type), str(self.file_id), str(self.channel_id), '{:.3f}'.format(float(self.time_start)), '{:.3f}'.format(float(self.duration)), str(self.ortho), str(self.speaker_type), str(self.speaker_name), str(self.conf_score), str(self.signal_look_ahead_time)])

