from functools import partial
import pyproj
from shapely.ops import transform
from shapely.geometry import Point

from gmplot import gmplot
import MapPloting

proj_wgs84 = pyproj.Proj(init='epsg:4326')


def geodesic_point_buffer(lat, lon, km):
	# Azimuthal equidistant projection
	aeqd_proj = '+proj=aeqd +lat_0={lat} +lon_0={lon} +x_0=0 +y_0=0'
	project = partial(
	pyproj.transform,
	pyproj.Proj(aeqd_proj.format(lat=lat, lon=lon)),
	proj_wgs84)
	buf = Point(0, 0).buffer(km *10)  # distance in metres
	return transform(project, buf).exterior.coords[:]

#b = geodesic_point_buffer(37.770776, -122.461689, 10)


#gmap = gmplot.GoogleMapPlotter(37.770776, -122.461689, 13)
#top_attraction_lats, top_attraction_lons = zip(*b)
#print(type(top_attraction_lats))
#gmap.scatter(list(top_attraction_lats), list(top_attraction_lons), '#3B0B39', size=40, marker=False)
# Marker

#hidden_gem_lat, hidden_gem_lon = 37.770776, -122.461689
#gmap.marker(hidden_gem_lat, hidden_gem_lon, 'cornflowerblue')

def PlotingMap(Lon, Lat,Outputfile	):
	gmap = gmplot.GoogleMapPlotter(Lat,Lon, 20)
	b = geodesic_point_buffer(Lat,  Lon, 1)
	Latitude, Longitude = zip(*b)

	#gmap = gmplot.GoogleMapPlotter(Lat,Lon)
	gmap.plot(Longitude,Latitude, 'cornflowerblue', edge_width=10)
	#gmap.scatter(Latitude, Longitude,'red',size = 100, marker = False) 
	gmap.marker(Lat, Lon, 'cornflowerblue')
	gmap.draw(Outputfile+".html")
	# Draw
	#gmap.draw("my_map.html")

