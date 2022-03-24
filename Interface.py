from Version import Version
from Updater import Updater
from termcolor import colored

def print_menu():
    print('\033[1m' + '\n--------------- XML File Migrator ---------------\n' + '\033[0m')
    print("1. Migrate file")
    print("2. Show existing versions")
    print("3. Add version")
    print("4. Edit version")
    print("0. Quit")

def print_versions(obj):
    for v in obj.versions:
        print("Version {}:".format(v.nbr))
        for i,rule in enumerate(v.changes):
            print("Rule {}: \"{}\" -> \"{}\"".format(i+1, rule[0], rule[1]))
        print("\n")

def find_version(obj, user_version):
    for v in obj.versions:
        if user_version == v.nbr:
            return v

def run(updater_obj):
    option = 1;
    i = 0;
    user_versions = [];
    while option != 0:
        print_menu()
        option = input("\nEnter your option: ")
        match option:
            case "1":
                user_filename = input("\nEnter the filename: ");
                if not (user_filename.__contains__(".xml")):
                    user_filename = user_filename + ".xml"
                user_target = input("\nEnter the target version number: ");
                updater_obj.update(user_filename, user_target);
            case "2":
                print(" ")
                print_versions(updater_obj)
            case "3":
                user_version = input("\nEnter version number: ");
                temp_version = Version(user_version);
                old_word = input("\nEnter the previous nomenclature: ");
                new_word = input("\nEnter the current nomenclature: ");
                temp_version.add_change([old_word, new_word]);
                updater_obj.versions.append(temp_version);
            case "4":
                user_version = input("\nEnter version number: ");
                old_word = input("\nEnter the previous nomenclature: ");
                new_word = input("\nEnter the current nomenclature: ");
                find_version(updater_obj, user_version).add_change([old_word, new_word]);
            case "0":
                break
            case _:
                print(colored("\nInvalid option.",'red'))