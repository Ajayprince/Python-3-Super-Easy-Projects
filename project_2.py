import sounddevice
from scipy.io.wavfile import write
frames = 44100
seconds = int(input("Enter the duration: "))
print("Recording is in progress...")
rec_voice = sounddevice.rec(int(frames*seconds),frames,channels=2)
sounddevice.wait()
write('reuslt.wav',frames,rec_voice)
print("Recording Finished!")