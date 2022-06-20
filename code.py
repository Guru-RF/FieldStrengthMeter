import FieldStrengthMeter
import OLED
import time

FieldStrengthMeter.Led.value = False

# TODO
# - MODE SELECTOR -> Wideband/VLF/HF/VHF
# - LOG via USB-HID-KBD (json/plain enable/set via config)
# - Grafical interface ... BAT/USB-C vector + xxx% if bat
# - dB -> v/m (log press button) + calculation

OLED.drawBattery()
OLED.printMode("Wide 1-500Mhz")

while True:
    OLED.printBatPCT(FieldStrengthMeter.batPCT())
    OLED.printDb(FieldStrengthMeter.rfDbWideband())
    time.sleep(1)