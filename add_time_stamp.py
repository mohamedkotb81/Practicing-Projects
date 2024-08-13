import re
import elementpath
import xml.etree.ElementTree as ET

def parse_vtt(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # Regex to match VTT timestamps and text
    pattern = re.compile(r'(\d{2}:\d{2}:\d{2}\.\d{3}) --> (\d{2}:\d{2}:\d{2}\.\d{3})\s+(.+)')
    matches = pattern.findall(content)

    # Create a list of tuples with (start_time, end_time, text)
    vtt_data = [(start, end, text.strip()) for start, end, text in matches]
    return vtt_data

def add_time_to_xml(vtt_data, xml_file_path, output_file_path):
    tree = ET.parse(xml_file_path)
    root = tree.getroot()

    for start_time, end_time, vtt_text in vtt_data:
        for element in root.iter():
            if element.text and vtt_text in element.text:
                element.set('start_time', start_time)
                element.set('end_time', end_time)

    tree.write(output_file_path, encoding='utf-8', xml_declaration=True)


vtt_file_path = 'D:\Tutorial\Project\Zidan\Input\982143289725_ar.vtt'
xml_file_path = 'D:\Tutorial\Project\Zidan\Input\982143289725_ar.xml'
output_xml_path = 'D:\Tutorial\Project\Zidan\Input\output.xml'

vtt_data = parse_vtt(vtt_file_path)
add_time_to_xml(vtt_data, xml_file_path, output_xml_path)