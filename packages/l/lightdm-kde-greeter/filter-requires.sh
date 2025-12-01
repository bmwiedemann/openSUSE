#!/bin/sh
FINDREQ=/usr/lib/rpm/find-requires
$FINDREQ $* | sed \
 -e '/ConnectionEnum.1/d'
