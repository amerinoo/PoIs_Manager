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


def check_flytoview(line):
    if line.count("@flytoview=") != 1:
        print("Flytoview error:", line)


def check_angle_bracket(line):
    if line.count("</") != line.count(">") / 2:
        print("Angle bracket error:", line, line.count("</"), line.count(">"))


def check_pois_count(count, minimum=30):
    if count < minimum:
        print("There are", count, "POIs in the file. Remaining", minimum - count, "POIs.")


def check_pois():
    try:
        with open(args.checkFile, 'r') as xml_file:
            line = xml_file.readline().strip()
            count = 0
            while line:
                while line.count("</LookAt>") != 1:
                    sub_line = xml_file.readline().strip()
                    if not sub_line:
                        break
                    line += sub_line

                check_flytoview(line)
                check_angle_bracket(line)

                line = xml_file.readline().strip()
                count += 1

            check_pois_count(count)

    except IOError:
        print('Invalid File')
    except:
        print('Unknown error, exiting.')
        quit()


if __name__ == "__main__":
    parser.add_argument('--checkFile', help='file name to check the syntax', required=True)
    args = parser.parse_args()

    print_liquid_galaxy()

    check_pois()
