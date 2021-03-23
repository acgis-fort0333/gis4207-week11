import arcpy

#parameters
fc = "../../../../data/Canada/Can_Mjr_Cities.shp"
fields = ['NAME', 'PROV']
count = 0


#search cursor created, print name and province fields, and count
with arcpy.da.SearchCursor(fc, fields) as cursor:
    print('Name, Prov')
    for row in cursor:
        print(f'{row[0]}, {row[1]}')
        count += 1
print(f'There are {count} cities in the above list')
