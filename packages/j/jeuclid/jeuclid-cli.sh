#!/bin/bash
. /usr/share/java-utils/java-functions

MAIN_CLASS=net.sourceforge.jeuclid.app.Mml2xxx

set_classpath "commons-logging commons-cli commons-lang xmlgraphics-commons batik-all commons-io jeuclid-core jeuclid-cli"

run "$@"
