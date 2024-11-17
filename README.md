Here’s a `README.md` file suitable for uploading this project to GitHub:


# Automate YouTube Shorts Video Creation

This project automates the creation of engaging YouTube Shorts-style videos by combining scripts, stock videos, audio, and subtitles. It uses APIs like AssemblyAI and Pexels along with libraries such as MoviePy to generate and compile video content seamlessly.

---

## Features
- **Script Generation**: Automatically generates scripts based on a given subject.
- **Stock Video Search**: Fetches relevant stock videos using the Pexels API.
- **Audio and Subtitle Creation**: Converts scripts to audio using TTS and generates subtitles.
- **Video Compilation**: Combines stock videos and synchronizes them with audio and subtitles.
- **Final Video Assembly**: Outputs a complete video ready for upload to platforms like YouTube.

---

## Prerequisites
Before running the project, ensure you have the following:
- Python 3.8 or later
- Required Python libraries (see [Requirements](#requirements))
- API keys for:
  - [AssemblyAI](https://www.assemblyai.com/)
  - [Pexels](https://www.pexels.com/api/)
- ImageMagick installed and its binary path configured

---

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/automate-youtube-shorts.git
   cd automate-youtube-shorts
   ```

2. Install required Python libraries:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up a `.env` file with the following keys:
   ```
   ASSEMBLY_AI_API_KEY=your_assembly_ai_api_key
   PEXELS_API_KEY=your_pexels_api_key
   IMAGEMAGICK_BINARY=path_to_imagemagick_binary
   ```

4. Ensure you have ImageMagick installed:
   - [Download ImageMagick](https://imagemagick.org/script/download.php)

---

## Usage

1. Run the notebook `Youtube.ipynb` to generate the video:
   - Open the notebook in Jupyter Notebook or JupyterLab.
   - Follow the step-by-step instructions in each cell to generate and compile the video.

2. The final video will be saved in the `./temp/` directory.

---
