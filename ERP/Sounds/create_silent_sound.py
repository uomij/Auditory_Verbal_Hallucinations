import numpy as np
import scipy.io.wavfile

class BeepGenerator:
    def __init__(self):
        self.audio = []
        self.sample_rate = 44100.0

    def append_sinewave(
            self,
            freq=440.0,
            duration_milliseconds=500,
            volume=1.0):
        num_samples = int(duration_milliseconds * (self.sample_rate / 1000.0))
        x = np.array([i for i in range(num_samples)])
        sine_wave = volume * np.sin(2 * np.pi * freq * (x / self.sample_rate))
        self.audio.extend(list(sine_wave))
        return

    def save_wav(self, file_name):
        self.audio = np.array(self.audio).astype(np.float32)
        scipy.io.wavfile.write(file_name, int(self.sample_rate), np.array(self.audio))

if __name__ == "__main__":
    bg = BeepGenerator()
    # Generate a 1000Hz, 100ms, 85dB beep sound
    bg.append_sinewave(freq=1000, duration_milliseconds=3, volume=0.0)  # Adjust volume for 85dB SPL
    bg.save_wav("silent_sound.wav")  # Save as click_sound.wav

