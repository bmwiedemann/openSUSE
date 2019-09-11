#!/bin/bash
# we always start in /home/abuild but in older distros we wouldnt find the sources that way.
# switch to /usr/src/packages/
if [ ! -d $PWD/rpmbuild ] ; then
  cd /usr/src/packages/
fi
shopt -s nullglob
# options may be followed by one colon to indicate they have a required argument
if ! options=$(getopt -o dEf -l default-gem:,build-root:,gem-name:,gem-version:,gem2rpm-config: -- "$@")
then
    # something went wrong, getopt will put out an error message for us
    exit 1
fi

eval set -- "$options"

otheropts="--local -t /usr/lib/rpm/gem_packages.template" 
defaultgem=
buildroot=
gemfile=
gemname=
gemversion=

while [ $# -gt 0 ]
do
    case $1 in
    --default-gem) defaultgem=$2 ; shift;;
    --gem-name) gemname="$2" ; shift;;
    --gem-version) gemversion="$2" ; shift;;
    --build-root) buildroot=$2; shift;;
    --gem2rpm-config) gem_config=$2; shift;;
    (--) ;;
    (-*) otheropts="$otheropts $1";;
    (*) gemfile=$1; otheropts="$otheropts $1"; break;;
    esac
    shift
done

if [ "x$gem_config" = "x" ] ; then 
  gem_config=$(find $RPM_SOURCE_DIR -name "*gem2rpm.yml")
  if [ "x$gem_config" != "x" ] ; then 
    otheropts="$otheropts --config=$gem_config"
  fi
fi

if [ "x$gemfile" = "x" ] ; then 
  gemfile=$(find . -maxdepth 2 -type f -name "$defaultgem" -not -path \*/.gem/\* | head -n 1)
  # if still empty, we pick the sources
  if [ "x$gemfile" = "x" ] ; then
    gemfile=$(find $RPM_SOURCE_DIR -name "$defaultgem")
  fi
  otheropts="$otheropts $gemfile"
fi
# workaround for rubinius bug
# https://github.com/rubinius/rubinius/issues/2732
export LC_ALL="en_US.UTF-8"
export LANG="en_US.UTF-8"
set -x
for gr in $(/usr/bin/ruby-find-versioned gem2rpm) ; do
  $gr $otheropts
done
