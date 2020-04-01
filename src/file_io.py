from src.segmentation_formats.RttmEntry import RttmEntry
from src.segmentation_formats.UemEntry import UemEntry
from src.segmentation_formats.LiumMdtmEntry import  LiumMdtmEntry

def read_file(file_path, format):
    if format not in ["uem", "rttm", "mdtm"]:
        print("Error! Format can be either uem, rttm or mdtm only")
        return
    f = open(file_path, "r")
    segment_list = []
    for line in f:
        fields = line.split(" ")
        if len(fields)>1:
            if format == "uem":
                if len(fields)==4:
                    file_id = fields[0]
                    channel_id = fields[1]
                    time_start = fields[2]
                    time_end = fields[3]
                    segment = UemEntry(file_id=file_id, channel_id=channel_id, time_start=time_start,
                                       time_end=time_end)
                    segment_list.append(segment)
                else:
                    print("No object created. Not sufficient fields for UEM: ", fields)
            elif format == "rttm":
                if len(fields) == 10:
                    seg_type = fields[0]
                    file_id = fields[1]
                    channel_id = fields[2]
                    time_start = fields[3]
                    duration = fields[4]
                    ortho = fields[5]
                    speaker_type = fields[6]
                    speaker_name = fields[7]
                    conf_score = fields[8]
                    signal_look_ahead_time = fields[9]
                    segment = RttmEntry(seg_type=seg_type, file_id=file_id, channel_id=channel_id,
                                        time_start=time_start, duration=duration, ortho=ortho,
                                        speaker_type=speaker_type, speaker_name=speaker_name,
                                        conf_score=conf_score, signal_look_ahead_time=signal_look_ahead_time)
                    segment_list.append(segment)
                else:
                    print("No object created. Not sufficient fields for RTTM: ", fields)
            elif format == "mdtm":
                if len(fields) == 8:
                    file_id= fields[0]
                    channel_id = fields[1]
                    time_start_in_features =fields[2]
                    duration_in_features=fields[3]
                    gender=fields[4]
                    band_type=fields[5]
                    env_type=fields[6]
                    speaker_name=fields[7]
                    segment= LiumMdtmEntry(file_id = file_id, channel_id = channel_id,
                                            time_start_in_features = time_start_in_features,
                                            duration_in_features = duration_in_features, gender = gender,
                                            band_type = band_type, env_type = env_type,
                                            speaker_name = speaker_name)
                    segment_list.append(segment)
                else:
                    print("No object created. Not sufficient fields for MDTM: ", fields)
        else:
            print("Unidentified file format ",format," in line ", line)
    f.close()
    return segment_list


def write_file(segmentation_format_list, file_path):
    f = open(file_path, "w")
    contents = ""
    for item in segmentation_format_list:
        contents = contents + item.get_as_string() + "\n"
    f.write(contents)
    f.close()

