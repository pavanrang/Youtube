import os
import srt_equalizer
import assemblyai as aai
from termcolor import colored

def generate_subtitles(audio_path: str, ASSEMBLY_AI_API_KEY: str, directory: str =  "./subtitles") -> str:
   
    def equalize_subtitles(srt_path: str, max_chars: int = 10) -> None:
      srt_equalizer.equalize_srt_file(srt_path, srt_path, max_chars)
    print(ASSEMBLY_AI_API_KEY)
    aai.settings.api_key = ASSEMBLY_AI_API_KEY
    transcriber = aai.Transcriber()
    transcript = transcriber.transcribe(audio_path)
    os.makedirs(directory, exist_ok=True) 
    subtitles_path = f"{directory}/audio.srt"
    subtitles = transcript.export_subtitles_srt()
    with open(subtitles_path, "w") as f:
        f.write(subtitles)
    equalize_subtitles(subtitles_path)
    print(colored("[+] Subtitles generated.", "green"))
    return subtitles_path

