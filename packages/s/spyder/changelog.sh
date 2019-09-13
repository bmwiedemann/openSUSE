#!/bin/bash

xclip -o | egrep -v "(^[-\s]*$|^In this release )" | sed -E 's/^### ([A-Za-z ]+)/ - \1:/' | sed -E 's/^\* /  - /' | sed -E 's/^## Version ([0-9.]+) \([0-9-]+\)/- update to version \1:/' | xclip -i
