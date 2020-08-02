#!/bin/bash
for type in byte char short int long; do
    case $type in
        int) object=Integer ;;
        char) object=Character ;;
        *) object=${type^} ;;
    esac
    hash='(int) key'
    if [ $type = long ]; then
        hash='(int) (key ^ (key >>> 32))'
    fi
    mkdir -p target/generated-sources/collections/java
    for file in `find src/main/templates -name '*.template'`; do
        filename=$(basename $file | sed "s/K/${type^}/;s/\.template/.java/")
        sed -e "s/@k@/${type}/g" \
            -e "s/@K@/${type^}/g" \
            -e "s/@O@/${object}/g" \
            -e "s/@KEY_NUMBER_METHOD@/${type}Value/g" \
            -e "s/@HASH_CODE@/${hash}/g" \
            $file > target/generated-sources/collections/java/$filename
    done
done
