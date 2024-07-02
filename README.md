# Marshall Acton III Keep Alive

## Purpose/Reasoning

The Marshall Action 3 is a fantastic Bluetooth speaker system, and one of my 
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

### Windows
## How to Run (Using source code)

Create your environment, install your requirements, then run the script.

```shell
~/.pyenv/versions/3.12.2/bin/python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

python3 keepalive.py
```
