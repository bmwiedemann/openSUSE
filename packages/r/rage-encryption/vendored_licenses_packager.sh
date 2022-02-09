#!/bin/bash

# written by cunix in 2019
# corrected by Bernhard Wiedemann in 2020 (pipe through sort)
# updated by cunix in 2021 + 2022


function helper {
  echo Without any guarantee or promise this may be used to try helping
  echo packagers to include some legal files from vendored source code archives.
  echo
  echo Script has to be run twice in spec file:
  echo
  echo 1. in archive directory to find packages with:
  echo     bash path_to_this_file finder path_to_tmp_target_directory
  echo example in section %prep:
  echo     cd vendor
  echo     bash %{SOURCE2} finder vendored
  echo
  echo 2. to install and link found files with:
  echo     bash path_to_this_file installer path_to_tmp_target_directory path_to_buildroot_target_directory
  echo example in section %install:
  echo     install -d -m 0755 %{buildroot}%{_licensedir}/%{name}/vendored
  echo     bash %{SOURCE2} installer vendor/vendored %{buildroot}/%{_licensedir}/%{name}/vendored
  echo
  echo 3. Files should be packaged:
  echo example in section %files:
  echo     %{_licensedir}/%{name}/vendored/
  echo
  echo
  echo Some more details in source code.
}


function finder {
  # Tries to find and prepare licenses from vendored packages for
  # installation as file or link to existing file.
  #
  # $1 should be a destination directory for vendored licenses

  vendor_licenses_dir=$1
  knows_the_risk=$2
  username=$(whoami)
  build_user="abuild"
  workingdir=$(pwd)
  licenses_file=$(mktemp /tmp/license_files_XXXXXXXXXX.txt)
  licenses_directories=$(mktemp /tmp/license_dirs_XXXXXXXXXX.txt)
  real_files=0
  linked_files=0
  goahead=0
  hash_list=()
  filename_list=()

  legal_file_names="copying copyright legal licence license notice patents unlicense"
  legal_directory_names="licence license"

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
          if [[ "$username" != "$build_user" ]]
            then
              if [[ -n "$knows_the_risk" ]]
                then
                  if [[ "$knows_the_risk" = "runanyway" ]]
                    then
                      build_user="$username"
                    fi
                fi
            fi
          if [[ "$username" = "$build_user" ]]
            then
              mkdir -pv $vendor_licenses_dir
              if [[ -d "$vendor_licenses_dir" ]]
                then
                  echo Searching for licenses ...
                  rm $licenses_file $licenses_directories
                  for item in $legal_file_names
                    do
                      echo searching for file names starting with $item
                      found=$(find ./*/ -type f -iname "$item*" | sort)
                      f=$(echo_to_file $licenses_file "$found")
                      echo found: $f
                    done
                  for item in $legal_directory_names
                    do
                      echo searching for directory names starting with $item
                      found=$(find ./*/ -type d -iname "$item*" | sort)
                      d=$(echo_to_file $licenses_directories "$found")
                      echo found: $d
                    done
                  if [[ -f "$licenses_directories" ]]
                    then
                      while read line
                        do
                          fl=$(find $line -type f | sort)
                          f=$(echo_to_file $licenses_file "$fl")
                          echo files added from directory "$line" : $f
                        done < $licenses_directories
                    fi
                  goahead=1
                else
                  echo "$vendor_licenses_dir" is not a directory.
                  exit 1
                fi
            else
              echo Script should only be executed in build environment indicated by user $build_user
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
              hash_output=$(sha256sum "$line")
              hash=${hash_output:0:66}
              hash_list_len=${#hash_list[@]}
              if [[ $hash_list_len -eq 0 ]]
                then
                  cat "$line" > $vendor_licenses_dir/$filename
                  hash_list[0]=$hash
                  filename_list[0]=$filename
                  real_files=$(($real_files+1))
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
                      cat "$line" > $vendor_licenses_dir/$filename
                      real_files=$(($real_files+1))
                    else
                      cd $vendor_licenses_dir
                      ln -s "${filename_list[$counter]}" "$filename"
                      linked_files=$(($linked_files+1))
                      cd $workingdir
                    fi
                fi
            done < $licenses_file
          echo License files to install: $real_files
          echo License files to link: $linked_files
          all_files=$(find "$vendor_licenses_dir")
          size=0
          for item in $all_files
            do
              file_size=$(stat --format=%s "$item")
              if [[ $file_size -ne 0 ]]
                then
                  size=$(($size+$file_size))
                fi
            done
          size_string=""
          sz=$size
          if [[ $size -gt 10000000 ]]
            then
              sz=$(($size/1000000))
              size_string="Mega"
            else
              if [[ $size -gt 10000 ]]
                then
                  sz=$(($size/1000))
                  size_string="Kilo"
                fi
            fi
          echo Size of licenses to package approximately: $sz $size_string Bytes
        else
          echo Does not package licenses.
          exit 1
        fi
    else
      echo No licenses found to package.
    fi
}


function installer {
  # Installs or links previously found licenses.
  #
  # $1 should be the soure directory, prepared with script "find_licenses.sh"
  # $2 should be the (already created) destination directory
  # $3 set to "verbose" gives more results output

  vendor_licenses_dir=$1
  install_licenses_dir=$2
  verbose=$3
  licenses_files=$(mktemp /tmp/real_license_files_XXXXXXXXXX.txt)
  licenses_links=$(mktemp /tmp/link_license_files_XXXXXXXXXX.txt)
  real_files=0
  linked_files=0

  rm $licenses_files
  rm $licenses_links

  if [[ -z "$vendor_licenses_dir" ]] || [[ -z "$install_licenses_dir" ]]
    then
      echo needed arguments:
      echo 1. Source Directory with vendored licenses
      echo 2. Existing Target Directory to install vendored licenses in
      exit 1
    else
      find -P $vendor_licenses_dir -type f -fprintf $licenses_files "%f\n"
      find -P $vendor_licenses_dir -type l -fprintf $licenses_links "%f %l\n"

      declare -A installers
      declare -A linkers
      while read line
        do
          install -D -m 0644 $vendor_licenses_dir/$line $install_licenses_dir/$line
          real_files=$(($real_files+1))
          installers["$line"]=0
        done < $licenses_files

      cd $install_licenses_dir
      while read line
        do
          combo=($line)
          ln -s ${combo[1]} ${combo[0]}
          linked_files=$(($linked_files+1))
          installers["${combo[1]}"]=$((${installers["${combo[1]}"]}+1))
          linkers["${combo[0]}"]="${combo[1]}"
        done < $licenses_links

      if [[ -n "$verbose" ]]
        then
          if [[ "$verbose" = "verbose" ]]
            then
              max=0
              for item in ${!installers[@]}
                do
                  if [[ ${installers["$item"]} > $max ]]
                    then
                      max=${installers["$item"]}
                    fi
                done
              installers_len=${#installers[@]}
              ct=0
              c=0
              sorted=()
              while [[ $ct -le $max ]] && [[ $c -lt $installers_len ]]
                do
                  for item in ${!installers[@]}
                    do
                      if [[ ${installers["$item"]} -eq $ct ]]
                        then
                          sorted[$c]="$item"
                          c=$(($c+1))
                        fi
                    done
                  ct=$(($ct+1))
                done
              for item in ${sorted[@]}
                do
                  echo installed  "$item" with ${installers["$item"]} Links
                  for i in ${!linkers[@]}
                    do
                      if [[ ${linkers["$i"]} = "$item" ]]
                        then
                          echo linked: "$i"  "->"  "$item"
                        fi
                    done
                done
            fi
        fi
    fi

  echo Number of license files installed: $real_files
  echo Number of license files linked: $linked_files

}


function echo_to_file {
  c=0
  for i in $2
    do
      echo "$i" >> $1
      c=$(($c+1))
    done
  echo $c
}


function main {
  arg1="$1"
  arg2="$2"
  arg3="$3"
  arg4="$4"
  arg5="$5"
  with_disclaimer=""
  for i in $@
    do
      if  [[ "$i" = "--no_disclaimer" ]]
        then
          with_disclaimer=" "
          break
        fi
    done
  if [[ -z "$with_disclaimer" ]]
    then
      echo DISCLAIMER:
      echo No promise is made that any obligation stated in license of
      echo vendored source code or in another way will be met or
      echo fulfilled by using this script!
      echo USE AT YOUR OWN RISK!
      echo
    fi
  runsomething=""
  if [[ -n "$arg1" ]]
    then
      case "$arg1" in
        "finder")
          runsomething="f"
          finder $arg2 $arg3
          ;;
        "installer")
          runsomething="i"
          installer $arg2 $arg3 $arg4
          ;;
        "help")
          runsomething="h"
          helper
        ;;
      esac
    fi
  if [[ -z "$runsomething" ]]
    then
      echo Only commands \'help\', \'finder\' and \'installer\' are valid.
      exit 1
    fi
}

main $@
