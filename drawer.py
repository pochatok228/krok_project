import cv2 as cv
import PIL
import json

def floodFill(x,y, d,e,f, g,h,i, image):
    toFill = set()
    toFill.add((x,y))
    while not toFill.empty():
        (x,y) = toFill.pop()
        (a,b,c) == image.getpixel((x,y))
        if not (a,b,c) == (255, 255, 255):
            continue
        image.putpixel((x,y), (g,h,i))
        toFill.add((x-1,y))
        toFill.add((x+1,y))
        toFill.add((x,y-1))
        toFill.add((x,y+1))
    image.save("flood.png")

def main(stats):
	with open("districts.json", 'r', encoding='utf-8') as file:
		districts_list = json.loads(file.read())

	values = [pare[1] for pare in stats]
	max_value = max(values)
	min_value = min(values)
	step = (max_value - min_value) / 5
	b1, b2, b3, b4 = min_value + step, min_value + step*2, min_value + step*3, min_value + step * 4
	image = cv.imread("map.png")
