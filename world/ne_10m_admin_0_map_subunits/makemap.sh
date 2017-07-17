#!/bin/bash

sub=subunits.json 
world=world.json

if [ -f $sub ] ; then
rm $sub
echo "removed subunits.json"
fi

if [ -f $world ] ; then
rm $world
echo "removed world.json"
fi

ogr2ogr \
  -f GeoJSON \
  subunits.json \
  ne_10m_admin_0_map_subunits.shp

topojson \
  -o world.json \
  --id-property SU_A3 \
  --properties name=NAME \
  -- \
  subunits.json \