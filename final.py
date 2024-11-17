import os
from moviepy.editor import VideoFileClip, AudioFileClip, CompositeVideoClip, TextClip
from moviepy.video.tools.subtitles import SubtitlesClip


def generate_video(combined_video_path, tts_path, subtitles_path, output_file_name="./temp/output_with_audio_subs.mp4"):
    """
    Generates a video by combining video, audio, and subtitle files.
    
    Args:
        combined_video_path (str): Path to the video file.
        tts_path (str): Path to the audio file.
        subtitles_path (str): Path to the subtitles file (in SRT format).
        output_file_name (str): Path to save the generated output video.
    
    Raises:
        FileNotFoundError: If any of the input files are not found.
        ValueError: If there is an issue processing subtitles or generating the video.
    """
    # Check input files
    for file_path, name in [
        (combined_video_path, "Video"),
        (tts_path, "Audio"),
        (subtitles_path, "Subtitles"),
    ]:
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"{name} file not found: {file_path}")
    
    try:
        # Subtitle generator function
        def generator(txt):
            return TextClip(
                txt,
                font="./fonts/bold_font.ttf",
                fontsize=100,
                color="#FFFF00",
                stroke_color="black",
                stroke_width=5,
            )

        # Load subtitles
        subtitles = SubtitlesClip(subtitles_path, generator)

        # Load video and overlay subtitles
        video = VideoFileClip(combined_video_path)
        video_with_subtitles = CompositeVideoClip([video, subtitles.set_pos(("center", "center"))])

        # Add audio
        audio = AudioFileClip(tts_path)
        final_video = video_with_subtitles.set_audio(audio)

        # Write final video to output
        final_video.write_videofile(output_file_name, threads=3, codec="libx264", audio_codec="aac")
        print(f"Video successfully generated: {output_file_name}")

    except Exception as e:
        raise ValueError(f"An error occurred while generating the video: {e}")


# # Example usage
# if __name__ == "__main__":
#     try:
#         generate_video(
#             "./temp/combined_video.mp4",  # Path to the combined video
#             "output.mp3",                 # Path to the audio file
#             "output.srt"                  # Path to the subtitles file
#         )
#     except Exception as e:
#         print(f"Error: {e}")
