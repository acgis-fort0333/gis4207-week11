import sys
import os
from zipfile import ZipFile


def main():

    global arcpy

    #validating the number of arguments and printing usage
    if len(sys.argv) != 1:
        print('Usage: cursor02.py ')
        sys.exit()

    #if output folder does not exist, create output folder
    if os.path.exists('../output') == False:
        os.mkdir('../output')


    import arcpy

    #environement setting
    arcpy.env.workspace = "../../../../data/Canada/Canada.gdb"

    #parameters
    fc = "MajorCities"
    fields = ['NAME', 'PROV', 'SHAPE@X', 'SHAPE@Y', 'UTM_MAP']

    fc_to_kml(fc, fields)

    zip_kml('../output/Cities.kml', '../output/Cities.kmz')


def fc_to_kml(fc, fields):
    """Takes a feature class and list of fields as argument, create a kml file"""
    
    #kml header and footer
    header = '''<?xml version="1.0" encoding="UTF-8"?>
    <kml xmlns="http://www.opengis.net/kml/2.2">\n
    <Document>\n'''
    footer = '</Document>\n</kml>'

    #Cities.kml created and written
    with open ('../output/Cities.kml', 'w') as file:
       #search cursor created, string with tags in cursor variables created for each point in the feature class
        with arcpy.da.SearchCursor(fc, fields) as cursor:
            file.write(header)
            for row in cursor:
                kml_string = ( 
                        f'\t<Placemark>\n'
                        f'\t\t<name>{row[0]}, {row[1]}</name>\n'
                        f'\t\t<description>http://www.canmaps.com/topo/nts50/map/{row[4]}.htm</description>\n'
                        f'\t\t<Point>\n'
                        f'\t\t\t<coordinates>{row[2]},{row[3]}</coordinates>\n'
                        f'\t\t</Point>\n'
                        f'\t</Placemark>\n'
                )
                file.write(kml_string)
            file.write(footer)


def zip_kml(in_kml, out_kmz):
    """Zip kml file into a kmz file"""    
    kml_file = 'input'    
    with ZipFile(out_kmz, 'w') as zip:
        zip.write(in_kml)


if __name__ == '__main__':
    main()