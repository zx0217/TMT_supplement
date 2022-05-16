import json

with open('/Users/apple/Documents/react-leaflet-app-demo-master/src/data/new.json', 'r') as f:
  data = json.load(f)

#coords = [data[0]['latitude'], data[0]['longitude']]
#print(coords)

features = []
for d in data:
    features.append({
        "type": "Feature",
        "geometry": {
            "type": "Point",
            "coordinates": [d['latitude'], d['longitude']]
        },
        "properties": {
            "address" : d["address"],
            "name" : d["name"],
            "stations" : d["stations"] 
          }
    })

with open('/Users/apple/Documents/react-leaflet-app-demo-master/src/data/cp_mod.json', 'w', encoding='utf-8') as f:
    json.dump(features, f, ensure_ascii=False, indent=4)



#for x in data:
#    x["station count"] = len(x['stations'])
    #print(len(x['stations']))

#with open('/Users/apple/Documents/new_mod.json', 'w', encoding='utf-8') as f:
#    json.dump(data, f, ensure_ascii=False, indent=4)
#{
#        "type": "Feature",
#        "geometry": {
#            "type": "point",
#            "coordinates": coords
#        }
#    }