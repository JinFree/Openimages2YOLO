#!/bin/bash
python3 open_images_downloader.py \
	 --class-names "Person, Car" \
	 --data=data \
	 --max-images=2000 \
	 --num-workers=2
