import os

def text_to_speech(text, output_path_location="output.mp3", subtitle_path_location="output.srt"):
    voice = "en-CA-LiamNeural"  
    command = f"edge-tts --voice \"{voice}\" --text \"{text}\" --write-media \"{output_path_location}\" --write-subtitles \"{subtitle_path_location}\""
    os.system(command)
    
    with open(subtitle_path_location, 'r') as file:
        lines = file.readlines()
    with open(subtitle_path_location, 'w') as file:
        file.writelines(lines[4:])
    
    return output_path_location, subtitle_path_location