#!/bin/bash
python3 open_images_downloader.py \
	 --class-names "Person, Car, Bus, Truck, Ambulance, Bicycle, Motorcycle" \
	 --data=data \
	 --max-images=10000 \
	 --num-workers=2
