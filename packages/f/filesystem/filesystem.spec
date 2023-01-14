#
# spec file for package filesystem
#
# Copyright (c) 2023 SUSE LLC
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


%define nvr %{name}-%{version}-%{release}

Name:           filesystem
Summary:        Basic Directory Layout
License:        MIT
Group:          System/Fhs
%if 0%{?sle_version}
Version:        %(echo %suse_version | cut -b-2).%(echo %suse_version | cut -b3)
Release:        0
%else
Version:        84.87
Release:        0
%endif
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
# XXX libsolv never sees the rpmlib provides fulfilled
Requires(pre):  (compat-usrmerge-tools or rpmlib(X-CheckUnifiedSystemdir))
Requires:       group(root)
Requires:       user(root)
URL:            https://build.opensuse.org/package/show/openSUSE:Factory/filesystem
Source0:        directory.list
Source1:        filesystem.links
Source2:        languages
Source3:        ghost.list
Source4:        languages.man
Source64:       directory.list64
Source65:       directory.list64-x86_64
Source66:       ghost.list64
Source99:       LICENSE.txt

%description
This package installs the basic directory structure. It also includes
the home directories of system users.

%prep
%setup -c -n filesystem -T
cp %{SOURCE0} .
cp %{SOURCE1} .
cp %{SOURCE3} .
%ifarch s390x %sparc x86_64 %x86_64 ppc64 ppc aarch64 ppc64le riscv64
cat %{SOURCE66} >> ghost.list
%endif

%build
cat > pretrans.lua <<'EOF'
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

local ghosts = {
EOF
#
while read MOD OWN GRP NAME ; do
	[ "$OWN" = root -a "$GRP" = root ]
	echo "[\"$NAME\"] = $MOD,"
done < ghost.list >> pretrans.lua
cat >> pretrans.lua <<'EOF'
}
function mkdir_p(path)
    d = ''
    for p in string.gmatch(path, "([^/]+)") do
	d = d.."/"..p
	posix.mkdir(d)
    end
end
for i in pairs(ghosts) do
  mkdir_p(i)
  posix.chmod(i, ghosts[i])
end
EOF
#
#
cat > pre.lua <<'EOF'
needmigrate = false
local dirs = {"/bin",
  "/sbin",
%ifarch s390x %sparc x86_64 %x86_64 ppc64 ppc aarch64 ppc64le riscv64
  "/lib64",
%endif
  "/lib" }
for i in pairs(dirs) do
  local t = posix.stat(dirs[i], "type")
  if t == nil then
    posix.symlink("usr"..dirs[i], dirs[i])
  elseif t == "directory" then
    needmigrate = true
  end
end
if needmigrate then
  if posix.getenv("ZYPP_SINGLE_RPMTRANS") == "1" then
    print("Warning: UsrMerge executed in single transcation mode")
    if not posix.stat("/usr/lib/rpm/lua/usrmerge.lua") then
      error("ERROR: compat-usrmerge file triggers not installed.\n!!! This will go horribly wrong. You need a rescue system now !!!")
    end
    rpm.define("_filesystem_need_posttrans_convertfs 1")
  else
    assert(os.execute("/usr/libexec/convertfs"))
  end
end
EOF

cat > posttrans.lua <<'EOF'
if rpm.expand("%%%%{?_filesystem_need_posttrans_convertfs}") == "1" then
  assert(os.execute("/usr/libexec/convertfs"))
end
EOF

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
    test -w $RPM_BUILD_ROOT$BDIR || chmod u+w $RPM_BUILD_ROOT$BDIR
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
	/usr/local/*)
	    echo "d $NAME $MODE $OWNR $GRUP -" >> fs-usr-local.conf
	    ;;
    esac
}
mkdir -p $RPM_BUILD_ROOT
# generic directories first
echo "%%defattr(-,root,root)" > filesystem.list
%ifarch s390x %sparc x86_64 %x86_64 ppc64 ppc aarch64 ppc64le riscv64
cat %{SOURCE64} >> directory.list
%endif
%ifarch x86_64 %x86_64
cat %{SOURCE65} >> directory.list
%endif
cat >> filesystem.links << EOF
usr/bin   /bin
usr/sbin  /sbin
usr/lib   /lib
%ifarch s390x %sparc x86_64 %x86_64 ppc64 ppc aarch64 ppc64le riscv64
usr/lib64 /lib64
%endif
EOF
cat >> directory.list <<EOF
0755 root root /usr/lib/modules
0755 root root %{_firmwaredir}
EOF
while read MOD OWN GRP NAME ; do
    create_dir $MOD $OWN $GRP $NAME
done < directory.list
# ghost files next
while read MOD OWN GRP NAME ; do
    create_dir $MOD $OWN $GRP $NAME "%%ghost "
done < ghost.list
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
while read SRC DEST ATTR ; do
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
	*) echo "$ATTR${ATTR:+ }$DEST" >> filesystem.list ;;
    esac
    # for tmpfiles.d
    case  $DEST in
	/var/*) echo "L $DEST - - - - $SRC" >> fs-var.conf ;;
    esac
    ;;
esac
done < filesystem.links
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
install -m 0644  fs-usr-local.conf $RPM_BUILD_ROOT/usr/lib/tmpfiles.d/fs-usr-local.conf

%pretrans -p <lua> -f pretrans.lua
%pre -p <lua> -f pre.lua

%posttrans -p <lua> -f posttrans.lua

%files -f filesystem.list
/usr/lib/tmpfiles.d/fs-tmp.conf
/usr/lib/tmpfiles.d/fs-var.conf
/usr/lib/tmpfiles.d/fs-var-tmp.conf
/usr/lib/tmpfiles.d/fs-usr-local.conf

%changelog
