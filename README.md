# LegionRefRateSwitcher
Refresh rate switcher for Lenovo Legion 7i when battery powered for Windows 10

## Devices Tested on:

- Lenovo Legion 7i with Display @ 144hz

Other devices that it could work on but have not been tested:
- Lenovo Legion 7i with Display @ 240hz
- Lenovo Legion 5i with Display @ 144hz
- Lenovo Legion 5 with Display @ 120hz

## Prerequisite:

Requires setting up a custom resolution refresh rate of 60hz for Lenovo Legion 7i's display in Nvidia Control Panel for the program to work.

Process to create and test custom resolutions in Nvidia Control Panel is described here: https://nvidia.custhelp.com/app/answers/detail/a_id/759/~/custom-resolutions

## Version 0.1 Feature: 

Auto switch the refresh rate of the laptop's display and one additional connected display refresh rate between 60hz and highest available refresh rate for that display.

## Limitation:
Currently, if an additional display is connected the display mode is always set to Optimus and cannot be changed. In this situation only the external monitor's refresh rate can be updated. The laptop's display will always be set to 144hz. Running the program with an external display will only update the external monitors refresh rate.


