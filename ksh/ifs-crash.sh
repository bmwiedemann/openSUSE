#!/bin/ksh

typeset -lui count=${1:-4}

function g
{
  IFS=
}

function f
{
  typeset IFS
  (g)
  : $V
}

while ((count-- > 0))
do
  f
done

function crash
{
  typeset L_FILE
  typeset L_VALIDATION
  typeset L_VARIABLE
  typeset L_MOD IFS

  OS=$(uname)
}

crash

function crash2
{
  typeset IFS
  IFS='\t'
  true
  unset IFS
  echo a b c | while read x y z; do
    echo $x
    echo $y
    echo $z
  done
}

crash2

echo a b c | while read x y z; do
  echo $x
  echo $y
  echo $z
done

echo "[${0##*/}: success]"
# end here
