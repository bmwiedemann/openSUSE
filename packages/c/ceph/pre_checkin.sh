#!/bin/bash

set -f

function packages_files {
  local spec_file=$1
  local exclude_pkg=$2
  local in_files=false
  local result=""
  
  while IFS='' read -r line || [[ -n "$line" ]]; do
  
    case $line in
    "%files "*)
        pkg=`echo "$line" | sed 's/%files.* \(\w\+\)/\1/g'`
        if [[ $pkg == $exclude_pkg ]]; then
          in_files=false
          continue
        fi
        in_files=true
        continue
        ;;
    "%post"* | "%pre"* | "%preun"* | "%postun"* | "%changelog")
      in_files=false
      continue
      ;;
    esac
    
    result=""
    changed=true
    while [[ $in_files == true ]] && [[ $changed == true ]]; do
      changed=false
      case $line in
      "%if"* | "" | "%defattr"* | "%endif"* | "%else"* | "#"* | "%docdir"*)
        break
        ;;
      "%dir"*)
        break # for now we'll ignore %dir entries
        ;;
      *)
        result=`echo "$line" | sed -e 's/%config \(.*\)/\1/g' \
                                   -e 's/%config(.*) \(.*\)/\1/g' \
                                   -e 's/%attr(.*) \(.*\)/\1/g' \
                                   -e 's/%exclude \(.*\)/\1/g'`
        if [[ ! $line == $result ]]; then
          changed=true
        	line=$result
  	continue
        fi
        ;;
      esac
      
      echo "$result"
    done
  done < $spec_file
}

function get_package_summary {
  local spec_file=$1
  local pkg_name=$2
  local in_package=false
  
  while IFS='' read -r line || [[ -n "$line" ]]; do
  
    case $line in
    "%package "*)
      pkg=`echo "$line" | sed 's/%package.* \(\w\+\)/\1/g'`
      if [[ ! $pkg == $pkg_name ]]; then
        in_package=false
      else
        in_package=true
      fi
      ;;
    "%prep"* | "%build"* | "%install"*)
      in_package=false
      ;;
    "Summary:"*)
      if [[ $in_package == true ]]; then
        echo $line
        break
      fi
      ;;
    esac
  done < $spec_file
}

function get_package_requires {
  local spec_file=$1
  local pkg_name=$2
  local in_package=false
  
  while IFS='' read -r line || [[ -n "$line" ]]; do
  
    case $line in
    "%package "*)
      pkg=`echo "$line" | sed 's/%package.* \(\w\+\)/\1/g'`
      if [[ ! $pkg == $pkg_name ]]; then
        in_package=false
      else
        in_package=true
      fi
      ;;
    "%prep"* | "%build"* | "%install"*)
      in_package=false
      ;;
    "Requires:"*)
      if [[ $in_package == true ]]; then
        echo $line
      fi
      ;;
    esac
  done < $spec_file
}

function get_package_description {
  local spec_file=$1
  local pkg_name=$2
  local in_desc=false
  
  while IFS='' read -r line || [[ -n "$line" ]]; do
  
    case $line in
    "%description "*)
      pkg=`echo "$line" | sed 's/%description.* \(\w\+\)/\1/g'`
      if [[ ! $pkg == $pkg_name ]]; then
        in_desc=false
      else
        in_desc=true
      fi
      continue
      ;;
    "%prep"* | "%build"* | "%install"* | "%package"* | "%if"* | "%endif"*)
      in_desc=false
      continue
      ;;
    esac
   
    if [[ $in_desc == true ]]; then
      echo "$line"
    fi
  done < $spec_file
}

function transform_spec_file {
  local spec_file=$1
  local include_pkg=$2
  local rm_files=$3
  local summary=$4
  local description=$5
  local requires=$6
  local in_package=false
  local in_files=false
  local in_desc=false
  
  while IFS='' read -r line || [[ -n "$line" ]]; do
  
    case $line in
    "%bcond_with ceph_test_package"*)
      line="%bcond_without ceph_test_package"
      ;;
    "Name:"*)
      line="Name:           $include_pkg"
      ;;
    "Summary:"*)
      if [[ $in_package == false ]]; then
        line="$summary"
      fi
      ;;
    "Source0:"*)
      line=`echo $line | sed 's/%{name}/ceph/g'`
      ;;
    "ExclusiveArch:"*)
      line="ExclusiveArch: x86_64"
      ;;
    "%autosetup -p1")
      line="%autosetup -p1 -n ceph-%version"
      ;;
    "Requires:"*)
      if [[ $in_package == false ]]; then
        line=""
      fi
      ;;
    "Requires(post):"*)
      if [[ $in_package == false ]]; then
        IFS=''
        for r in "$requires"; do
          echo "$r"
        done
      fi
      ;;
    "%description"*)
      if [[ $in_package == false ]]; then
        in_desc=true
        echo "$line"
        echo "$description"
        echo ""
        continue
      fi
      ;;
    "%package "*)
        in_package=true
        continue
        ;;
    "%prep"* | "%build"* | "%install"*)
      in_package=false
      in_desc=false
      ;;
    "%files "*)
        pkg=`echo "$line" | sed 's/%files.* \(\w\+\)/\1/g'`
        if [[ $pkg == $include_pkg ]]; then
          in_files=false
        else
          in_files=true
          continue
        fi
        ;;
    "%changelog"*)
      in_files=false
      ;;
    "%clean"*)
      in_package=false
      IFS=''
      for rf in "$rm_files"; do
        echo "$rf"
      done
      echo ""
      echo "dirs=\`find %{buildroot} -type d -empty\`"
      echo "while [[ -n \$dirs ]]; do"
      echo "  for d in \$dirs; do"
      echo "    rm -rf \$d"
      echo "  done"
      echo "dirs=\`find %{buildroot} -type d -empty\`"
      echo "done"
      echo ""
      ;;
    "#"* | "%"*)
      in_desc=false
      ;;
    esac

  if [[ $in_package == false ]] && [[ $in_files == false ]] && [[ $in_desc == false ]]; then
    echo $line
  else
    if [[ $line == "%if"* ]] || [[ $line == "%endif"* ]]; then
      echo $line
    fi
  fi

  done < $spec_file
}

function generate_rm_exclude_files {
  local exclude_list=$1
  local buildroot=$2

  for f in $exclude_list; do
    echo "rm -rf $buildroot$f"
  done
}

function insert_line_before {
  local FILE=$1
  local line_to_insert=$2
  local match_regex=$3
  sed -i "/${match_regex}/i $line_to_insert" $FILE
}

function copy_changes_file {
  local dest_pkg=$1

  cp ceph.changes ${dest_pkg}.changes
}

PACKAGE="ceph-test"
SPEC_FILE="ceph.spec"

files=`packages_files $SPEC_FILE $PACKAGE`
if [[ "$?" == "1" ]]; then
 echo "ERROR: "
 echo $files
 exit 0
fi
rm_files=`generate_rm_exclude_files "$files" "%{buildroot}"`
summ=`get_package_summary $SPEC_FILE $PACKAGE`
desc=`get_package_description $SPEC_FILE $PACKAGE`
reqs=`get_package_requires $SPEC_FILE $PACKAGE`
transform_spec_file $SPEC_FILE $PACKAGE "$rm_files" "$summ" "$desc" "$reqs" > $PACKAGE.spec
insert_line_before "${PACKAGE}.spec" "Source99: ceph-rpmlintrc" "_insert_obs_source_lines_here"
insert_line_before "${PACKAGE}.spec" "Source98: README-ceph-test.txt" "^Source99:"
insert_line_before "${PACKAGE}.spec" "Source97: README-checkin.txt" "^Source98:"
insert_line_before "${PACKAGE}.spec" "Source96: checkin.sh" "^Source97:"
copy_changes_file $PACKAGE
