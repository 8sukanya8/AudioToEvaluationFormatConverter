from src.segmentation_formats.RttmEntry import RttmEntry

class LiumMdtmEntry:
    def __init__(self, file_id, channel_id, time_start_in_features, duration_in_features, gender, band_type, env_type, speaker_name):
        """
        :param file_id: file name; basename of the recording minus extension(e.g., rec1_a)
        :param channel_id: channel(1 - indexed) that turn is on; default can be 1
        :param time_start_in_features: onset of turn in seconds from beginning of recording( in features)
        :param duration_in_features: duration of turn( in features)
        :param gender: speaker gender(U=unknown, F=female, M=Male)
        :param band_type: the type of band(T=telephone, S=studio)
        :param env_type: the type of environment(music, speech only, …)
        :param speaker_name: name of speaker of turn; should be unique within scope of each file
        """
        self.file_id = file_id
        self.channel_id = channel_id
        self.time_start_in_features = time_start_in_features
        self.duration_in_features =duration_in_features
        self.gender=gender
        self.band_type = band_type
        self.env_type = env_type
        self.speaker_name =speaker_name

    def get_as_string(self):
        """
        Gets a string representation of the entry
        :return: a string
        """
        return " ".join([str(self.file_id), str(self.channel_id), '{:.3f}'.format(float(self.time_start_in_features)), '{:.3f}'.format(float(self.duration_in_features)),
                         str(self.gender), str(self.band_type), str(self.env_type), str(self.speaker_name)])

    def convert_to_rttm(self, audio_len):
        rttm_entry_obj = RttmEntry(file_id=self.file_id,time_start=self.time_start_in_features/100,
                                   duration= self.duration_in_features/100, speaker_name= self.speaker_name)
        return rttm_entry_obj