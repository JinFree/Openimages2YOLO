#!/bin/bash
python3 open_images_downloader.py \
	 --class-names "Person, Car" \
	 --data=data/cctv_raw \
	 --max-images=100 \
	 --num-workers=2
