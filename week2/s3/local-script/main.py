#!/usr/bin/env python3

# "Build a grid from files in a source folder"
import glob
import math
from PIL import Image

tile_size = 100
# using the glob module in Python to search for all .jpg in the directory
source_images = glob.glob('source/*.jpeg')
image_count = len(source_images)

# calc the height, width of the grid
titles_width = math.floor(math.sqrt(image_count))
titles_height = math.ceil(image_count / titles_width)

print(f"Converting: {image_count} source images. Creating: {titles_width} x {titles_height} grid.")

# create new image with given size
destination_image = Image.new(mode="RGB", size=(titles_width * tile_size, titles_height * tile_size))
# loop for each tile and draw source image into grid image
for y in range(titles_height):
	for x in range(titles_width):
		if source_images:
			filename = source_images.pop()
			with open(filename, 'rb') as fd:
				img = Image.open(fd)
				image_width = img.size[0]
				image_height = img.size[1]
				# crop the image to a square the length of
				# the shorted side
				crop_square = min(img.size)
				img = img.crop(((image_width - crop_square) // 2,
								(image_height - crop_square) // 2,
								(image_width + crop_square) // 2,
								(image_height + crop_square) // 2))
				img = img.resize((tile_size, tile_size))
				# draw the ijmage onto the destination grid
				destination_image.paste(img, (x*tile_size, y*tile_size))

# save the output image
destination_image.save("destination/grid.jpg")
