# top: (69,62417-широта)*1147,27
# left: 1334-(35,59167-долгота)*368,3896
####Introduction to Web Scraping#####

from getting_coordinates import Getting_coordinates
from reading_and_writing_css import Operations_with_css

from getting_css_lines import Getting_css_text
from getting_coordinates import Getting_coordinates
# A Gusev
gusev_position = Getting_coordinates(9052678)
lat_long_gusev = gusev_position.getting_coordinates()
lat_gusev = lat_long_gusev[0]
long_gusev = lat_long_gusev[1]
print(lat_gusev)
print(long_gusev)

# # V Harlamov position
# print(getting_coordinates(9052666))
harlamov_position = Getting_coordinates(9052666)
lat_long_harlamov = harlamov_position.getting_coordinates()
lat_harlamov = lat_long_harlamov[0]
long_harlamov = lat_long_harlamov[1]
print(lat_harlamov)

# # Bluetrans position

bluetrans_position = Getting_coordinates(9220835)
lat_long_bluetrans = bluetrans_position.getting_coordinates()
lat_bluetrans = lat_long_bluetrans[0]
long_bluetrans = lat_long_bluetrans[1]
print(lat_bluetrans)

# # Vladimir Petrov position

petrov_position = Getting_coordinates(9139567)
lat_long_petrov = petrov_position.getting_coordinates()
lat_petrov = lat_long_petrov[0]
long_petrov = lat_long_petrov[1]
print(lat_petrov)

# # Aleksander Ragulin position

ragulin_position = Getting_coordinates(9255086)
lat_long_ragulin = ragulin_position.getting_coordinates()
lat_ragulin = lat_long_ragulin[0]
long_ragulin = lat_long_ragulin[1]
print(lat_ragulin)
#
# getting_text_from_css_file:
text_object = Getting_css_text()
css_lines = text_object.getting_lines()

# writing new coordinates into current css(css_lines)

read_write = Operations_with_css(lat_gusev, long_gusev, lat_harlamov, long_harlamov, lat_bluetrans, long_bluetrans, lat_petrov, long_petrov, lat_ragulin, long_ragulin, css_lines)
print(read_write.updating_css_file_with_new_coordinates())

