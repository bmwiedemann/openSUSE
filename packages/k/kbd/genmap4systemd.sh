#!/bin/bash

# Generate entries for systemd's /usr/share/systemd/kbd-model-map

if [ $# -eq 0 ]; then
  pushd /usr/share/kbd/keymaps/xkb > /dev/null || exit 1
else
  pushd > /dev/null $1 || exit 1
fi

echo "# generated from xkb generated keymaps (basic layouts *without* variant)"
for i in $(ls *.map.gz|grep -v "-"); do
  consolelayout=$(echo $i|sed 's/.map.gz//g')
  layout=$consolelayout
  variant="-"
  printf '%s' "$consolelayout"
  printf "\t\t\t"
  printf '%s' "$layout"
  printf '\t'
  printf 'microsoftpro\t\t'
  printf '%s' "$variant"
  printf '\t\t'
  printf 'terminate:ctrl_alt_bksp\n'
done | sort -u

echo "# generated from xkb generated keymaps (layouts *with* variant)"
for i in $(ls *-*.map.gz); do 
  consolelayout=$(echo $i|sed 's/.map.gz//g')
  conlen=$(echo "$consolelayout" |wc -m)
  conlen=$((conlen - 1))

  layout=$(echo $i|cut -d "-" -f 1)

  variant=$(echo $i|cut -d "-" -f 2,3,4,5,6,7,8,9,10|cut -d "." -f1)
  varlen=$(echo $variant|wc -m)
  varlen=$((varlen -1))

  printf '%s' "$consolelayout"
  if [ $conlen -lt 8 ]; then
    printf "\t\t\t"
  elif [ $conlen -lt 16 ]; then 
    printf "\t\t"
  elif [ $conlen -lt 24 ]; then 
    printf "\t"
  else
    printf ' '
  fi
  printf '%s' "$layout"
  printf '\t'
  if [ "$layout" == "br" ]; then
    printf 'abnt2\t\t'
  elif [ "$layout" == "jp" ]; then
    printf 'jp106\t\t'
  else
    printf 'microsoftpro\t\t'
  fi
  printf '%s' "$variant"
  if [ $varlen -lt 8 ]; then
    printf "\t\t"
  elif [ $varlen -lt 16 ]; then 
    printf "\t"
  else
    printf ' '
  fi
  printf 'terminate:ctrl_alt_bksp\n'

done | sort -u

popd > /dev/null

