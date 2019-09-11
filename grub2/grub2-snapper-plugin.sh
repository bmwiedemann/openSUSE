#!/bin/sh
set -e

# Copyright (C) 2006,2007,2008,2009,2010  Free Software Foundation, Inc.
#
# GRUB is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# GRUB is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with GRUB.  If not, see <http://www.gnu.org/licenses/>.

grub_mkconfig="/usr/sbin/grub2-mkconfig"
grub_mkrelpath="/usr/bin/grub2-mkrelpath"
grub_script_check="/usr/bin/grub2-script-check"
grub_setting="/etc/default/grub"
grub_cfg="/boot/grub2/grub.cfg"
grub_snapshot_cfg="/boot/grub2/snapshot_submenu.cfg"

snapper_snapshot_path="/.snapshots"
snapshot_submenu_name="grub-snapshot.cfg"
snapper_snapshots_cfg="${snapper_snapshot_path}/${snapshot_submenu_name}"

# add hotkeys for s390.  (bnc#885668)
hotkey=
incr_hotkey()
{
  [ -n "$hotkey" ] || return
  expr $hotkey + 1
}
print_hotkey()
{
  keys="123456789abdfgijklmnoprstuvwyz"
  if [ -z "$hotkey" ]||[ $hotkey -eq 0 ]||[ $hotkey -gt 30 ]; then
    return
  fi
  echo "--hotkey=$(expr substr $keys $hotkey 1)"
}


snapshot_submenu () {

  s_dir="$1"

  snapshot="${s_dir}/snapshot"
  num="`basename $s_dir`"
  
  # bnc#864842 Important snapshots are not marked as such in grub2 menu
  # the format is "important distribution version (kernel_version, timestamp, pre/post)"
  date=`xmllint --xpath '/snapshot/date/text()' "${s_dir}/info.xml" || echo ""`
  date=`echo $date | sed 's/\(.*\) \(.*\):.*/\1T\2/'`
  important=`xmllint --xpath "/snapshot/userdata[key='important']/value/text()" "${s_dir}/info.xml" 2>/dev/null || echo ""`
  stype=`xmllint --xpath '/snapshot/type/text()' "${s_dir}/info.xml" || echo ""`
  kernel_ver=`readlink ${snapshot}/boot/vmlinuz | sed -e 's/^vmlinuz-//' -e 's/-default$//'` 
  if [ -z "$kernel_ver" -a -L ${snapshot}/boot/image ]; then
    kernel_ver=`readlink ${snapshot}/boot/image | sed -e 's/^image-//' -e 's/-default$//'`
  fi
  eval `cat ${snapshot}/etc/os-release` 
  # bsc#934252 - Replace SLES 12.1 with SLES12-SP1 for the list of snapshots
  if test "${NAME}" = "SLES" -o "${NAME}" = "SLED"; then
    VERSION=`echo ${VERSION} | sed -e 's!^\([0-9]\{1,\}\)\.\([0-9]\{1,\}\)$!\1-SP\2!'`
  fi

  # FATE#318101
  # Show user defined comments in grub2 menu for snapshots
  # Use userdata tag "bootloader=[user defined text]"
  full_desc=`xmllint --xpath "/snapshot/userdata[key='bootloader']/value/text()" "${s_dir}/info.xml" 2>/dev/null || echo ""`
  test -z "$full_desc" && desc=`xmllint --xpath '/snapshot/description/text()' "${s_dir}/info.xml" 2>/dev/null || echo ""`

  # FATE#317972
  # If we have a post entry and the description field is empty, 
  # we should use the "Pre" number and add that description to the post entry.
  if test -z "$full_desc" -a -z "$desc" -a "$stype" = "post"; then
    pre_num=`xmllint --xpath '/snapshot/pre_num/text()' "${s_dir}/info.xml" 2>/dev/null || echo ""`
    if test -n "$pre_num"; then
      if test -f "${snapper_snapshot_path}/${pre_num}/info.xml" ; then
        desc=`xmllint --xpath '/snapshot/description/text()' "${snapper_snapshot_path}/${pre_num}/info.xml" 2>/dev/null || echo ""`
      fi
    fi 
  fi

  test "$important" = "yes" && important="*" || important=" "
  test "$stype" = "single" && stype=""
  test -z "$stype" || stype=",$stype"
  test -z "$desc" || desc=",$desc"
  test -z "$full_desc" && full_desc="$kernel_ver,$date$stype$desc"

  if test "${NAME}" = "SLES" -o "${NAME}" = "SLED"; then
    title="${important}${NAME}${VERSION} ($full_desc)"
  else
    title="${important}${NAME} ${VERSION} ($full_desc)"
  fi

  if test "$s390" = "1"; then
    subvol="\$2"
  else
    subvol="\$3"
  fi

  cat <<EOF

  if [ -f "${snapper_snapshot_path}/$num/snapshot/boot/grub2/grub.cfg" ]; then
    snapshot_found=true
    saved_subvol=\$btrfs_subvol
    menuentry `print_hotkey` "$title" "${snapper_snapshot_path}/$num/snapshot" "`$grub_mkrelpath ${snapper_snapshot_path}/${num}/snapshot`" {
        btrfs_subvol="$subvol"
        extra_cmdline="rootflags=subvol=\$3"
        export extra_cmdline
        snapshot_num=$num
        export snapshot_num
        configfile "\$2/boot/grub2/grub.cfg"
        btrfs_subvol=\$saved_subvol
      }
  fi

EOF
  hotkey=`incr_hotkey`
  return 0
}

snapper_snapshots_cfg_refresh () {

  if [ ! -d "$snapper_snapshot_path" ]; then
    return
  fi

  cs=
  for s_dir in ${snapper_snapshot_path}/*; do

    snapshot="${s_dir}/snapshot"

    # list only read-only snapshot (bnc#878528)
    if [ ! -d ${s_dir} -o -w "$snapshot" ]; then
        continue
    fi
    if [ -r "${s_dir}/info.xml" -a -r "${s_dir}/snapshot/boot/grub2/grub.cfg" ]; then
      cs="${s_dir}
${cs}"
    else
      # cleanup any grub-snapshot.cfg without associated snapshot info
      snapper_cfg="${s_dir}/${snapshot_submenu_name}"
      if [ -f "$snapper_cfg" ]; then
	rm -f "$snapper_cfg"
	rmdir "$s_dir" 2>/dev/null || true
      fi
      continue
    fi

  done

  hk=""
  [ -z "$hotkey" ] || hk="--hotkey=s"

  for c in $(printf '%s' "${cs}" | sort -Vr); do
    if ! snapshot_submenu "$c" > "${c}/${snapshot_submenu_name}"; then
       rm -f "${c}/${snapshot_submenu_name}"
       continue
    fi
    snapshot_cfg="${snapshot_cfg}
    if [ -f \"$c/${snapshot_submenu_name}\" ]; then
      source \"$c/${snapshot_submenu_name}\"
    fi"
  done

  cat <<EOF >"${snapper_snapshots_cfg}.new"
if [ -z "\$extra_cmdline" ]; then
  submenu $hk "Start bootloader from a read-only snapshot" {${snapshot_cfg}
    if [ x\$snapshot_found != xtrue ]; then
      submenu "Not Found" { true; }
    fi
  }
fi
EOF

  if ${grub_script_check} "${snapper_snapshots_cfg}.new"; then
    mv -f "${snapper_snapshots_cfg}.new" "${snapper_snapshots_cfg}"
  fi

}


snapshot_submenu_clean () {

  for s_dir in ${snapper_snapshot_path}/*; do

    snapper_cfg="${s_dir}/${snapshot_submenu_name}"

    if [ -f "$snapper_cfg" ]; then
      rm -f "$snapper_cfg"
      rmdir "$s_dir" 2>/dev/null || true
    fi

  done

  if [ -f "${snapper_snapshot_path}/${snapshot_submenu_name}" ]; then
    rm -f "${snapper_snapshot_path}/${snapshot_submenu_name}"
  fi

}

set_grub_setting () {

  name=$1
  val=$2

  if grep -q "$name" "$grub_setting"; then
    sed -i -e "s!.*\($name\)=.*!\1=\"$val\"!" "$grub_setting"
  else
    echo "$name=\"$val\"" >> "$grub_setting"
  fi
}

enable_grub_settings () {
  set_grub_setting SUSE_BTRFS_SNAPSHOT_BOOTING "true"
}

disable_grub_settings () {
  set_grub_setting SUSE_BTRFS_SNAPSHOT_BOOTING "false"
}

update_grub () {
   "${grub_mkconfig}" -o "${grub_cfg}"
}

machine=`uname -m`
case "$machine" in
(s390|s390x)
  hotkey=1
  s390=1
  ;;
esac
cmdline="$0 $* hotkey='$hotkey'"

# Check the arguments.
while test $# -gt 0
do
  option=$1
  shift

  case "$option" in
  -e | --enable)
  opt_enable=true
  ;;
  -d | --disable)
  opt_enable=false
  ;;
  -r | --refresh)
  opt_refresh=true
  ;;
  -c | --clean)
  opt_clean=true
  ;;
  -*)
  ;;
  esac
done

if [ "x${opt_enable}" = "xtrue" ]; then
  #enable_grub_settings
  #update_grub
  snapper_snapshots_cfg_refresh
elif [ "x${opt_enable}" = "xfalse" ]; then
  #disable_grub_settings
  update_grub
  snapshot_submenu_clean
fi

if [ x${opt_refresh} = "xtrue" ]; then
  snapper_snapshots_cfg_refresh
fi

if [ x${opt_clean} = "xtrue" ]; then
  snapshot_submenu_clean
fi

