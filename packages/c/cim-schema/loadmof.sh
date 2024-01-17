#!/bin/sh

OWLM=/usr/bin/ow-loadmof.sh
PEGLM=/usr/bin/peg-loadmof.sh

if [ -x $OWLM ]; then
  $OWLM $@
fi

if [ -x $PEGLM ]; then
  $PEGLM $@
fi

