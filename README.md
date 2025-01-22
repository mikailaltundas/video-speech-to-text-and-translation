# Transcribe and Translate Videos 🎥✍️

This project contains a Python script designed to process `.mp4` video files in a specified folder. It performs the following actions:

1. Transcribes the audio from each video.
2. Translates the transcription into English.
3. Saves the translated text to a `.txt` file.

## Features

- **High Accuracy**: Utilizes the `openai/whisper-large-v2` model for precise transcription and translation.
- **Customizable Parameters**: Configurable options such as chunk size, beam search, and length penalty for optimizing transcription and translation.
- **Batch Processing**: Automatically processes all `.mp4` files in a specified folder.

## Prerequisites

Before running the script, ensure the following:

- Python 3.8 or higher is installed.
- Install the required Python packages:

  ```bash
  pip install transformers
  ```

## Usage

1. Clone the repository or copy the script.
2. Place your `.mp4` video files in a folder (e.g., `speech`).
3. Update the `video_folder` variable in the script to the path of your folder containing the videos:

   ```python
   video_folder = r"speech"
   ```

4. Run the script:

   ```bash
   python main.py
   ```

5. The script will generate a `.txt` file for each video in the folder, containing the translated transcription.

## How It Works

- The script uses the `transformers.pipeline` API with the `openai/whisper-large-v2` model.
- Each `.mp4` file is processed in chunks of 30 seconds for optimal performance.
- Transcriptions are translated into English and saved as text files with the same name as the video, appended with `_en.txt`.

## Configuration Options

You can adjust the following parameters in the script for better results:

- **Chunk Length** (`chunk_length_s`): Determines the size of audio segments (in seconds) for processing.
- **Beam Search** (`num_beams`): Controls the number of beams for decoding. Higher values improve accuracy but slow down processing.
- **Length Penalty** (`length_penalty`): Affects the length of the generated sentences.
- **No Repeat N-Gram Size** (`no_repeat_ngram_size`): Prevents repetitive sequences in translations.

## Example Output

For a video file named `example.mp4`, the script generates a text file named `example_en.txt` containing the English transcription.