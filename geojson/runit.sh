#!
# ogr2ogr -f GeoJSON small.json state.json -where 'REGION10="4"'
ogr2ogr -progress -f GeoJSON nyc-zip.json zcta5.json -where 'GEOID10="11221"'
