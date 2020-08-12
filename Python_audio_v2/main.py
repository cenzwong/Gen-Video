from pydub import AudioSegment
# you will needed to install ffmpeg
import os, math
from natsort import natsorted


audios_folder = "output"

audios = [aud for aud in os.listdir(audios_folder) if aud.endswith(".mp3")]
audios = natsorted(audios)

for i,e in enumerate(audios):
    sound = AudioSegment.from_mp3(os.path.join(audios_folder, e))
    silent_ms = math.ceil(len(sound)/1000)*1000 - len(sound)
    print("Processing: "+ e+ " "+str(round(i*100/len(audios), 2)) +"% finish", end='\r')
    ms_silence = AudioSegment.silent(duration=(silent_ms))
    if i == 0:
        myOutput = AudioSegment.silent(duration=5000) + sound
        myOutput = myOutput.append(ms_silence, crossfade=0)
    else:
        myOutput = myOutput.append(sound, crossfade=0)
        myOutput = myOutput.append(ms_silence, crossfade=0)
    # if i == 0:
    #     myOutput = sound + ms_silence
    # else:
    #     myOutput = myOutput + sound + ms_silence
myOutput = myOutput + AudioSegment.silent(duration=20000)

bgm = AudioSegment.from_mp3("./bgm.mp3") - 9.5
myOutput = myOutput.overlay(bgm, loop=True)
# writing mp3 files is a one liner
myOutput.export("../video_combine/input.mp3", format="mp3")
for i,e in enumerate(audios):
    os.remove(os.path.join(audios_folder, e))

# ceil_sum = 0
# silent_sum = 0
# sound_sum = 0
# for i,e in enumerate(audios):
#     sound = AudioSegment.from_mp3(os.path.join(audios_folder, e))
#     silent_ms = math.ceil(len(sound)/1000)*1000 - len(sound)
#     silent_sum = silent_sum + silent_ms
#     ceil_sum = ceil_sum + math.ceil(len(sound)/1000)*1000
#     sound_sum = sound_sum + len(sound)

# ===== Demo Code =======
# # len() and slicing are in milliseconds
# halfway_point = len(sound) / 2
# second_half = sound[halfway_point:]

# # Concatenation is just adding
# second_half_3_times = second_half + second_half + second_half



# two_sec_silence = AudioSegment.silent(duration=2000)
# sound_with_gap = sound[:1000] + two_sec_silence + sound[1000:]