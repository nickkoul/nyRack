# API Documentation


`GET /citibike` - Returns a list of the Citi Bike Rack locations in (Lat, Long)   

`GET /new` - Returns a list of the potential bike rack locations in (Lat, Long)      

`GET /existing` - Returns a list of the existing NYC DOT bike rack locations in (Lat, Long)   

`GET /k` - Returns a list of the best k new locations for bike rack locations in (Lat, Long)
URL Parameters:   
* k: The number of best locations requested   
* n: The number of total locations to search form.

Note that this currently send all n data points to the fronted.
