#!/bin/bash
#
# Installs the DocBook XSL Stylesheets on openSUSE systems
#
# Author: Thomas Schraitle
# Copyright 2016-2018 toms@opensuse.org
#

# set -x

ME=${0##*/}
#
PACKAGE=docbook-xsl-stylesheets
PACKAGE_VERSION=
SOURCEDIR=

#----------------------------------------------------------------------
# System variables
BUILDROOT=
PREFIX=/usr
BINDIR=$PREFIX/bin
DATADIR=share
DOCDIR=$DATADIR/doc/packages
SYSCONFDIR=/etc
XMLCONFDIR=$SYSCONFDIR/xml
XMLDIR=$DATADIR/xml
XMLCATALOGDIR=$XMLCONFDIR/catalog.d
DBSTYLE_CATALOG=$XMLCATALOGDIR/$PACKAGE.xml
DB_XSL_ROOTDIR=$XMLDIR/docbook/stylesheet
DB_XSL_SUFFIX=nwalsh
DBSTYLE_DIR=$DB_XSL_ROOTDIR/$DB_XSL_SUFFIX
SYS_DBSTYLE_DIR=$PREFIX/$DBSTYLE_DIR

INSTALL_SCRIPTS=0


function exit_on_error() {
   local result
   result=${2:-1}
   echo "ERROR: ${1}" >&2
   exit $result;
}


function my_debug() {
# Syntax: my_debug "MESSAGE" [MORE ARGUMENTS...]
# Prints debug messages, if DEBUG_SCRIPT is non-empty
    if [[ "$DEBUG_SCRIPT" ]]; then
        echo -n -e "[debug] ${ME}: $@\n" >&2;
    fi
}

function usage() {
   cat << EOF
Installs the DocBook XSL Stylesheets

Usage:
$ME [OPTIONS]

Fine tuning of the installation directories:
  --buildroot=DIR         build root directory []
  --prefix=DIR            [${PREFIX}]
  --bindir=DIR            user executables [${BINDIR}]
  --sysconfdir=DIR        read-only single-machine data [${SYSCONFDIR}]
  --datarootdir=DIR       read-only arch.-independent data root [PREFIX/DATADIR]
  --datadir=DIR           read-only architecture-independent data [${DATADIR}]
  --docdir=DIR            documentation root [PREFIX/${DOCDIR}]
  --catalog-dir=DIR       XML catalog directory to store all catalog files [${XMLCATALOGDIR}]
  --db-xsl-suffix=SUFFIX  the suffix that is appended to the DocBook stylesheet dir [${DB_XSL_SUFFIX}]
  --db-xslt-dir=DIR       root directory for DocBook stylesheets (without version)
                          [DATADIR/xml/docbook/stylesheet/DB_XSL_SUFFIX]

Behaviour
  --skip-install-scripts  Do not install any scripts [False]


Source package options:
  --sourcedir=NAME            directory of source directory
  --package-name=NAME         name of the package [$PACKAGE]
  --package-version=VERSION   version of the package [$PACKAGE_VERSION]

EOF
}

function printvariables() {
my_debug "Currently set variables:"
cat << EOF
package=$PACKAGE
package-version=$PACKAGE_VERSION
sourcedir=$SOURCEDIR
buildroot=$BUILDROOT
prefix=$PREFIX
bindir=$BINDIR
datadir=$DATADIR
docdir=$DOCDIR
xmldir=$XMLDIR
xsltrootdir=$XSLTROOTDIR
dbstyle_dir=$DBSTYLE_DIR
db_xsl_suffix=$DB_XSL_SUFFIX
#
sysconfdir=$SYSCONFDIR
xmlconfdir=$XMLCONFDIR
xmlcatalogdir=$XMLCATALOGDIR
dbstyle_catalog=$DBSTYLE_CATALOG
EOF
}

#----------------------------------------------------------------------
#
DEBUG_SCRIPT=

# Source Installation directories:
DBXSLT_DIRS="assembly common eclipse epub epub3 extensions fo \
             images highlighting html htmlhelp lib javahelp manpages params \
             profiling roundtrip slides template webhelp website xhtml xhtml-1_1 xhtml5"
# Without catalog.xml
DBXSLT_FILES="VERSION VERSION.xsl"
# Without INSTALL
DBXSLT_DOCFILES="AUTHORS BUGS COPYING NEWS.html NEWS.xml README TODO \
RELEASE-NOTES.html RELEASE-NOTES.pdf RELEASE-NOTES.txt RELEASE-NOTES.xml"


#----------------------------------------------------------------------
# printing help / catching errors
#

if [[ -z "$1" ]]; then
  usage
  printvariables
  exit
fi

# datarootdir:,
longopt="help,debug,buildroot:,sourcedir:,\
package-name:,package-version:,\
bindir:,prefix:,datadir:,docdir:,sysconfdir:,\
skip-install-scripts,\
db-xslt-dir:,db-xsl-suffix:,catalog-dir:"

export POSIXLY_CORRECT=1
ARGS=$(getopt -o h,d -l $longopt -n $ME -- "$@")
eval set -- "$ARGS"
while true ; do
   case "$1" in
      -h|--help)
         usage
         # printvariables
         exit
         ;;
      -d|--debug)
         DEBUG_SCRIPT=1
         shift
         ;;
      #
      --sourcedir)
         SOURCEDIR=$2
         shift 2
         ;;
      #
      --package-name)
         PACKAGE=$2
         shift 2
         ;;
      #
      --package-version)
         PACKAGE_VERSION="$2"
         shift 2
         ;;
      #
      --buildroot)
         BUILDROOT=$2
         shift 2
         ;;
      --bindir)
         BINDIR=$2
         shift 2
         ;;
      --prefix)
         PREFIX=$2
         shift 2
         ;;
      #--datarootdir)
      #   DATAROOTDIR=$2
      #   shift 2
      #   ;;
      --datadir)
         DATADIR=$2
         shift 2
         ;;
      --docdir)
         DOCDIR=$2
         shift 2
         ;;
      --sysconfdir)
         SYSCONFDIR=$2
         shift 2
         ;;
      #
      --catalog-dir)
        XMLCATALOGDIR=$2
        shift 2
        ;;
      #
      --db-xslt-dir)
        DBSTYLE_DIR=$2
        shift 2
        ;;
      #
      --db-xsl-suffix)
        DB_XSL_SUFFIX=$2
        echo ">>>> $2"
        shift 2
        ;;
      --printvariables)
         printvariables
         exit 1
         ;;
      #
      --skip-install-scripts)
         INSTALL_SCRIPTS=1
         shift
         ;;
      --)
         break
         ;;
   esac
done
unset POSIXLY_CORRECT

PREFIX=$BUILDROOT$PREFIX
BINDIR=$BUILDROOT$BINDIR
DATADIR=$PREFIX/$DATADIR
DOCDIR=$PREFIX/$DOCDIR
XMLDIR=$PREFIX/$XMLDIR
XSLTROOTDIR=$PREFIX$XSLTROOTDIR
DBSTYLE_DIR=$PREFIX/$DB_XSL_ROOTDIR/$DB_XSL_SUFFIX
#
SYSCONFDIR=$BUILDROOT$SYSCONFDIR
XMLCONFDIR=$BUILDROOT$XMLCONFDIR
XMLCATALOGDIR=$BUILDROOT$XMLCATALOGDIR
# DBSTYLE_CATALOG=$BUILDROOT$DBSTYLE_CATALOG
DBSTYLE_CATALOG=$XMLCATALOGDIR/$PACKAGE.xml

printvariables

# exit 1

# Consistency check
[[ -z $SOURCEDIR ]] && exit_on_error "Source directory not set. Use --sourcedir DIRECTORY"

# exit 100


#----------------------------------------------------------------------
#
#
function create_directory_structure() {
   local i
   my_debug "\n\n=== Create directory structure ==="
   for i in $PREFIX $BINDIR $DATADIR $XMLCATALOGDIR \
            $DOCDIR/$PACKAGE/html $DBSTYLE_DIR/$PACKAGE_VERSION; do
      mkdir ${DEBUG_SCRIPT:+-v} -p $i
      [[ $? -ne 0 ]] && exit_on_error "Could not create $i directory"
   done
}


#----------------------------------------------------------------------
#
#
function install_dbxsltdirs() {
   my_debug "\n\n=== Install all DocBook XSL stylesheet directories ==="

   for dir in $DBXSLT_DIRS; do
     my_debug "Copy directory $dir..."
     cp -a $SOURCEDIR/$dir $DBSTYLE_DIR/$PACKAGE_VERSION
   done
}

function install_scripts() {
   my_debug "\n\n=== Install scripts ==="

   install ${DEBUG_SCRIPT:+-v} -m755 $SOURCEDIR/fo/pdf2index       $BINDIR
   install ${DEBUG_SCRIPT:+-v} -m755 $SOURCEDIR/epub/bin/dbtoepub  $BINDIR
   # install ${DEBUG_SCRIPT:+-v} -m755 $SOURCEDIR/slides/images/callouts/gen.sh $BINDIR/callout-gen
   # rm fo/pdf2index epub/bin/dbtoepub slides/images/callouts/gen.sh
}

function install_dbxsltfiles() {
   my_debug "\n\n=== Install other files ==="

   for file in $DBXSLT_FILES; do
     my_debug "Copy $file..."
     cp -a $SOURCEDIR/$file $DBSTYLE_DIR/$PACKAGE_VERSION
   done
}

function install_dbxsltdocfiles() {
   my_debug "\n\n=== Install documentation ==="
   my_debug "    Current dir: $PWD"

   for file in $DBXSLT_DOCFILES; do
      cp ${DEBUG_SCRIPT:+-v} $SOURCEDIR/$file $DOCDIR/$PACKAGE
      # $DBSTYLE_DIR/$PACKAGE_VERSION
   done
}

function create_link() {
    my_debug "\n\n=== Create link ==="
    pushd $DBSTYLE_DIR
    ln ${DEBUG_SCRIPT:+-v} -s ${PACKAGE_VERSION} current
    popd
}

function create_dbxslt_catalog() {
   my_debug "\n\n=== Create catalog file ==="

   # /etc/xml/catalog.d/docbook-xsl-stylesheets.xml
   xmlcatalog --noout --create $DBSTYLE_CATALOG
}

function create_dbxslt_addentries() {
   my_debug "\n\n=== Create entries in the catalog file ==="

   DBSTYLE_DIR=$DB_XSL_ROOTDIR/$DB_XSL_SUFFIX
   # Don't be confused, see docbook-apps mailinglist
   local CDN4_XSL_URL="http://cdn.docbook.org/release/xsl-nons"
   local CDN5_XSL_URL="http://cdn.docbook.org/release/xsl"
   local DB4_XSL_URL="http://docbook.sourceforge.net/release/xsl/"
   local DB5_XSL_URL="http://docbook.sourceforge.net/release/xsl-ns/"

   local CDN_XSL_URL DB_XSL_URL
     
   CDN_XSL_URL=$CDN4_XSL_URL
   DB_XSL_URL=$DB4_XSL_URL
   
   # This is flaky and not ideal. :-(
   if [[ $DB_XSL_SUFFIX = "nwalsh5" ]]; then
        CDN_XSL_URL=$CDN5_XSL_URL
        DB_XSL_URL=$DB5_XSL_URL
   fi

   my_debug "Using URL=${DB_XSL_URL}"
   my_debug "Using URL=${CDN_XSL_URL}"
   my_debug "Using system path=${DBSTYLE_DIR}"
   
   # Create first the old DocBook SF identifiers:
   xmlcatalog --noout --add "rewriteSystem" \
      "${DB_XSL_URL}${PACKAGE_VERSION}" \
      "file://$SYS_DBSTYLE_DIR/${PACKAGE_VERSION}" $DBSTYLE_CATALOG
   xmlcatalog --noout --add "rewriteURI" \
      "${DB_XSL_URL}${PACKAGE_VERSION}" \
      "file://$SYS_DBSTYLE_DIR/$PACKAGE_VERSION" $DBSTYLE_CATALOG
   xmlcatalog --noout --add "rewriteSystem" \
      "${DB_XSL_URL}current" \
      "file://$SYS_DBSTYLE_DIR/current" $DBSTYLE_CATALOG
   xmlcatalog --noout --add "rewriteURI" \
      "${DB_XSL_URL}current" \
      "file://$SYS_DBSTYLE_DIR/current" $DBSTYLE_CATALOG
   # Create the new DocBook XSL identifier:
   xmlcatalog --noout --add "rewriteURI" \
      "${CDN_XSL_URL}/${PACKAGE_VERSION}" \
      "file://$SYS_DBSTYLE_DIR/${PACKAGE_VERSION}" $DBSTYLE_CATALOG
    xmlcatalog --noout --add "rewriteSystem" \
      "${CDN_XSL_URL}/${PACKAGE_VERSION}" \
      "file://$SYS_DBSTYLE_DIR/${PACKAGE_VERSION}" $DBSTYLE_CATALOG
    xmlcatalog --noout --add "rewriteURI" \
      "${CDN_XSL_URL}/current" \
      "file://$SYS_DBSTYLE_DIR/current" $DBSTYLE_CATALOG
    xmlcatalog --noout --add "rewriteSystem" \
      "${CDN_XSL_URL}/current" \
      "file://$SYS_DBSTYLE_DIR/current" $DBSTYLE_CATALOG
}


function cleanup_buildroot() {
   rm $DBSTYLE_DIR/$PACKAGE_VERSION/fo/pdf2index \
      $DBSTYLE_DIR/$PACKAGE_VERSION/epub/bin/dbtoepub \
      $DBSTYLE_DIR/$PACKAGE_VERSION/slides/images/callouts/gen.sh
}

#----------------------------------------------------------------------
# MAIN
#

[[ -e "$SOURCEDIR" ]] || exit_on_error "Could not find directory $SOURCEDIR"
#
#
create_directory_structure
install_dbxsltdirs
install_dbxsltfiles
[[ 0 -eq $INSTALL_SCRIPTS ]] && install_scripts

# install_dbxsltdocfiles
create_link
#
# create_dbxslt_catalog
# create_dbxslt_addentries
# cleanup_buildroot

my_debug "\n\n=== Finished script."

# EOF
