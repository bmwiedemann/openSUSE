#!/bin/bash

JAR=/usr/lib/tomcat/serverxmltool.jar
SERVERXML=/etc/tomcat/server.xml

function usage {
    echo "Usage: <script> add|remove docBase path [contextXmlFile]"
}

if [[ -z "$1" || -z "$2" ]]; then
    usage
    exit 1
fi

CMD="$1"
DOCBASE="$2"
CTXPATH="$3"
CONTEXTXML=${4:-''}

if [ "$CMD" = "add" ]; then
    XSLT="add-context.xslt"
elif [ "$CMD" = "remove" ]; then
    XSLT="remove-context.xslt"
else
    usage
    exit 1;
fi

SUFIX=$(date +%H%M%S%N)
rm -f ${SERVERXML}.new${SUFIX} ${SERVERXML}.old${SUFIX}

/usr/bin/java -jar $JAR  $XSLT $SERVERXML $DOCBASE $CTXPATH $CONTEXTXML > ${SERVERXML}.new${SUFIX}

if [ $? -eq 0 ]; then
    mv $SERVERXML ${SERVERXML}.old${SUFIX}
    mv ${SERVERXML}.new${SUFIX} $SERVERXML
    rm ${SERVERXML}.old${SUFIX}
    if [ "$CMD" = "add" ]; then
        echo "Added webapp $CTXPATH from $DOCBASE to $SERVERXML."
    else
        echo "Removed webapp $CTXPATH from $SERVERXML."
    fi
else
    echo "$SERVERXML was not modified."
    rm ${SERVERXML}.new${SUFIX}
    exit 2
fi