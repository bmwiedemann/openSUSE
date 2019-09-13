#
# spec file for package grub
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           grub
BuildRequires:  automake
%ifarch x86_64
BuildRequires:  gcc-32bit
BuildRequires:  glibc-devel-32bit
%if 0%sles_version
%else
BuildRequires:  glibc-devel-static-32bit
%endif
BuildRequires:  libncurses5-32bit
BuildRequires:  ncurses-devel-32bit
%else
BuildRequires:  glibc-devel
%if 0%sles_version
%else
BuildRequires:  glibc-devel-static
%endif
BuildRequires:  libncurses5
BuildRequires:  ncurses-devel
%endif
%if %suse_version >= 1230
BuildRequires:  makeinfo
%endif
Version:        0.97
Release:        0
Source0:        ftp://alpha.gnu.org/gnu/%{name}/%{name}-%{version}.tar.gz
Source1:        installgrub
Source2:        grubonce
Source3:        grub-install
Patch0:         %{name}-%{version}-path-patch
Patch1:         use_ferror.diff
Patch2:         grub-R
Patch3:         bad-assert-sideeffect
Patch4:         %{name}-gfxmenu-v8.diff
Patch5:         reiser-unpack
Patch6:         chainloader-devicefix
Patch7:         %{name}-%{version}-devicemap.diff
Patch8:         grub-linux-setup-fix
Patch9:         fix-uninitialized
Patch10:        force-LBA-off.diff
Patch11:        gcc4-diff
Patch12:        %{name}-%{version}-initrdaddr.diff
Patch13:        grub-a20.patch
Patch14:        disk-by-ID
Patch15:        e100-newIDs
Patch16:        add-e2fs-slice-types
Patch17:        grub-install-fix-UUID_LABEL
Patch18:        ext2-support-256byte-inodes
Patch19:        grub-read-gpt
Patch24:        grub-%{version}-protexec.patch
Patch25:        pacify-autoconf
Patch26:        grub-grubonce-no-wait
Patch27:        grub-long-commandline
Patch28:        ext4-support
Patch29:        grub-acinclude-buildid-fix.diff
Patch30:        remove-buildid.diff
Patch31:        string-ops-fix
Patch32:        unsigned-blocks-n-offsets
Patch39:        document-grub-install.unsupported
Patch40:        grub-iso-fixes
Patch41:        stage2-gfx-cmdline-len-fix.diff
Patch42:        nulterminate-configfile
Patch43:        handle-incomplete-last-track
Patch44:        no-MAP_GROWSDOWN
Patch45:        grub-automake.patch
Patch46:        grub-bigraid-failsafe
Patch47:        grub-configure-check-libncurses
Patch48:        grub-password-sha2-crypt
Patch49:        illumos-zfs-grub-fix-for-dell-bios
Url:            http://www.gnu.org/software/grub/grub.en.html
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Summary:        Grand Unified Boot Loader
License:        GPL-2.0+
Group:          System/Boot
PreReq:         fileutils sh-utils util-linux
Conflicts:      trustedgrub
ExclusiveArch:  %ix86 x86_64

%description
GNU GRUB is a multiboot boot loader. It was derived from GRUB. It is an
attempt to produce a boot loader for IBM PC-compatible machines that
has both the ability to be friendly to beginning or otherwise
nontechnically interested users and the flexibility to help experts in
diverse environments. It is compatible with Free/Net/OpenBSD and Linux.
It supports Win 9x/NT and OS/2 via chainloaders. It has a menu
interface and a command line interface.

%prep
%setup
rm -f acconfig.h || true
%patch0 -p1 -E
%patch1
%patch2 -p1
%patch3 -p1
%patch4
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1
# A20 gate haunts even intel macs. Be extra careful,
# see http://www.win.tue.nl/~aeb/linux/kbd/A20.html
%patch13 -p1
%patch14 -p1
%patch15 -p1
%patch16 -p1
%patch17 -p1
%patch18 -p1
%patch19 -p1
%patch24 -p1
%patch25 -p1
%patch26 -p1
%patch27 -p1
%patch28 -p1
%patch29 -p1
%patch30
%patch31 -p1
%patch32 -p1
%patch39 -p1
%patch40 -p1
%patch41 -p1
%patch42 -p1
%patch43 -p1
%patch44 -p1
%patch45 -p1
%patch46 -p1
%patch47 -p1
%patch48 -p1
%patch49 -p5

%build
perl -pi -e 's,/usr/share/grub/i386-pc,/usr/lib/grub,' docs/grub.texi
%{?suse_update_config:%{suse_update_config -l -f . }}
autoreconf --force --install
EXTRACFLAGS=' -fno-reorder-functions -fno-stack-protector -fno-strict-aliasing -minline-all-stringops -fno-asynchronous-unwind-tables -fno-unwind-tables -static'
# RPM_OPT_FLAGS considered harmful
CFLAGS="-m32 -Os -g -DNDEBUG -W -Wall -Wpointer-arith $EXTRACFLAGS" ./configure \
  --prefix=/usr --infodir=%{_infodir} --mandir=%{_mandir} --datadir=/usr/lib \
  --disable-auto-linux-mem-opt --disable-ffs --disable-ufs2
export CFLAGS
make %_smp_mflags

%install
make -k DESTDIR=$RPM_BUILD_ROOT install 
mkdir -p $RPM_BUILD_ROOT/boot/grub
ln -sfn . $RPM_BUILD_ROOT/boot/boot
(cd $RPM_BUILD_ROOT/usr/lib/grub && mv *-suse/* . && rmdir *-suse) >/dev/null 2>&1 || true
mv $RPM_BUILD_ROOT/usr/sbin/grub-install{,.unsupported}
mv $RPM_BUILD_ROOT/%{_mandir}/man8/grub-install{,.unsupported}.8
install -p -m 755 %{SOURCE2} %{SOURCE3} $RPM_BUILD_ROOT/usr/sbin/.
# This fine script used to do everything at once, which
# isn't necessary any more with Yast2 support.
# Kept only for reference and historical reasons.
# install -o root -g root -m 744 %{SOURCE1} /usr/sbin
# grub-terminfo is irrelevant to us
rm -f $RPM_BUILD_ROOT/usr/sbin/grub-terminfo
rm -f $RPM_BUILD_ROOT/usr/share/man/man8/grub-terminfo*
rm -f $RPM_BUILD_ROOT/usr/sbin/grub-set-default

%clean
rm -rf $RPM_BUILD_ROOT;

%preun
%install_info --delete --info-dir=%{_infodir} %{_infodir}/%{name}.info.gz
%install_info --delete --info-dir=%{_infodir} %{_infodir}/multiboot.info.gz

%files
%defattr(-,root,root)
%doc BUGS NEWS TODO README THANKS AUTHORS INSTALL ChangeLog COPYING 
%docdir %{_infodir}
%docdir %{_mandir}
%docdir /usr/share/doc/packages/grub
%dir /boot/grub
/usr/bin/mbchk
%{_infodir}/grub*.gz
%{_infodir}/multiboot.info.gz
%{_mandir}/man1/mbchk.1.gz
%{_mandir}/man8/grub-install.unsupported.8.gz
%{_mandir}/man8/grub.8.gz
%{_mandir}/man8/grub-md5-crypt.8.gz
%{_mandir}/man8/grub-crypt.8.gz
/usr/lib/grub
%defattr(755,root,root)
/usr/sbin/grub
/usr/sbin/grubonce
/usr/sbin/grub-install
/usr/sbin/grub-install.unsupported
/usr/sbin/grub-md5-crypt
/usr/sbin/grub-crypt
#/usr/sbin/installgrub
/boot/boot

%post
%install_info --info-dir=%{_infodir} %{_infodir}/%{name}.info.gz
%install_info --info-dir=%{_infodir} %{_infodir}/multiboot.info.gz

# bnc#863293: make kiwi happy
# copy especially stage2 over, because it will be modified in-place !
cp -p /usr/lib/grub/*stage1* /boot/grub/. 2>/dev/null || true
# Avoid fragmentation on reiserfs.
dd if=/usr/lib/grub/stage2 of=/boot/grub/stage2.new bs=256k 2>/dev/null
# should anything go wrong the system will remain bootable :
mv --backup=simple --suffix=.old /boot/grub/stage2{.new,}

if [ -e /etc/sysconfig/bootloader ] ; then
    source /etc/sysconfig/bootloader
else
    if test "$YAST_IS_RUNNING" != "instsys"; then
	echo "grub postinstall: no /etc/sysconfig/bootloader"
    fi
    exit 0
fi

# bnc#682337
if [ "x$LOADER_TYPE" != "xgrub" -o ! -r /etc/grub.conf ] ; then
    echo "grub postinstall: grub is not the active boot loader"
    exit 0
fi
if [ -x /bin/fsync ]; then
    fsync /boot/grub/stage2
    fsync /boot/grub
    fsync /boot
    fsync /
else
    sync
fi
# sync may take much longer on XFS (Bug#223773)
if test "$YAST_IS_RUNNING" != "instsys"; then
    bootpart=`df /boot/. 2>/dev/null | perl -ane '$F[0] =~ m,/dev/[^\s]*, && print $F[0]'`
    eval `/sbin/blkid -u filesystem -o udev $bootpart`
    XFS_FREEZE=`type -p xfs_freeze` || true
    if [ -n "$XFS_FREEZE" ] ; then
      if [ "t_$ID_FS_TYPE" = "t_xfs" ]; then
            sync; sleep 5; sync;
	    # bnc#805732
            (xfs_freeze -f /; xfs_freeze -f /boot; \
		xfs_freeze -u /; xfs_freeze -u /boot ) > /dev/null 2>&1
      fi
    fi
fi

# command sequence to update-install stage1/stage2.
# leave everything else alone !
/usr/sbin/grub --batch < /etc/grub.conf >/dev/null 2>&1

exit 0

%changelog
