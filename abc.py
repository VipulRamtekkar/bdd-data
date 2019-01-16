import cv2 
import json 
import sys 
import numpy as np 

def get_lanes(objects):
    return [o for o in objects
            if 'poly2d' in o and o['category'][:4] == 'lane']

def parse_args():

    parser = argparse.ArgumentParser()
    parser.add_argument('--image-dir', help='image directory')
    parser.add_argument("-l", "--label", required=True,
                        help="corresponding bounding box annotation "
                             "(json file)", type=str)
    args = parser.parse_args()
    return args
parse_args()

label_paths = [args.label]
if isdir(args.label):
    input_names = sorted(
        [splitext(n)[0] for n in os.listdir(args.label)
         if splitext(n)[1] == '.json'])
    label_paths = [join(args.label, n + '.json') for n in input_names]

a = sys.argv[1]

label_path = label_paths[current_index]

with open(label_path) as data_file:
    label = json.load(data_file)

objects = label['frames'][0]['objects']

objects = get_lanes(objects)

colors = np.array([[0, 0, 0, 255],
                   [255, 0, 0, 255],
                   [0, 0, 255, 255]]) / 255

for obj in objects:
    if self.color_mode == 'random':
        if obj['attributes']['direction'] == 'parallel':
            color = colors[1]
        else:
            color = colors[2]
        alpha = 0.9
    else:
        color = (
            (1 if obj['category'] == 'area/drivable' else 2) / 255.,
            obj['id'] / 255., 0)
        alpha = 1
