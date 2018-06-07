#!/bin/bash

# This script downloads all data needed for testing lexicon domain adaptation

cd data
curl http://www.clips.uantwerpen.be/sites/default/files/datasets/polisent.zip
unzip polisent.zip
rm polisent.zip
python example.py