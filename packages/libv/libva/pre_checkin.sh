#!/bin/sh

sed -e 's,build_gl 0,build_gl 1,' libva.spec > libva-gl.spec
sed -e 's,^Name:.*,Name: libva-gl,' -i libva-gl.spec
cp libva.changes libva-gl.changes
