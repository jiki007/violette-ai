from playsound3 import playsound
import os, asyncio
import edge_tts

async def violette_speak(text):
    voice = "en-US-AriaNeural"
    output_file = "response.mp3"

    communicate = edge_tts.Communicate(text, voice, rate="+10%", pitch="-2Hz")
    await communicate.save(output_file)

    try:
        playsound(output_file)
    except Exception as e:
        print(f"Audio Error:{e}")
    finally:
        if os.path.exists(output_file):
            os.remove(output_file)