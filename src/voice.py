import edge_tts
import subprocess
import asyncio

async def violette_speak(text):
    voice = "en-US-AriaNeural"
    rate = "+10%"
    pitch = "-2Hz"
    communicate = edge_tts.Communicate(text, voice, rate=rate, pitch=pitch)
    await communicate.save("response.mp3")

    #mpv plays the audio on Debian
    subprocess.run(
        ["mpv","--no-video","response.mp3"],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL

    )