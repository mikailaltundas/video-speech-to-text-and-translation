import os
from transformers import pipeline

def transcribe_and_translate_videos(folder):
    """
    Processes all .mp4 files in the given folder,
    transcribes the voice-over, and translates it into English.
    Then saves the result in a text file.

    This uses the 'openai/whisper-large-v2' model for maximum accuracy
    and configures generation to optimize quality.
    """
    asr_pipeline = pipeline(
        "automatic-speech-recognition",
        model="openai/whisper-large-v2",
        # Segments are split into 30s chunks (you can increase this, but 30s is a good balance).
        chunk_length_s=30,
        return_timestamps=False,
        generate_kwargs={
            "task": "translate",
            # Enable beam search.
            # Increasing num_beams makes it slower but potentially more accurate.
            "num_beams": 5,
            # Controls the length penalty (1.0 = neutral).
            # Adjust if sentences are too short or too long.
            "length_penalty": 1.0,
            # Prevents repeating the same n-gram sequences too often.
            "no_repeat_ngram_size": 2
        }
    )

    for file_name in os.listdir(folder):
        if file_name.endswith(".mp4"):
            full_path = os.path.join(folder, file_name)

            print(f"Processing transcription for: {full_path}")
            result = asr_pipeline(full_path)

            # If chunk_length_s > 0, the output is usually a list of chunks
            # (a dict per chunk), otherwise a single dict. Handle both cases.
            if isinstance(result, list):
                translated_text = " ".join(segment["text"] for segment in result)
            else:
                translated_text = result["text"]

            output_file_name = os.path.splitext(full_path)[0] + "_en.txt"
            with open(output_file_name, "w", encoding="utf-8") as file:
                file.write(translated_text)

            print(f"Text file saved: {output_file_name}")


if __name__ == "__main__":
    # Specify the path to your folder containing .mp4 videos
    video_folder = r"speech"
    transcribe_and_translate_videos(video_folder)
