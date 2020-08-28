
# import gmplot package 
import gmplot 
  
# GoogleMapPlotter return Map object 
# Pass the center latitude and 
# center longitude 
gmap1 = gmplot.GoogleMapPlotter(27.7172,85.3240, 13 ) 
  
# Pass the absolute path 
gmap1.draw( "map.html" )

gmplot.__file__
