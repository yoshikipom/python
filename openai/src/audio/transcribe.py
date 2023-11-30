from pathlib import Path

from openai import OpenAI

openai = OpenAI()
speech_file_path = Path("./test_data/speech.mp3")


def main() -> None:
    audio = openai.audio
    
    # Create transcription from audio file
    transcription = audio.transcriptions.create(
        model="whisper-1", file=speech_file_path, language='ja')
    print(transcription.text)


if __name__ == "__main__":
    main()
