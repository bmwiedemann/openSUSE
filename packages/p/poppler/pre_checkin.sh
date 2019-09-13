#!/bin/sh

sed -e 's,build_qt5 0,build_qt5 1,' poppler.spec > poppler-qt5.spec
sed -e 's,^Name:.*,Name: poppler-qt5,' -i poppler-qt5.spec
cp poppler.changes poppler-qt5.changes
