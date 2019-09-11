#
# spec file for package lilo
#
# Copyright (c) 2016 SUSE LINUX GmbH, Nuernberg, Germany.
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


Url:            https://github.com/openSUSE/lilo

Name:           lilo
ExclusiveArch:  ppc ppc64 %ix86 x86_64
%define yaboot_vers 24.2-150408.027659a
Summary:        The Linux Loader, a Boot Menu
License:        BSD-3-Clause
Group:          System/Boot
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Obsoletes:      quik
Obsoletes:      yaboot
%ifarch ppc ppc64
%if 0%{?suse_version} > 1020
BuildRequires:  dtc
%endif
Requires:       coreutils
Requires:       dosfstools
Requires:       gawk
Requires:       hfsutils
Requires:       sed
# for relinking the prep/chrp images in lilo
%ifarch ppc
Requires:       gcc
%endif
%ifarch ppc64
Requires:       gcc-32bit
%endif
# for nvram
%if 0%{?suse_version} > 1000
Requires:       powerpc-utils >= 1.2.6
%else
Requires:       util-linux
%endif
Requires:       binutils
Requires:       parted
%endif
%ifarch %ix86 x86_64
BuildRequires:  bin86
BuildRequires:  nasm
%endif
%ifarch %ix86
BuildRequires:  device-mapper
BuildRequires:  device-mapper-devel
%endif
%ifarch x86_64
# device-mapper-32bit was dropped in Tumbleweed in favor of SLPP
# a direct build dep is wrong: it is the -devel packages responsibility
# to pull in the depending libraries
%if 0%{?suse_version} < 1330
BuildRequires:  device-mapper-32bit
%else
BuildRequires:  device-mapper-devel-32bit
%endif
BuildRequires:  gcc-32bit
BuildRequires:  glibc-devel-32bit
%endif
%ifarch ppc64
BuildRequires:  gcc-32bit
%endif
Version:        24.2
Release:        0
Source0:        lilo-ppc-%{version}.tar.xz
Source1:        yaboot-%{yaboot_vers}.tar.xz
Source86:       lilo-%{version}.tar.gz
Patch8601:      lilo.x86.mount_by_persistent_name.patch
Patch8602:      lilo.x86.array-bounds.patch
Patch8604:      lilo.x86.checkit.patch
Patch8610:      lilo.src.Makefile.patch

%description
LILO boots Linux from your hard drive. It can also boot other operating
systems, such as MS-DOS and OS/2, and can even boot DOS from the second
hard drive. The configuration file is /etc/lilo.conf.

The PowerPC variant can be used on new PowerMacs and CHRP machines.

The ix86 variant comes with Memtest86, offering an image that can be
booted to perform a memory test.

%prep
%setup -q -T -c -a 0 -a 1 -a 86
mv lilo-ppc-%{version} lilo.ppc
mv yaboot-%{yaboot_vers} yaboot
pushd lilo-%{version}
%patch8601 -p1
%patch8602 -p1
%patch8604 -p1
%patch8610 -p1
popd

%build
%ifarch %ix86 x86_64
pushd lilo-%{version}
cflags="$RPM_OPT_FLAGS -fno-strict-aliasing -DLCF_DEVMAPPER"
%ifarch x86_64
cflags="$cflags -m32"
%endif
make CC="gcc $cflags" MAN_DIR=/usr/share/man all 
popd
# powerpc
%else
pushd yaboot
#
make clean
make DEBUG=1 VERSION=%{yaboot_vers}.SuSE yaboot HOSTCFLAGS="$RPM_OPT_FLAGS -U_FORTIFY_SOURCE -g"
mv second/yaboot yaboot.debug
mv second/yaboot.chrp yaboot.chrp.debug
#
make clean
make DEBUG=0 VERSION=%{yaboot_vers}.SuSE yaboot HOSTCFLAGS="$RPM_OPT_FLAGS -U_FORTIFY_SOURCE -g"
mv second/yaboot yaboot
mv second/yaboot.chrp yaboot.chrp
mv second/yaboot.a second/crt0.o .
#
popd
#
pushd lilo.ppc
pushd bootheader
make HOST_CFLAGS="$RPM_OPT_FLAGS -U_FORTIFY_SOURCE -g"
popd
popd
%endif

%install
%ifarch %ix86 x86_64
pushd lilo-%{version}
make MAN_DIR=/usr/share/man install DESTDIR=$RPM_BUILD_ROOT
rm -rfv $RPM_BUILD_ROOT/boot
mkdir -p $RPM_BUILD_ROOT/boot
cp -av src/*.b $RPM_BUILD_ROOT/boot
popd
%else
# powerpc
# get rid of /usr/lib/rpm/brp-strip-debug 
# it kills the zImage.chrp-rs6k 
export NO_BRP_STRIP_DEBUG=true
# do not strip binaries, keep debug info
export NO_DEBUGINFO_STRIP_DEBUG=true
#
mkdir -p $RPM_BUILD_ROOT/lib/lilo/pmac
mkdir -p $RPM_BUILD_ROOT/lib/lilo/chrp
mkdir -p $RPM_BUILD_ROOT/sbin
mkdir -p $RPM_BUILD_ROOT/bin
mkdir -p $RPM_BUILD_ROOT/bin
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man8
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man5
mkdir -p $RPM_BUILD_ROOT%{_docdir}/lilo
pushd lilo.ppc
cp -av lilo.new $RPM_BUILD_ROOT/sbin/lilo
cp -av lilo-pmac.lib $RPM_BUILD_ROOT/lib/lilo/lilo-pmac.lib
cp -av lilo-chrp.lib $RPM_BUILD_ROOT/lib/lilo/lilo-chrp.lib
cp -av lilo-iseries.lib $RPM_BUILD_ROOT/lib/lilo/lilo-iseries.lib
cp -av show_of_path.sh $RPM_BUILD_ROOT/bin
cp -av Finder.bin $RPM_BUILD_ROOT/lib/lilo/pmac
cp -av System.bin $RPM_BUILD_ROOT/lib/lilo/pmac
cp -av os-badge-icon $RPM_BUILD_ROOT/lib/lilo/pmac
cp -av README* $RPM_BUILD_ROOT%{_docdir}/lilo/
cp -av COPYING $RPM_BUILD_ROOT%{_docdir}/lilo/
cp -av man/lilo.conf.5 $RPM_BUILD_ROOT%{_mandir}/man5
cp -av man/lilo.8 $RPM_BUILD_ROOT%{_mandir}/man8
cp -av man/show_of_path.sh.8 $RPM_BUILD_ROOT%{_mandir}/man8
pushd bootheader
make install DESTDIR=$RPM_BUILD_ROOT
popd
popd
pushd yaboot
cp -av yaboot yaboot.debug $RPM_BUILD_ROOT/lib/lilo/pmac
cp -av yaboot.chrp* $RPM_BUILD_ROOT/lib/lilo/chrp
cp -av crt0.o $RPM_BUILD_ROOT/lib/lilo/chrp/yaboot.crt0.o
cp -av ld.script $RPM_BUILD_ROOT/lib/lilo/chrp/yaboot.ld.script
cp -av yaboot.a $RPM_BUILD_ROOT/lib/lilo/chrp/
cp -av make_yaboot.sh $RPM_BUILD_ROOT/lib/lilo/scripts/
cp -av man/bootstrap.8 man/yaboot.8 $RPM_BUILD_ROOT%{_mandir}/man8
cp -av man/yaboot.conf.5 $RPM_BUILD_ROOT%{_mandir}/man5
popd
#powerpc
%endif

%triggerpostun  -- lilo < 0.0.10
# for manual updates
if [ -f /etc/lilo.conf.rpmsave -a ! -f /etc/lilo.conf ] ; then
mv -v /etc/lilo.conf.rpmsave /etc/lilo.conf
fi
exit 0

%files
%defattr (-,root,root)
%ifarch %ix86 x86_64
/sbin/*
/usr/sbin/*
/boot/*.b
%else
#powerpc
%dir /lib/lilo
%dir /lib/lilo/pmac
%dir /lib/lilo/prep
%dir /lib/lilo/chrp
%dir /lib/lilo/ps3
%dir /lib/lilo/common
%dir /lib/lilo/scripts
%dir /lib/lilo/utils
#
%attr(755,root,root) /bin/mkzimage_cmdline
%attr(755,root,root) %config /bin/show_of_path.sh
%attr(755,root,root) %config /bin/mkzimage
%attr(755,root,root) %config /lib/lilo/pmac/os-badge-icon
%attr(644,root,root) /lib/lilo/pmac/*.bin
%attr(644,root,root) /lib/lilo/pmac/yaboot*
%attr(644,root,root) /lib/lilo/ps3/*
%attr(644,root,root) /lib/lilo/*/*.o
%attr(644,root,root) /lib/lilo/*/*.a
%attr(644,root,root) %config /lib/lilo/*/*ld.script*
%attr(644,root,root) %config /lib/lilo/lilo-*.lib
%attr(644,root,root) /lib/lilo/chrp/yaboot.chrp*
%attr(755,root,root) %config /lib/lilo/scripts/*.sh
%attr(755,root,root) /lib/lilo/utils/*
%attr(755,root,root) %config /sbin/lilo
%doc %{_docdir}/lilo
%endif
%doc %{_mandir}/*/*

%changelog
