#!/usr/bin/env sh

# wlprop
#
# Licensed under the MIT license
# Copyright © 2022 bjosephmitchell@gmail.com
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the “Software”), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
# 
# Dependencies:
# - swaymsg
# - jq
# - slurp
# - awk

# Get the sway tree and store the output
SWAY_TREE=$(swaymsg -t get_tree | jq -r '.. | select(.pid? and .visible?)')

# Invoke slurp to let the user select a window
SELECTION=$(echo $SWAY_TREE | jq -r '.rect | "\(.x),\(.y) \(.width)x\(.height)"' | slurp)

# Extract the X, Y, Width, and Height from the selection
X=$(echo $SELECTION | awk -F'[, x]' '{print $1}')
Y=$(echo $SELECTION | awk -F'[, x]' '{print $2}')
W=$(echo $SELECTION | awk -F'[, x]' '{print $3}')
H=$(echo $SELECTION | awk -F'[, x]' '{print $4}')

# Find the window matching the selection
echo $SWAY_TREE | jq -r --argjson x $X --argjson y $Y --argjson w $W --argjson h $H \
  '. | select(.rect.x == $x and .rect.y == $y and .rect.width == $w and .rect.height == $h)'

