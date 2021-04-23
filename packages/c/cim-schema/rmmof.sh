#!/bin/sh

OWLM=/usr/bin/ow-rmmof.sh
PEGLM=/usr/bin/peg-rmmof.sh

if [ -x $OWLM ]; then
  $OWLM $@
fi

if [ -x $PEGLM ]; then
  $PEGLM $@
fi

