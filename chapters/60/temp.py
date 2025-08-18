import sys
sys.path.insert(0, r"D:\Github\molass-legacy")
from molass_legacy import get_version
assert get_version() >= "0.2.4", "Please update molass_legacy to the latest version."
from molass_legacy.SecTheory.PlateTheory import demo, demo2, demo3
# demo(save=True, mp4=True)
# demo2(save=True, mp4=True)
demo3()