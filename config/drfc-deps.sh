#!/usr/bin/env bash

mkdir drfc-images

mkdir scripts

git clone https://github.com/aws-deepracer-community/deepracer-for-cloud.git

cd deepracer-for-cloud || exit

mv docker/* ../drfc-images

mv scripts/training/prepare-config.py ../scripts

cd ..

sudo rm -r deepracer-for-cloud

