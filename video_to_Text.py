import os
import whisper
from moviepy import VideoFileClip

# Load Whisper model only once when the app starts
model = whisper.load_model("base")


def extract_audio(video_path, audio_path):
    """
    Extract audio from the uploaded video.
    """

    video = VideoFileClip(video_path)
    video.audio.write_audiofile(
        audio_path,
        logger=None
    )


def transcribe_video(video_path):
    """
    Convert video to text.
    """

    audio_path = "outputs/audio.wav"

    os.makedirs("outputs", exist_ok=True)

    # Step 1
    extract_audio(video_path, audio_path)

    # Step 2
    result = model.transcribe(
        audio_path,
        fp16=False
    )

    return result["text"]