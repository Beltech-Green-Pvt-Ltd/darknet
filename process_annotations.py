import json
import glob
import shutil

categories = ['man', 'car', 'bike', 'auto', 'truck', 'bus', ' ambulance']


maps = {}
for cat in categories:
    maps[cat] = cat

maps["JCB"] = 'truck'
maps["jcb"] = 'truck'

maps['Police'] = 'man'
maps["bike_1"] = 'bike'
maps["bike_2"] = 'bike'
maps["bike_3"] = 'bike'

maps["tractor"] = "truck"

maps["animal"] = "NIL"
maps["traffic-sign"] = "NIL"
maps["traffic-light"] = "NIL"
maps["signal"] = "NIL"

maps["bike-1"] = 'bike'
maps["bike-2"] = 'bike'
maps["bike-3"] = 'bike'
maps['bike_'] = 'bike'

maps["bicycle_1"] = 'bicycle'
maps["bicycle_2"] = 'bicycle'
maps["bicycle_3"] = 'bicycle'
maps["bycycle"] = 'bicycle'

maps["bicycle-1"] = 'bicycle'
maps["bicycle-2"] = 'bicycle'
maps["bicycle-3"] = 'bicycle'

maps["bycycle_1"] = 'bicycle'
maps["bycycle_2"] = 'bicycle'
maps["bycycle_3"] = 'bicycle'

maps["tempo"] = "auto"
maps["ambulance"] = "car"

maps['motorcycle'] = 'bike'
maps['police-bike_1'] = 'bike'

maps["helmet"] = "NIL"
maps["men"] = "man"
maps["nen"] = "man"
maps["m"] = "man"

maps["no-helmet"] = "NIL"
maps["no_helmet"] = "NIL"
maps["police"] = "man"
maps["police man"] = "man"

maps["police-bus"] = "bus"
maps['nbus'] = 'bus'
maps['police-car'] = "car"
maps['acr'] = 'car'
maps['traffic_men'] = 'man'
maps['police-bike'] = 'bike'

maps['police-bike_1'] = 'bike'
maps['police-bike_2'] = 'bike'
maps['police-bike_3'] = 'bike'

maps['police_bike_1'] = 'bike'
maps['police_bike_2'] = 'bike'
maps['police_bike_3'] = 'bike'


maps['police-bike-1'] = 'bike'
maps['police-bike-2'] = 'bike'
maps['police-bike-3'] = 'bike'

maps['fire-truck'] = 'truck'

maps['traffic_sign'] = 'NIL'
maps['traffic sign'] = 'NIL'
maps['trffic-sign'] = 'NIL'

json_files = glob.glob("Annotations/*.json")

for json_file in json_files:
    print(json_file)
    with open(json_file) as f:
        data = json.load(f)
    txt_file = []
    H, W = data['imageHeight'], data['imageWidth']
    if len(data['shapes']):
        txt_file = []
        for shape in data['shapes']:
            if maps[shape['label']] in categories:
                c = categories.index(maps[shape['label']])
                x = (shape['points'][0][0] + shape['points'][1][0])/2.0
                y = (shape['points'][0][1] + shape['points'][1][1])/2.0
                w = abs(shape['points'][0][0] - shape['points'][1][0])
                h = abs(shape['points'][0][1] - shape['points'][1][1])
                txt_file.append(str(c) + " " + str(x/W) + " " + str(y/H) + " " + str(w/W) + " " + str(h/H))
        try:
            shutil.copy("Annotations/" + data["imagePath"], "YOLO-Annotations/" + data["imagePath"])
            with open("YOLO-" + json_file.replace(".json", ".txt").replace(" - Copy", ""), 'w') as f:
                for item in txt_file:
                    f.write("%s\n" % item)
        except:
            pass  
    else:
        print("empty json annotation observed rejecting")
