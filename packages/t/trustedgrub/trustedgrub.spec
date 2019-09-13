#
# spec file for package trustedgrub
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           trustedgrub
%ifarch x86_64
BuildRequires:  gcc-32bit
BuildRequires:  glibc-devel-32bit
BuildRequires:  libncurses5-32bit
BuildRequires:  ncurses-devel
BuildRequires:  ncurses-devel-32bit
%endif
BuildRequires:  automake
%if %suse_version >= 1230
BuildRequires:  makeinfo
%endif
Version:        1.1.3
Release:        0
Source0:        TrustedGRUB-%{version}.tgz
Source2:        grubonce
Source3:        grub-install
Patch1:         use_ferror.diff
Patch2:         grub-R
Patch3:         bad-assert-sideeffect
Patch4:         trustedgrub-compile-fixes
Patch5:         reiser-unpack
Patch6:         chainloader-devicefix
Patch7:         grub-%{version}-devicemap.diff
Patch8:         grub-linux-setup-fix
Patch9:         fix-uninitialized
Patch12:        grub-%{version}-initrdaddr.diff
Patch13:        grub-a20.patch
Patch14:        disk-by-ID
Patch16:        recognise-zen
Patch17:        grub-install-fix-UUID_LABEL
Patch18:        ext2-support-256byte-inodes
Patch19:        grub-read-gpt
Patch24:        grub-%{version}-protexec.patch
Patch25:        pacify-autoconf
Patch26:        grub-grubonce-no-wait
Patch27:        grub-long-commandline
Patch29:        grub-acinclude-buildid-fix.diff
Patch30:        remove-buildid.diff
Patch31:        string-ops-fix
Patch32:        trustedgrub-automake.patch
Patch33:        grub-no-pie.patch
Url:            http://trustedgrub.sf.net
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Summary:        Grand Unified Boot Loader with TPM support
License:        GPL-2.0+
Group:          System/Boot
PreReq:         fileutils sh-utils 
Conflicts:      grub
ExclusiveArch:  %ix86 x86_64

%description
GNU GRUB is a multiboot boot loader. It was derived from GRUB. It is an
attempt to produce a boot loader for IBM PC-compatible machines that
has both the ability to be friendly to beginning or otherwise
nontechnically interested users and the flexibility to help experts in
diverse environments. It is compatible with Free/Net/OpenBSD and Linux.
It supports Win 9x/NT and OS/2 via chainloaders. It has a menu
interface and a command line interface.

Trusted GRUB is the continuation of the 1.0 GRUB series, introducing
support for Trusted Platform Modules. This means that it simply records
the configuration of the files used for booting in the TPM for later
verification.



Authors:
--------
    Alessandro Rubini <rubini@gnu.org>
    Chip Salzenberg <chip@valinux.com>
    Edmund GRIMLEY EVANS <edmundo@rano.demon.co.uk>
    Edward Killips <ekillips@triton.net>
    Gordon Matzigkeit <gord@fig.org>
    Jochen Hoenicke <jochen@gnu.org>
    Khimenko Victor <grub@khim.sch57.msk.ru>
    Klaus Reichl <Klaus.Reichl@alcatel.at>
    Michael Hohmuth <hohmuth@innocent.com>
    OKUJI Yoshinori <okuji@gnu.org>
    Pavel Roskin <proski@gnu.org>

%prep
%setup -n TrustedGRUB-%{version}
rm -f acconfig.h || true
# %patch -p1 -E
%patch1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
# %patch10 -p1
# %patch11 -p1
%patch12 -p1
# A20 gate haunts even intel macs. Be extra careful,
# see http://www.win.tue.nl/~aeb/linux/kbd/A20.html
%patch13 -p1
%patch14 -p1
# %patch15 -p1
%patch16 -p1
%patch17 -p1
%patch18 -p1
%patch19 -p1
# %patch18 -p1
# %patch24 -p1
%patch25 -p1
%patch26 -p1
%patch27 -p1
%patch29 -p1
%patch30
%patch31 -p1
%patch32
%patch33 -p1
%build
perl -pi -e 's,/usr/share/grub/i386-pc,/usr/lib/grub,' docs/grub.texi
autoreconf --force --install
%ifarch x86_64
  EXTRACFLAGS=' -fno-PIE -fno-stack-protector -fno-strict-aliasing -minline-all-stringops -m32 -fno-asynchronous-unwind-tables -fno-unwind-tables'
%else
  EXTRACFLAGS=' -fno-PIE -fno-stack-protector -fno-strict-aliasing -minline-all-stringops -fno-asynchronous-unwind-tables -fno-unwind-tables'
%endif
LDFLAGS="-no-pie" CFLAGS="$RPM_OPT_FLAGS -Os -DNDEBUG -W -Wall -Wpointer-arith $EXTRACFLAGS" ./configure \
  --prefix=/usr --infodir=%{_infodir} --mandir=%{_mandir} --datadir=/usr/lib \
  --disable-auto-linux-mem-opt --disable-xfs --disable-ffs --disable-ufs2
make

%install
[ "$RPM_BUILD_ROOT" != "" -a -d $RPM_BUILD_ROOT ] && rm -rf $RPM_BUILD_ROOT;
make -k DESTDIR=$RPM_BUILD_ROOT install 
mkdir -p $RPM_BUILD_ROOT/boot/grub
ln -sfn . $RPM_BUILD_ROOT/boot/boot
(cd $RPM_BUILD_ROOT/usr/lib/grub && mv *-suse/* . && rmdir *-suse) >/dev/null 2>&1 || true
mv $RPM_BUILD_ROOT/usr/sbin/grub-install{,.unsupported}
mv $RPM_BUILD_ROOT/%{_mandir}/man8/grub-install{,.unsupported}.8
cp -p %{SOURCE2} %{SOURCE3} $RPM_BUILD_ROOT/usr/sbin/.
# grub-terminfo is irrelevant to us
rm -f $RPM_BUILD_ROOT/usr/sbin/grub-terminfo
rm -f $RPM_BUILD_ROOT/usr/share/man/man8/grub-terminfo*
# Files contining BSD-licensed code that might get linked with GPL'ed one.
rm -f $RPM_BUILD_ROOT/usr/lib/grub/{ufs2,ffs}_stage1_5

%clean
rm -rf $RPM_BUILD_ROOT;

%preun
%install_info --delete --info-dir=%{_infodir} %{_infodir}/grub.info.gz
%install_info --delete --info-dir=%{_infodir} %{_infodir}/multiboot.info.gz

%files
%defattr(-,root,root)
%doc BUGS NEWS TODO README THANKS AUTHORS ChangeLog COPYING 
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
/usr/lib/grub
%defattr(755,root,root)
/usr/sbin/grub
/usr/sbin/grubonce
/usr/sbin/grub-set-default
/usr/sbin/grub-install
/usr/sbin/grub-install.unsupported
/usr/sbin/grub-md5-crypt
#/usr/sbin/installgrub
/boot/boot

%post
# should anything go wrong the system will remain bootable :
[ -e /boot/grub/stage2 ] && mv /boot/grub/stage2{,.old}
# copy especially stage2 over, because it will be modified in-place !
cp -p /usr/lib/grub/*stage1*   /boot/grub 2>/dev/null || true
cp -p /usr/lib/grub/*/*stage1* /boot/grub 2>/dev/null || true
%install_info --info-dir=%{_infodir} %{_infodir}/grub.info.gz
%install_info --info-dir=%{_infodir} %{_infodir}/multiboot.info.gz
#special hack for #46843
dd if=/usr/lib/grub/stage2 of=/boot/grub/stage2 bs=256k 
sync
# XFS is disabled for new products.
## sync may take much longer on XFS (Bug#223773)
#bootpart=`df /boot/. | perl -ane '$F[0] =~ m,/dev/[^\s]*, && print $F[0]'`
#eval `PATH="$PATH":/lib/udev vol_id $bootpart`
#if [ "X$ID_FS_TYPE" = "X" -o "t_$ID_FS_TYPE" = "t_xfs" ]; then
#	sync; sleep 5; sync; sleep 5; sync
#fi
# Do not try to update/install in the chrooted build environment
[ -e /.buildenv ] && exit 0
# command sequence to update-install stage1/stage2.
# leave everything else alone !
[ -e /etc/grub.conf ] && /usr/sbin/grub --batch < /etc/grub.conf >/var/log/grub-install.log 2>&1 || true
exit 0

%changelog
