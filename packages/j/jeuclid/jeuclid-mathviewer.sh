#!/bin/bash
. /usr/share/java-utils/java-functions

MAIN_CLASS=net.sourceforge.jeuclid.app.mathviewer.MathViewer

set_classpath "commons-logging commons-io xmlgraphics-commons batik-all jeuclid-core jeuclid-mathviewer"

run "$@"
