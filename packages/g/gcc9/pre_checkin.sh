#!/bin/bash
# This script is called automatically during autobuild checkin.

case $0 in
  \./*)
    here=$PWD
    ;;
  */*)
    here=${0%/*}
    ;;
  *)
    here=$PWD
    ;;
esac
case ${here##*/} in
  gcc*.*)
    # Handle maintainance projects with .$REPO suffix
    suffix=${here##*/}
    suffix=${suffix%%\.*}
    set ${suffix#gcc}
    ;;
  gcc-*)
    suffix=${here##*/}
    set ${suffix#*-}-
    ;;
  gcc[0-9]*)
    suffix=${here##*/}
    set ${suffix#gcc}
    ;;
esac
. ${here}/change_spec
