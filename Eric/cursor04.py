import sys

#validating the number of arguments and printing usage
if len(sys.argv) != 2:
    print('Usage: cursor04.py <Province abbreviation>')
    sys.exit()


#assigning arguments to variables
province = sys.argv[1]

#validation of the province abbreviation
if province.upper() not in ['AB', 'BC', 'MB', 'NB', 'NF', 'NS', 'NT', 'ON', 'PE', 'QC', 'SK', 'YT']:
    print('Province abbreviation invalid')
    sys.exit()


import arcpy

#environement setting
arcpy.env.workspace = "../../../../data/Canada/Canada.gdb"

#parameters
fc = "MajorCities"
fields = ['NAME', 'PROV', 'SHAPE@X', 'SHAPE@Y']
field_del = arcpy.AddFieldDelimiters(fc, 'PROV')
sql_where = f"{field_del} = '{province.upper()}'"
count = 0

#search cursor created, print name and province fields, x and y geometry and count
with arcpy.da.SearchCursor(fc, fields, sql_where) as cursor:
    print('Name, Prov, Latitude, Longitude')
    for row in cursor:
        print(f'{row[0]}, {row[1]}, {row[2]}, {row[3]}')
        count += 1
print(f'There are {count} cities in the above list')