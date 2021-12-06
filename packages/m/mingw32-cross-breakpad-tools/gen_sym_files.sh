#!/bin/sh

# $1 filename
if [ -z "$1" ];
then
	echo "ERROR: filename must not be empty"
	exit -1
fi

# $2 target directory
if [ -z "$2" ];
then
	TARGET_DIR="symbols"
else
	TARGET_DIR="$2"
fi

# $3 path mapping <src>:<dest>
if [ -z "$3" ];
then
	PATH_MAP=""
else
	regex=`echo $3 | sed 's#:#,#g'`
	PATH_MAP=" | sed 's,$regex,g'"
fi


FILE=`basename $1`
SYMFILE="$FILE.sym"
i686-w64-mingw32-dump_syms $1 $PATH_MAP > $SYMFILE

BUILDID=`head -n1 $SYMFILE | cut -f4 -d ' '`
if [ "$BUILDID" == "000000000000000000000000000000000" ];
then
	echo "ERROR: buildid is empty in $SYMFILE"
	exit -1
fi

DESTINATION_DIR="$TARGET_DIR/$FILE/$BUILDID"
DESTINATION_FILE="$DESTINATION_DIR/$SYMFILE"

mkdir -p $DESTINATION_DIR
mv $SYMFILE $DESTINATION_FILE
echo $DESTINATION_FILE
