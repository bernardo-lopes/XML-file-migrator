import xml.etree.ElementTree as ET
from termcolor import colored
from Version import Version
from Updater import Updater
from Interface import run

# manually populate the versions and respective changes
v1 = Version("1.0");

v15 = Version("1.5");
v15.add_change(["v1.0-Element", "v1.5-Element"]);
v15.add_change(["v1.0-Sub-Element", "v1.5-Sub-Element"]);

v2 = Version("2.0");
v2.add_change(["v1.5-Element", "v2.0-Element"]);
v2.add_change(["v1.5-Sub-Element", "v2.0-Sub-Element"]);

v25 = Version("2.5");
v25.add_change(["v2.0-Element", "v2.5-Element"]);
v25.add_change(["v2.0-Sub-Element", "v2.5-Sub-Element"]);

v251 = Version("2.5.1");
v251.add_change(["v2.5-Element", "v2.5.1-Element"]);
v251.add_change(["v2.5-Sub-Element", "v2.5.1-Sub-Element"]);

v3 = Version("3.0");
v3.add_change(["v2.5.1-Element", "v3.0-Element"]);
v3.add_change(["v2.5.1-Sub-Element", "v3.0-Sub-Element"]);

updater = Updater();
updater.add_version(v15);
updater.add_version(v2);
updater.add_version(v25);
updater.add_version(v251);
updater.add_version(v3);

# run starts the terminal interface/menu
if __name__ == '__main__':
    run(updater)

# add option to delete inside "Edit version"