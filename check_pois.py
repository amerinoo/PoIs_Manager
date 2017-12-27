import argparse

parser = argparse.ArgumentParser(description='Process the KMZ files that you extract from Google Earth and save '
                                             'de PoIs to a file')


def print_liquid_galaxy():
    print(" _ _             _     _               _" + '\n' +
          "| (_) __ _ _   _(_) __| |   __ _  __ _| | __ ___  ___   _ " + '\n' +
          "| | |/ _` | | | | |/ _` |  / _` |/ _` | |/ _` \ \/ / | | |" + '\n' +
          "| | | (_| | |_| | | (_| | | (_| | (_| | | (_| |>  <| |_| |" + '\n' +
          "|_|_|\__, |\__,_|_|\__,_|  \__, |\__,_|_|\__,_/_/\_\\__, |" + '\n' +
          "        |_|                |___/                    |___/ " + '\n' +
          "https://github.com/LiquidGalaxy/liquid-galaxy" + '\n' +
          "https://github.com/LiquidGalaxyLAB/liquid-galaxy" + '\n' +
          "-------------------------------------------------------------\n")


def check_flytoview(line, errors):
    if line.count("@flytoview=") != 1 and line:
        errors.append("Flytoview error: " + line)


def check_angle_bracket(line, errors):
    if line.count("</") != line.count(">") / 2:
        errors.append("Angle bracket error: " + line + " " + line.count("</") + "  " + line.count(">"))


def check_lookat(line, errors):
    for p in ["/ook", "look"]:
        if line.count(p) > 0:
            errors.append("LookAt error: " + line)
            return True
    return False


def check_pois_count(count, minimum=30):
    print("There are", count, "POIs in the file.", end=' ')
    if count < minimum:
        print("Remaining", minimum - count, "POIs.")
    else:
        print("There are", count - minimum, "extra POIs.\n")


def show_errors(errors):
    if len(errors) > 0:
        print("There are", len(errors), "errors in this file:")
    else:
        print("There are not mistakes in this file!")
    tag = "</altitude>"
    for idx, error in enumerate(errors):
        print(idx + 1, "-", error[:error.find(tag) + len(tag)])
        print("\t", error[error.find(tag) + len(tag):])


def check_pois():
    try:
        with open(args.checkFile, 'r') as xml_file:
            errors = []
            line = xml_file.readline()
            count = 0
            while line:
                line = line.strip()
                while line.count("</LookAt>") != 1:
                    sub_line = xml_file.readline().strip()
                    line += sub_line
                    if not sub_line or check_lookat(line, errors):
                        break

                check_flytoview(line, errors)
                check_angle_bracket(line, errors)
                if line:
                    count += 1
                line = xml_file.readline()

            check_pois_count(count)
            show_errors(errors)

    except IOError:
        print('Invalid File')


if __name__ == "__main__":
    parser.add_argument('--checkFile', help='file name to check the syntax', required=True)
    args = parser.parse_args()

    print_liquid_galaxy()

    check_pois()
