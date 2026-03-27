import wave
import contextlib
import os

# Determine the durations of all wav files in ../sounds/waves/ and write them to wav_durations.txt

def GetWavDuration(filename):
    with contextlib.closing(wave.open(filename,'r')) as f:
        frames = f.getnframes()
        rate = f.getframerate()
        duration = frames / float(rate)
        return f"Duration of file '{filename}' = {str(duration)}"

wavdir = "../sounds/waves/"
with open("wav_durations.txt", 'w') as f:
    for file in os.listdir(wavdir):
        if file.endswith(".wav"):
            f.write(GetWavDuration(os.path.join(wavdir, file)) + "\n")
