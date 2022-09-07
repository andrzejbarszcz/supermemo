import playsound
playsound.playsound('ptak3d.wav')


'''
from scipy.io import wavfile
import sys
# samplerate, data = wavfile.read('ptak3d.wav')

sample_rate, data = wavfile.read('ptak3d.wav')
# samples = wavfile.read(open('ptak3d.wav', 'r'))
'''
'''
import soundfile as sf
y, s = librosa.load(pwd+'\\ans.wav', sr=48000)
sf.write('audio_test_1.wav', y, s, "PCM_24")

rate, data = read('durny.wav')
'''