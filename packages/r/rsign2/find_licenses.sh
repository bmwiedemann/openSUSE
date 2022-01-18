#!/bin/bash

# written by cunix in 2019
# corrected by Bernhard Wiedemann in 2020 (pipe through sort)
# updated by cunix in 2021
#
# Tries to find and prepare licenses from vendored packages for
# installation as file or link to existing file.
#
# $1 should be a destination directory for vendored licenses

vendor_licenses_dir=$1
username=$(whoami)
workingdir=$(pwd)
licenses_file=$(mktemp /tmp/license_files_XXXXXXXXXX.txt)
goahead=0
hash_list=()
filename_list=()
legal_file_names="copying copyright legal licence license notice patents unlicense"

if [[ -z "$vendor_licenses_dir" ]]
  then
    echo missing directory as parameter
    exit 1
  else
    if [[ "$vendor_licenses_dir" = "/" ]] || [[ "$vendor_licenses_dir" = "/home" ]] \
      || [[ "$vendor_licenses_dir" = "/home/" ]] || [[ "$vendor_licenses_dir" = "/home/$username" ]] \
      || [[ "$vendor_licenses_dir" = "/home/$username/" ]] || [[ "$vendor_licenses_dir" = "$HOME" ]]
      then
        echo Do not use "$vendor_licenses_dir" as destination directory.
        echo It will delete all your files.
        exit 1
      else
        mkdir -pv $vendor_licenses_dir
        if [[ -d "$vendor_licenses_dir" ]]
          then
            echo Searching for licenses ...
            rm $licenses_file
            for item in $legal_file_names
              do
                echo searching for file names starting with $item
                find ./*/ -iname  "$item*" | sort >> $licenses_file
              done
            goahead=1
          else
            echo "$vendor_licenses_dir" is not a directory.
            exit 1
          fi
      fi
  fi

if [[ -f "$licenses_file" ]]
  then
    if [[ $goahead -eq 1 ]]
      then
        echo Removing $vendor_licenses_dir
        rm -r "$vendor_licenses_dir"
        mkdir -pv $vendor_licenses_dir
        echo Processing licenses . . .
        while read line
          do
            filenamepre=${line////__}
            filename=${filenamepre//.__/}
            hash_output=$(sha256sum $line)
            hash=${hash_output:0:66}
            hash_list_len=${#hash_list[@]}
            if [[ $hash_list_len -eq 0 ]]
              then
                cat $line > $vendor_licenses_dir/$filename
                hash_list[0]=$hash
                filename_list[0]=$filename
              else
                counter=0
                match=0
                for item in ${hash_list[@]}
                  do
                    if test $item = $hash
                      then
                        match=1
                        break
                      fi
                    counter=$(($counter+1))
                  done
                if [[ $match -eq 0 ]]
                  then
                    hash_list[$counter]=$hash
                    filename_list[$counter]=$filename
                    cat $line > $vendor_licenses_dir/$filename
                  else
                    cd $vendor_licenses_dir
                    ln -s ${filename_list[$counter]} $filename
                    cd $workingdir
                  fi
              fi
          done < $licenses_file
      else
        echo Does not package licenses.
        exit 1
      fi
  else
    echo No licenses found to package.
  fi
