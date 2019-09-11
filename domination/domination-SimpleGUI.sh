#!/bin/sh

cd /usr/share/domination  && exec "/usr/bin/java" \
-cp Domination.jar net.yura.domination.ui.simplegui.RiskGUI "${@}"
