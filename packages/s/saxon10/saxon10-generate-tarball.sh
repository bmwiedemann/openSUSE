#!/bin/sh

SAXON_VERSION=10

wget https://github.com/Saxonica/Saxon-HE/raw/main/${SAXON_VERSION}/resources/saxon-resources-${SAXON_VERSION}.zip -O saxon-resources-${SAXON_VERSION}-cleaned.zip
# Remove script.js and search.js from doc/javadoc/ directory
zip -d saxon-resources-${SAXON_VERSION}-cleaned.zip doc/javadoc/script.js doc/javadoc/search.js
