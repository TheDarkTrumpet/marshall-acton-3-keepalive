import pyaudio
import numpy as np
import time
import schedule

# Override this, if necessary, to match another Bluetooth device
DEVICE_NAME = 'ACTON III'


# Function to get the output device index
def get_output_device_index() -> int | None:
    """
    Loops through the devices, looking for the name DEVICE_NAME (defined above) and if found, it returns the
    index.
    :return: Device ID, or None if not found
    """
    p = pyaudio.PyAudio()
    info = p.get_host_api_info_by_index(0)
    device_count = info.get('deviceCount')
    for i in range(0, device_count):
        device = p.get_device_info_by_index(i)
        if device['name'] == DEVICE_NAME:
            return i
    return None


# Function to play the tone
def play_tone() -> None:
    """
    If the device is found through get_output_device_index, will send a tone of 5Mhz (below human hearing) for 1/2
    a second to the device, then turning it off afterwards.
    :return: None
    """
    output_device_index = get_output_device_index()
    if output_device_index is not None:
        print(f"Sending tone to {DEVICE_NAME}")
        p = pyaudio.PyAudio()
        stream = p.open(format=pyaudio.paInt16, channels=1, rate=44100, output=True,
                        output_device_index=output_device_index)
        # Generate the tone
        frequency = 5000000  # 5 MHz
        duration = 0.5  # 500ms
        amplitude = 0.5
        samples = np.sin(2 * np.pi * frequency * np.arange(44100 * duration) / 44100)
        tone = (samples * amplitude).astype(np.int16)
        # Play the tone
        stream.write(tone.tobytes())
        # Wait for the tone to play
        time.sleep(0.5)
        # Turn off the tone
        stream.stop_stream()
        stream.close()
        p.terminate()
    else:
        print(f"{DEVICE_NAME} not found in output devices, skipping")


# Schedule the tone-sending function to run every 5 minutes
schedule.every(5).minutes.do(play_tone)

# Main loop
while True:
    schedule.run_pending()
    time.sleep(1)
