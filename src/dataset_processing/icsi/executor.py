import os
from fnmatch import filter
import xml.etree.ElementTree as ET
from src.segmentation_formats.RttmEntry import RttmEntry
from src.file_io import write_file


input_directory = "/Users/sukanyanath/Documents/PhD/Internship_Spinning_Bytes/Datasets/Diarization/ICSI/ICSI_transcripts/Segments"
output_directory = "/Users/sukanyanath/Documents/PhD/Internship_Spinning_Bytes/Datasets/Diarization/ICSI/ICSI_transcripts/rttm2"


def execute_isci_dataset_to_rttm_file(input_directory, output_directory):
    """
    Executes the conversion of the icsi_dataset into rttm files
    :param input_directory: directory of all author segment files
    :param output_directory: output directory for the rttm files
    :return: None
    """
    if os.path.isdir(input_directory) and os.path.exists(input_directory):
        file_segments_dict = get_audio_file_segments_dict(input_directory)
        convert_audio_file_segments_to_rttm_file(file_segments_dict, input_directory, output_directory)
    else:
        print("Error! path does not exist ", input_directory)


def get_audio_file_segments_dict(input_directory):
    """
    Given an input directory of author segment files of each audio, get a dictionary with keys as audio file name
     and value as the list of  corresponding author segment files
    :param input_directory: directory of all author segment files
    :return: dictionary of audio file names and corresponding author segments
    """
    all_segments = filter(os.listdir(input_directory),pat="*.xml")
    file_segments_dict ={}
    for segment_file in all_segments:
        fields = segment_file.split(".")
        audio_file_name = fields[0]
        if audio_file_name in file_segments_dict:
            corresponding_segments = file_segments_dict[audio_file_name]
            corresponding_segments.append(segment_file)
            file_segments_dict[audio_file_name] = corresponding_segments
        else:
            file_segments_dict[audio_file_name] = [segment_file]
    return file_segments_dict

def convert_audio_file_segments_to_rttm_file(file_segments_dict, input_directory, output_directory):
    """
    Given a dictionary of audio file and its segments, output corresponding rttm file for each audio.
    :param file_segments_dict: dictionary of audio file names and corresponding author segments
    :param input_directory: directory of all author segment files
    :param output_directory: output directory for the rttm files
    :return: None
    """
    for audio_file_name in file_segments_dict.keys():
        author_segments = file_segments_dict[audio_file_name]
        print(audio_file_name, author_segments)
        rttm_list = []
        for segment in author_segments:
            rttm_list = rttm_list + read_xml_into_rttm_list(audio_file_name, input_directory+"/"+segment)
        sort_rttm_list_by_time_start(rttm_list)
        output_file_path = output_directory + "/" + audio_file_name + ".txt"
        write_file(rttm_list, output_file_path)


def read_xml_into_rttm_list(audio_file_name, xml_file_path):
    """
    Given a segment xml file, convert it into a list of rttm objects
    :param audio_file_name: name of the audio, required for creating an rttm object
    :param xml_file_path: segment xml file path
    :return: a list of rttm items
    """
    tree = ET.parse(xml_file_path)
    root = tree.getroot()
    rttm_list = []
    for child in root.getchildren():
        if len(child.attrib) > 0 :
            file_id = audio_file_name
            time_start = float(child.attrib['starttime'])*100
            duration = (float(child.attrib['endtime']) - float(child.attrib['starttime']))*100
            speaker_name = child.attrib['participant']
            rttm_entry_obj = RttmEntry(file_id=file_id, time_start=time_start, duration=duration,
                                       speaker_name=speaker_name)
            rttm_list.append(rttm_entry_obj)
    return rttm_list


def sort_rttm_list_by_time_start(rttm_list):
    """
    sort the list of rttm entry objects by the time_start tag
    :param rttm_list:
    :return:
    """
    return rttm_list.sort(key=lambda x: float(x.time_start))

