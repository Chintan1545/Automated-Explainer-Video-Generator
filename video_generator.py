import os
from gtts import gTTS
from moviepy import ImageClip, AudioFileClip, concatenate_videoclips
from PIL import Image, ImageDraw, ImageFont

os.makedirs("temp", exist_ok=True)
VIDEO_SIZE = (1280,720)

def create_video(text):

    slides = [s.strip() for s in text.split("\n\n") if s.strip()]
    clips = []

    for i, slide in enumerate(slides):

        # audio
        tts = gTTS(slide)
        audio_path = f"temp/audio_{i}.mp3"
        tts.save(audio_path)

        audio = AudioFileClip(audio_path)

        # image
        img = Image.new("RGB", VIDEO_SIZE, (30,30,40))
        draw = ImageDraw.Draw(img)

        font = ImageFont.load_default()

        bbox = draw.textbbox((0,0), slide, font=font)
        w  = bbox[2] - bbox[0]
        h = bbox[3] - bbox[1]

        draw.text(
        ((1280-w)/2, (720-h)/2),
        slide,
        fill=(255,255,255),
        font=font
        )

        img_path = f"temp/slide_{i}.png"
        img.save(img_path)

        clip = ImageClip(img_path, duration=audio.duration)
        clip = clip.with_audio(audio)

        clips.append(clip)

    final_video = concatenate_videoclips(clips)

    output_path = "output_video.mp4"

    final_video.write_videofile(output_path,fps=24)

    return output_path