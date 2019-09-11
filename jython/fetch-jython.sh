#!/bin/sh

# Generate a source drop for jython from SVN

# Usage message
usage="usage: $0 <project_name> <svn_root> <svn_tag>"

project_name=$1
svn_root=$2
svn_tag=$3

# Ensure we got all of the variables
if [ "x$project_name"x = "xx" ]
then
        echo >&2 "$usage"
        exit 1
fi

if [ "x$svn_root"x = "xx" ]
then
        echo >&2 "$usage"
        exit 1
fi

if [ "x$svn_tag"x = "xx" ]
then
        echo >&2 "$usage"
        exit 1
fi

mkdir -p temp && cd temp

svn export --username guest --password "" $svn_root/$project_name/tags/$svn_tag
mv $svn_tag/$project_name $project_name-svn-$svn_tag
tar jcf $project_name-fetched-src-$svn_tag.tar.bz2 $project_name-svn-$svn_tag
