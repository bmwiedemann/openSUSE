#!/usr/bin/sh
cp graphviz.changes graphviz-addons.changes
sed \
    -e 's:%bcond_with extras:%bcond_without extras:' \
    -e 's#Name:           graphviz#Name:           graphviz-addons#' \
    -e 's#spec file for package graphviz#spec file for package graphviz-addons#' \
    graphviz.spec > graphviz-addons.spec
