import xml.etree.ElementTree as ET
from termcolor import colored

class Updater:
    def __init__(self):
        self.versions = []

    def add_version(self, version_nbr):
        self.versions.append(version_nbr)

    def update(self, filename, target_version):
        tree = ET.parse(filename)
        # root is the parent attribute
        root = tree.getroot()
        self.current_version = root.get('version')

        if (target_version != self.current_version):
            if (target_version > self.current_version):
                self.update_forward(self.current_version, target_version, tree)
            else:
                self.update_backward(self.current_version, target_version, tree)

            root.set('version',target_version)
            # save updated XML file
            tree.write(filename)
            print(colored("\nFile succesfully updated from version {} to {}.".format(self.current_version, target_version),'green'))
        else:
            print(colored("\nThe file is already in version {}.".format(self.current_version),'yellow'))


    def update_forward(self, current_version, target_version, tree):
        for version in self.versions:
            if version.nbr > current_version and version.nbr <= target_version:
                for element in tree.iter():
                    for change in version.changes:
                        # if finds the word to replace -> replaces element names, otherwise does nothing
                        element.tag = element.tag.replace(change[0], change[1])

    def update_backward(self, current_version, target_version, tree):
        for version in reversed(self.versions):
            if version.nbr <= current_version and version.nbr > target_version:
                for element in tree.iter():
                    for change in version.changes:
                        # if finds the word to replace -> replaces element names, otherwise does nothing
                        element.tag = element.tag.replace(change[1], change[0])

# replace element content
# node.text = node.text.replace("test", "Content")