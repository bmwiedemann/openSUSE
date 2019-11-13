#!/bin/bash
cvs -d :pserver:anonymous:anonymous@gee.cs.oswego.edu/home/jsr166/jsr166 login
cvs -d :pserver:anonymous@gee.cs.oswego.edu/home/jsr166/jsr166 export -r release-1_7_0 jsr166
rm -r jsr166/src/main/java
rm -r jsr166/src/jsr166x jsr166/.cvsignore
rm -r jsr166/src/jsr166y
rm -r jsr166/src/loops
rm -r jsr166/src/test/jtreg
rm -r jsr166/src/test/loops
rm -r jsr166/src/test/tck
find jsr166 -type f -name "*.jar" -delete
find jsr166 -type f -name "*.class" -delete
tar cJf jsr166-1.7.0.tar.xz jsr166
