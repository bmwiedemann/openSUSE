#!/usr/bin/env python3
 # Copyright (c) 2022 Tamara Schmitz <tamara.schmitz@suse.com>.
 # 
 # This program is free software: you can redistribute it and/or modify  
 # it under the terms of the GNU General Public License as published by  
 # the Free Software Foundation, version 3.
 #
 # This program is distributed in the hope that it will be useful, but 
 # WITHOUT ANY WARRANTY; without even the implied warranty of 
 # MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU 
 # General Public License for more details.
 #
 # You should have received a copy of the GNU General Public License 
 # along with this program. If not, see <http://www.gnu.org/licenses/>.
 #

import argparse
import json

# arg parsing
parser = argparse.ArgumentParser(description="Parse an NVIDIA supported devices\
        JSON and convert it to a pci id list.")
parser.add_argument("INPUT_JSON",
        help="The JSON file to be parsed",
        type=argparse.FileType('r')
        )
parser.add_argument("OUTPUT_PCI_ID_LIST",
        help="The output file to save to",
        type=argparse.FileType('w')
        )
parser.add_argument("--skiplegacy", help="Skip GPUs that are in a legacy branch",
                    action="store_true")
parser.add_argument("--kernelopen", help="Only select GPUs that are supported by\
        the Open GPU kernel modules",
                    action="store_true")
args = parser.parse_args()

# json parsing
json = json.load(args.INPUT_JSON)
pci_id_list = {}
for chip in json["chips"]:
    if args.skiplegacy and "legacybranch" in chip:
        continue
    if args.kernelopen and \
            ("features" not in chip or "kernelopen" not in chip["features"]):
        continue
    if "devid" in chip and "name" in chip:
        pci_id_list[chip["devid"]] = chip["name"]

# write to file
for devid, name in sorted(pci_id_list.items(), key=lambda i: i[0]):
    # there are no duplicates since a dictionary's key is unique
    args.OUTPUT_PCI_ID_LIST.write("%s %s\n" % (devid, name))
