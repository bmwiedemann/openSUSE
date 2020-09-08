#
# spec file for package filesystem
#
# Copyright (c) 2020 SUSE LLC
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


Name:           filesystem
Summary:        Basic Directory Layout
License:        MIT
Group:          System/Fhs
Version:        %(echo %suse_version | cut -b-2).%(echo %suse_version | cut -b3)
Release:        0
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Requires:       group(root)
Requires:       user(root)
URL:            https://build.opensuse.org/package/show/openSUSE:Factory/filesystem
Source0:        directory.list
Source1:        filesystem.links
Source2:        languages
Source3:        ghost.list
Source4:        languages.man
Source64:       directory.list64
Source99:       LICENSE.txt

%description
This package installs the basic directory structure. It also includes
the home directories of system users.

%prep
%setup -c -n filesystem -T

%build

%install
function create_dir () {
    local MODE=$1
    case "$MODE" in
	 \#*) return ;;
    esac
    local OWNR=$2
    local GRUP=$3
    local NAME=$4
    local XTRA=$5
    local BDIR=`dirname $NAME`
    test -d "$RPM_BUILD_ROOT/$NAME" && { echo "dir $NAME does already exist" ; echo "input out of sequence ?" ; exit 1 ; }
    test -n "$BDIR" -a ! -d $RPM_BUILD_ROOT$BDIR && create_dir 0755 root root $BDIR
    mkdir -m $MODE $RPM_BUILD_ROOT/$NAME
    echo "$XTRA%%dir %%attr($MODE,$OWNR,$GRUP) $NAME" >> filesystem.list
    case "$NAME" in
        /tmp)
            echo "q $NAME $MODE $OWNR $GRUP 10d" >> fs-tmp.conf
            ;;
        /var/tmp)
            echo "d $NAME $MODE $OWNR $GRUP -" >> fs-var-tmp.conf
            ;;
	/var/*)
	    echo "d $NAME $MODE $OWNR $GRUP -" >> fs-var.conf
	    ;;
    esac
}
mkdir -p $RPM_BUILD_ROOT
# generic directories first
echo "%%defattr(-,root,root)" > filesystem.list
{
    cat %{SOURCE0}
%ifarch s390x %sparc x86_64 ppc64 ppc aarch64 ppc64le riscv64
    cat %{SOURCE64}
%endif
} | while read MOD OWN GRP NAME ; do
    create_dir $MOD $OWN $GRP $NAME
done
# ghost files next
cat %{SOURCE3} | while read MOD OWN GRP NAME ; do
%ifarch s390 s390x
    case $NAME in
	/media/floppy|/media/cdrom) continue ;;
    esac
%endif
    create_dir $MOD $OWN $GRP $NAME "%%verify(not mode) %%ghost "
done
# arch specific leftovers
for march in \
%ifarch %ix86
i586-suse-linux \
%else
%ifarch %sparc
sparc-suse-linux sparc64-suse-linux \
%else
%ifarch ppc
powerpc-suse-linux \
%else
%ifarch ppc64
powerpc64-suse-linux \
%else
%ifarch ppc64le
powerpc64le-suse-linux \
%else
%ifarch %arm
%{_target_cpu}-suse-linux-gnueabi \
%else
%{_target_cpu}-suse-linux \
%endif
%endif
%endif
%endif
%endif
%endif
  ; do
  create_dir 0755 root root /usr/$march
  for xdir in bin include lib ; do
    create_dir 0755 root root /usr/$march/$xdir
  done
done
%ifarch ia64
create_dir 0755 root root /emul/ia32-linux
%endif
# now do the links
while read SRC DEST ; do
case $SRC in
 "") continue ;;
 \#*) echo "comment: $SRC $DEST" ;;
 *)
    case $SRC in
	/*) test -d $RPM_BUILD_ROOT/$SRC || { echo "link src does not exist" ; exit 1 ; }
	    ;;
	*)  test -d $RPM_BUILD_ROOT/`dirname $DEST`/$SRC || { echo "link src does not exist" ; exit 1 ; }
	    ;;
    esac
    ln -sf $SRC $RPM_BUILD_ROOT$DEST
    case $DEST in
	/var/run|/var/lock) echo "%ghost $DEST" >> filesystem.list ;;
	*) echo "$DEST" >> filesystem.list ;;
    esac
    # for tmpfiles.d
    case  $DEST in
	/var/*) echo "L $DEST - - - - $SRC" >> fs-var.conf ;;
    esac
    ;;
esac
done < %{SOURCE1}
# Create the locale directories:
while read LANG ; do
  create_dir 0755 root root /usr/share/locale/$LANG/LC_MESSAGES
  create_dir 0755 root root /usr/share/help/$LANG
done < %{SOURCE2}
# Create the locale directories for man:
while read LANG ; do
  create_dir 0755 root root /usr/share/man/$LANG
  for sec in 1 2 3 4 5 6 7 8 9 n; do
    create_dir 0755 root root /usr/share/man/$LANG/man$sec
  done
done < %{SOURCE4}

RPM_INSTALL_PREFIX=$RPM_BUILD_ROOT
export RPM_BUILD_ROOT
# check, if all home directories are present.
UNFOUND=false
UNFOUND_DIRS=
OLDIFS="$IFS"
IFS=":"
while read LOGIN PASSWD UID_T GID_T NAME HOME_DIR SHELL_T ; do
    test "$LOGIN" = "abuild" && continue
    test "$LOGIN" = "icecream" && continue
    test "$LOGIN" = "vscan" && continue
    test -n "$HOME_DIR" || continue
    test "$UID_T" -gt 100 && continue
    test -d $RPM_BUILD_ROOT/$HOME_DIR && continue
    echo $HOME_DIR does not exist.
    UNFOUND=true
    UNFOUND_DIRS="$UNFOUND_DIRS $HOME_DIR"
done < /etc/passwd
IFS=$OLDIFS
if test "$UNFOUND" = true ; then
    echo There are home directories defined, which are not present.
    echo Unfound: $UNFOUND_DIRS
    exit 1
fi
#
# now check, if all files of aaa_base have a directory in this package
#
NON_EXISTING_DIR=
for FILE in `rpm -ql aaa_base` ; do
    test -d $FILE && continue
    case $FILE in
      /etc/init.d/*.local|/usr/share/doc/support/*|/lib/mkinitrd/scripts/*)
             continue
             ;;
      /usr/share/doc/packages/aaa_base/*|/usr/share/licenses/aaa_base/*|/lib/aaa_base/*|/usr/lib/base-scripts/*)
             continue
             ;;
    esac
    test -d $RPM_BUILD_ROOT/`dirname $FILE` || {
        echo `dirname $FILE` for $FILE is not in filesystem.
        NON_EXISTING_DIR="$NON_EXISTING_DIR `dirname $FILE`"
    }
done
test -n "$NON_EXISTING_DIR" && {
    echo NON_EXISTING_DIR=$NON_EXISTING_DIR
    exit 1
}
install -m 0644  fs-tmp.conf $RPM_BUILD_ROOT/usr/lib/tmpfiles.d/fs-tmp.conf
install -m 0644  fs-var.conf $RPM_BUILD_ROOT/usr/lib/tmpfiles.d/fs-var.conf
install -m 0644  fs-var-tmp.conf $RPM_BUILD_ROOT/usr/lib/tmpfiles.d/fs-var-tmp.conf

%pretrans -p <lua>
os.remove ("/usr/include/X11")
os.remove ("/usr/lib/X11")
if not posix.readlink("/var/run") then
   os.rename("/var/run","/var/run.rpmsave.tmpx")
end
if not posix.readlink("/var/lock") then
   os.rename("/var/lock","/var/lock.rpmsave.tmpx")
end
if not posix.stat("/var/run") then
  posix.symlink("/run","/var/run")
end
if not posix.stat("/var/lock") then
  posix.symlink("/run/lock","/var/lock")
end
if posix.stat("/var/run.rpmsave.tmpx") then
  os.execute("mv /var/run.rpmsave.tmpx/* /var/run")
  os.remove("/var/run.rpmsave.tmpx")
end
if posix.stat("/var/lock.rpmsave.tmpx") then
  os.execute("mv /var/lock.rpmsave.tmpx/* /var/lock")
  os.remove("/var/lock.rpmsave.tmpx")
end

%files -f filesystem.list
/usr/lib/tmpfiles.d/fs-tmp.conf
/usr/lib/tmpfiles.d/fs-var.conf
/usr/lib/tmpfiles.d/fs-var-tmp.conf

%changelog
