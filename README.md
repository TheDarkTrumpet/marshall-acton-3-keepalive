# Marshall Acton III Keep Alive

## Purpose/Reasoning

The Marshall Acton 3 is a fantastic Bluetooth speaker system, and one of my 
favorite when it comes to sound quality.  Unfortunately, there's also a setting that turns the
device off after 10 minutes of inactivity.

More information can be found on their [website](https://support.marshallheadphones.com/hc/en-us/articles/6903536230929-How-to-Acton-III-Use-the-network-standby-mode)

Their reasoning for the setting, being unable to be overridden, is insufficient in my view
and incredibly inconvenient.  Due to meetings, pausing periodically for various reasons,
and other reasons, 10-minutes of inactivity is simply too short.  And, their reasoning to 
save energy is not a good [excuse](https://www.androidauthority.com/does-bluetooth-drain-battery-1145853/) in my view.

This project helps resolve this problem.

## Project Description

This project is _incredibly simple_.  What it does is sending a tone, 5Mhz, every 5 minutes, to the device.  This
is intended to run on a consistent basis (whether the device is connected, or not).  If the device isn't connected,
the tone simply doesn't play.  Otherwise, it does.  If you disconnect, and reconnect, it will automatically
resume.

## How to Run (Using distributables provided)

1. Go to the releases (on the ride side)
2. Download the relevant release (see table below)
3. Unzip the file you downloaded
4. Run the `marshall-keepalive` program (from command line)

### Releases
| Filename | Architecture | OS |
|----------|--------------|----|
| marshall-keepalive-windows.zip | x86 | Windows |
| marshall-keepalive-osx86.zip | x86 | OSX |
| marshall-keepalive-osx.zip | aarch64 | OSX |
| marshall-keepalive-linux.zip | x86 | Linux |

### OSX Special Considerations

The OSX version may need to be allowed through security.  You need to first unzip and run it,
when OSX complains about it:

1. Go to Settings
2. Go to Privacy and Security
3. Click on the button to allow it to "Run Anyways" and enter your pin.
4. Return to the terminal and run it again.

If you also have problems running this you may need to install portaudio through homebrew:

```text
brew install portaudio
```

### Linux Special Considerations

The Linux version was built through Github Actions, on Ubuntu.  It requires the Python module
for pyaudio installed.

Install it through:
```text
sudo apt install python3-pyaudio
```

## How to Run (Using source code)

Create your environment, install your requirements, then run the script.

```shell
~/.pyenv/versions/3.12.2/bin/python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

python3 keepalive.py
```
