import arcpy

fc = "../../../../data/Canada/Can_Mjr_Cities.shp"
fields = ['NAME', 'PROV']
count = 0

with arcpy.da.SearchCursor(fc, fields) as cursor:
    print('Name, Prov')
    for row in cursor:
        print(f'{row[0]}, {row[1]}')
        count += 1
print(f'There are {count} cities in the above list')
