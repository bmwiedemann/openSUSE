#!/bin/bash

# e.g. tar -xzOf pymisp-2.4.102.tar.gz pymisp-2.4.102/CHANGELOG.txt | head -n 131 | xclip -i ; ./changelog.sh ; xclip -o
# and then in `osc vc` for more cleanups

xclip -o | sed -E 's/^(New|Changes|Fix|Other)$/ - \1/' | sed -E 's/^  /    /' | sed -E 's/^[-\*] (.*)$/  - \1/' | sed -E 's/^v([0-9\.]+) \([0-9-]+\)$/- update to version \1:/' | egrep -v '^([=~-]+|Changelog)$' | sed -E 's/ \[(Raphaël ?(Vinot)?|Alexandre ?(Dulaunoy)?)\]?$//' | sed -E 's/\s+(Vinot|Dulaunoy)\]$//' | grep -v '^\s*$' | xclip -i
