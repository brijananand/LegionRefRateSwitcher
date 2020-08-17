# LegionRefRateSwitcher
Refresh rate switcher for Lenovo Legion 7i when battery powered for Windows 10. 

The purpose is to automatically lower the refresh rate when on battery power in order to reduce battery usage by running the display at a higher refresh rate.

## Devices Tested on

- Lenovo Legion 7i with Display @ 144hz

Other devices that it could work on but have not been tested:
- Lenovo Legion 7i with Display @ 240hz
- Lenovo Legion 5i with Display @ 144hz
- Lenovo Legion 5 with Display @ 120hz

## Prerequisite

Requires setting up a custom resolution refresh rate of 60hz for Lenovo Legion 7i's display in Nvidia Control Panel for the program to work.

Process to create and test custom resolutions in Nvidia Control Panel is described here: https://nvidia.custhelp.com/app/answers/detail/a_id/759/~/custom-resolutions

## Installation

### Method 1
#### Python 3 installation
- Install Python3 release on Windows 10 https://www.python.org/downloads/windows/. This should also install [pip](https://pip.pypa.io/en/stable/) (Python Package Installer) by default. 
- While installing Python3 ensure that the 'Add Python 3.x to PATH is checked' in the installer.

#### Installing dependencies with PIP

```bash
pip install psutil pypiwin32 wmi apscheduler
```

#### Running LegionRefRateSwitcher.py

In command line enter the following:

```bash
py LegionRefRateSwitcher.py
```

### Method 2
#### Executing the release build

Navigate to https://github.com/brijananand/LegionRefRateSwitcher/releases and click on the latest release. Once found, find the .exe file under 'Assets'. The build was generated with pyinstaller. 

### Creating .EXE builds with pyinstaller

Navigate into the source directory and open a command window to type the following:

1) Install pyinstaller
```bash
pip install pyinstaller
```

2) Create the build. Replace version-file with your verison text file and icon with your .ico file. 

```bash
pyinstaller --onefile --version-file=version.txt --icon=icon.ico LegionRefRateSwitcher.py
```

## Version 0.1 Feature 

Auto switch the refresh rate of the laptop's display and one additional connected display refresh rate between 60hz and highest available refresh rate for that display. The switch to a lower refresh rate happens only when the Vantage thermal mode - (1, 4) - Silent is selected by the user either by pressing fn + Q or through the Lenovo Vantage application. For all other modes even on battery power, the refresh rate should still be left on 144 hz considering that users might be requiring the higher refresh rate on other thermal modes.

Vantage thermal modes outputs displayed in command line when the program runs:
- (1, 4) - Silent 
- (2, 4) - Balanced
- (3, 4) - Performance

AC Powered modes outputs displayed in command line when the program runs:
- True: Running on AC Power
- False: Running on Battery

## Limitation
Currently, if an additional display is connected the display mode is always set to Optimus and cannot be changed. In this situation only the external monitor's refresh rate can be updated. The laptop's display will always be set to 144hz. Running the program with an external display will only update the external monitors refresh rate.

## Battery consumption tests

Reduced battery usage when lowering the refresh rate by using this program is yet to be confirmed. Currently the program only furnishes the need to automatically lower the refresh rate or increase it when on AC power. 

## License

[GNU GPL V3](https://github.com/brijananand/LegionRefRateSwitcher/blob/master/LICENSE)
