import xml.dom.minidom
import os
import zipfile
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


def extract_pois():
    with open(args.output, 'w') as f:
        os.chdir(args.folder)
        for _, _, files in os.walk("."):
            for file in files:
                result = to_xml(file[:-4])
                f.write(result + "\n")
                print("From", file, ":", result)
        print("Saved locations into", args.output)


def to_xml(location):
    # Extract the doc.kml file from kmz file
    with zipfile.ZipFile(location + ".kmz", "r") as zip_ref:
        zip_ref.extract("doc.kml")

    # Convert kml to DOM (Document Object Model)
    e = xml.dom.minidom.parse('doc.kml')

    # Get the element Placemark where LookAt is allocated
    placemark = e.getElementsByTagName("Placemark")[0]

    # Get LookAt and convert to xml string
    lookat = placemark.getElementsByTagName("LookAt")[0].toxml()

    # We do not need doc.kml anymore
    os.remove('doc.kml')

    return (args.planet + "@" + location + "@flytoview=" + lookat).replace("\n", "").replace("\t", "")


if __name__ == "__main__":
    parser.add_argument('--folder', help='folder where you have the kmz files', default="KMZ")
    parser.add_argument('--planet', help='the planet where your locations are', default="Earth")
    parser.add_argument('--output', help='output file name', default="pois.txt")
    args = parser.parse_args()

    print_liquid_galaxy()
    print("Folder :", args.folder, "\tPlanet :", args.planet, "\tOutput :", args.output)
    extract_pois()
