#!/bin/sh

# Do not edit the list of locales here: they come from pre_checkin.sh
DEFAULT_LOCALES="en"
RECOMMENDED_LOCALES="de ru it pl es pt fr nl"

if test $# -ne 5; then
  echo "Wrong number of arguments."
  exit 1
fi

buildroot=$1
datadir=$2
recommendedfile=$3
extrasfile=$4
excludedfile=$5

directory=${datadir}/dasher
builddirectory=${buildroot}${directory}

RESULT=

find_locale_for_file() {
  RESULT=

  if test $# -ne 2; then
    echo "Wrong number of arguments in find_locale_for_file."
    exit 1
  fi

  _file="$1"
  _fatal_missing=$2

  _line=`grep -E "$_file |# *$_file" locale-map.txt`

  if test "x$_line" = "x"; then
    if test ! $_fatal_missing; then
      echo "No locale found for $_file."
      exit 1
    else
      return
    fi
  fi

  _locale=`echo $_line | grep -v ^# | sed "s;.* ;;g" | sort -u`

  echo $_locale | grep -q " "
  if test $? -eq 0; then
    echo -n "More than one locale found for $_file: "
    echo $_locale | sed "s;\n;;g"
    exit 1
  fi

  RESULT=$_locale
}

add_file_with_locale() {
  # second argument can be empty
  if test $# -ne 1 -a $# -ne 2; then
    echo "Wrong number of arguments in add_file_with_locale."
    exit 1
  fi

  _file="$1"
  _locale="$2"

  # if this file is commented out, then it's not even a locale and we don't
  # care to have that by default
  if test "x$_locale" = "x"; then
    echo "%exclude ${directory}/${_file}" >> $excludedfile
    echo "${directory}/${_file}" >> $extrasfile
    continue
  fi

  echo "$DEFAULT_LOCALES" | grep -q $_locale
  if test $? -eq 0; then
    # It will be list implicitly in the file list of the main package
    continue
  fi

  echo "%exclude ${directory}/${_file}" >> $excludedfile

  echo "$RECOMMENDED_LOCALES" | grep -q $_locale
  if test $? -eq 0; then
    echo "${directory}/${_file}" >> $recommendedfile
  else
    echo "${directory}/${_file}" >> $extrasfile
  fi
}


echo "%defattr (-, root, root)" > $recommendedfile
echo "%defattr (-, root, root)" > $extrasfile


for file in ${builddirectory}/training_*; do
  file=`basename $file`
  find_locale_for_file $file true
  add_file_with_locale $file $RESULT
done


for file in ${builddirectory}/alphabet.*.xml; do
  # Note: if the file mentions a training file, then the map will be done with
  # the training file if possible.

  training=`grep '<train>' $file | sed "s,<train>,,g;s,</train>,,g" | head -n 1`
  file=`basename $file`
  find_locale_for_file $training false
  locale=$RESULT

  if test "x$locale" = "x"; then
    find_locale_for_file $file true
    locale=$RESULT
  fi

  add_file_with_locale $file $locale
done
