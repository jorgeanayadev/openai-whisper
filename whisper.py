import sys
import os
import argparse
import openai
import json
from enum import Enum


class ResponseFormat(Enum):
    json = 1
    verbose_json = 2
    text = 3
    srt = 4
    vtt = 5


def format_type(value):
    try:
        return ResponseFormat[value.lower()]
    except KeyError:
        raise argparse.ArgumentTypeError(f"Invalid format response: '{value}'. Allowed values are {', '.join(fmt.name for fmt in ResponseFormat)}.")


def transcribe_audio(api_key, audio_file, response_format):
    openai.api_key = api_key
    audio_data = open(audio_file, "rb")

    transcript = openai.Audio.transcribe("whisper-1", audio_data, response_format=str(response_format))

    if "json" in response_format:
        transcript_data = json.dumps(transcript, indent=2)
    else:
        transcript_data = transcript

    transcript_file = os.path.splitext(audio_file)[0] + "." + response_format
    with open(transcript_file, "w") as f:
        f.write(transcript_data)

    return transcript_file


def main():
    if len(sys.argv) != 4:
        print("Usage: python whisper_to_subtitles.py <API_KEY> <AUDIO_FILE> <FORMAT_RESPONSE>")
        sys.exit(1)

    api_key = sys.argv[1]
    audio_file = sys.argv[2]
    response_format = format_type(sys.argv[3]).name

    subtitle_file = transcribe_audio(api_key, audio_file, response_format)

    print(f"Speech to Text file created: {subtitle_file}")


if __name__ == "__main__":
    main()
