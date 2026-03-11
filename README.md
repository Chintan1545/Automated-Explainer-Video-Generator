# 🎬 Automated Explainer Video Generator

A simple Python app that converts text scripts into explainer videos with text-to-speech audio and slide images. Users can preview and download the generated video via a **Streamlit web app**.

---

## 📝 Features

- Convert text into slides automatically.
- Generate audio for each slide using **Google Text-to-Speech (gTTS)**.
- Combine images and audio into a video using **MoviePy**.
- Preview the video directly in the browser.
- Download the video as `explainer_video.mp4`.
- Supports custom slide separation using **blank lines** in the script.

---

## 🛠️ Technologies Used

- **Python 3.9+**
- [Streamlit](https://streamlit.io/) – Web app interface.
- [gTTS](https://pypi.org/project/gTTS/) – Text-to-Speech conversion.
- [MoviePy](https://zulko.github.io/moviepy/) – Video generation.
- [Pillow (PIL)](https://pillow.readthedocs.io/en/stable/) – Image creation and text rendering.

---

## 📂 Project Structure

```

.
├── app.py                  # Streamlit app
├── video_generator.py      # Video generation logic
├── temp/                   # Temporary folder for audio/images
├── output_video.mp4        # Final generated video
└── README.md

````

---

## ⚡ Installation

1. **Clone the repository:**

```bash
git clone https://github.com/Chintan1545/explainer-video-generator.git
cd explainer-video-generator
````

2. **Create a virtual environment (optional but recommended):**

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

3. **Install dependencies:**

```bash
pip install -r requirements.txt
```

**Sample `requirements.txt`:**

```
streamlit
gTTS
moviepy
Pillow
```

---

## 🚀 Usage

1. Run the Streamlit app:

```bash
streamlit run app.py
```

2. Open the link in your browser (usually `http://localhost:8501`).

3. Paste your script in the text area.

   * Use **blank lines** to separate slides.

4. Click **Generate Video**.

5. Preview your video and download it using the **Download Video** button.

---

## 🖌️ Example Script

```
Welcome to the Automated Explainer Video Generator!

This tool converts your text into slides with voiceover.

Enjoy creating videos automatically!
```

* This will generate **3 slides** with voiceover.

---

## ⚙️ Notes & Tips

* Longer text may require text wrapping; currently text is centered but may overflow for very long lines.
* Temporary files are stored in the `temp/` folder during processing.
* Default font is used. You can customize it in `video_generator.py`.

---

## 📜 License

This project is licensed under the **MIT License** – see the [LICENSE](LICENSE) file for details.

---

## 👨‍💻 Author

Chintan Dabhi
