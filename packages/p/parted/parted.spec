#
# spec file for package parted
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


Name:           parted
Version:        3.3
Release:        0
Summary:        GNU partitioner
License:        GPL-3.0-or-later
Group:          System/Filesystems
URL:            http://www.gnu.org/software/parted/
Source0:        ftp://ftp.gnu.org/gnu/parted/%{name}-%{version}.tar.xz
Source1:        ftp://ftp.gnu.org/gnu/parted/%{name}-%{version}.tar.xz.sig
Source2:        https://savannah.gnu.org/project/memberlist-gpgkeys.php?group=parted&download=1#/%{name}.keyring
Source3:        baselibs.conf
Source4:        fatresize-0.1.tar.bz2
# Build patches
Patch1:         parted-2.4-ncursesw6.patch

# Other patches
Patch10:        hfs_fix.dif
Patch11:        parted-wipeaix.patch
Patch12:        libparted-partition-naming.patch
#PATCH-FEATURE-SUSE more-reliable-informing-the-kernel.patch bnc#657360 petr.uzel@suse.cz
Patch13:        more-reliable-informing-the-kernel.patch
Patch14:        dummy-bootcode-only-for-x86.patch
Patch15:        parted-type.patch
Patch16:        parted-mac.patch
Patch17:        libparted-use-BLKRRPART-for-DASD.patch.patch
Patch18:        libparted-make-BLKRRPART-more-robust.patch
Patch19:        libparted-dasd-implicit-partition-disk-flag.patch
# Remove following compatibility patch once bnc#931765 is resolved
Patch20:        parted-resize-alias-to-resizepart.patch
Patch21:        libparted-avoid-libdevice-mapper-warnings.patch
# Patch31 dropped for bsc#1058667
Patch22:        libparted-open-the-device-RO-and-lazily-switch-to-RW.patch
Patch23:        parted-implement-wipesignatures-option.patch
# bsc#982169
Patch24:        libparted-fix-nvme-partition-naming.patch
# fate#314888
Patch25:        libparted-dasd-improve-lvm-raid-flag-handling.patch
Patch26:        parted-mkpart-set-a-swap-flag-if-available.patch
Patch27:        libparted-dasd-add-swap-flag-handling-for-DASD-CDL.patch
Patch28:        parted-mkpart-allow-empty-gpt-part-name.patch
Patch29:        libparted-fix-NVDIMM-partition-naming.patch
Patch30:        parted-escape-printed-device-path.patch
Patch31:        parted-add-ignore-busy-option.patch
Patch32:        parted-fix-resizepart-and-rm-command.patch
Patch33:        libparted-use-BLKRRPART-only-when-needed.patch
Patch34:        libparted-canonicalize-dev-md-paths.patch
Patch35:        parted-fix-end_input-usage.patch 

# bsc#1168756
Patch36:        libparted-linux-pmem-path.patch

# bsc#1164260
Patch37:        parted-print-max-partitions-for-yast.patch
# bsc#1164907
Patch64:        parted-type-accept-hex.patch
# Fatresize
Patch100:       parted-fatresize-autoconf.patch
Patch101:       fatresize-fix-getting-dev-name.patch
# Tests patches
Patch156:       tests-add-helper-require_swap_.patch
Patch157:       tests-add-dev-md-check-to-t6100.patch

# SUSE tests patches
Patch200:       tests-adapt-to-SUSE.patch
BuildRequires:  check-devel
BuildRequires:  device-mapper-devel >= 1.02.33
BuildRequires:  e2fsprogs-devel
BuildRequires:  libblkid-devel >= 2.17
BuildRequires:  libreiserfs-devel
BuildRequires:  libselinux-devel
BuildRequires:  libsepol-devel
BuildRequires:  libtool
BuildRequires:  libuuid-devel
BuildRequires:  makeinfo
BuildRequires:  pkg-config
BuildRequires:  readline-devel
PreReq:         %install_info_prereq
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
# bug437293
%ifarch ppc64
Obsoletes:      parted-64bit
%endif

%description
GNU Parted is a program for creating, destroying, resizing, checking,
and copying partitions, and the file systems on them.

%package -n libparted0
Summary:        Library for manipulating partitions
Group:          System/Libraries

%description -n libparted0
Libparted is a library for creating, destroying, resizing, checking
and copying partitions and the file systems on them.

%package devel
Summary:        Parted Include Files and Libraries necessary for Development
Group:          Development/Libraries/C and C++
Requires:       device-mapper-devel >= 1.02.33
Requires:       e2fsprogs-devel
Requires:       libparted0 = %version
Requires:       libreiserfs-devel
# bug437293
%ifarch ppc64
Obsoletes:      parted-devel-64bit
%endif

%description devel
This package contains all necessary include files and libraries needed
to develop applications that require these.

%lang_package
%prep
%setup -a 4
%patch1 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1
%patch14 -p1
%patch15 -p1
%patch16 -p1
%patch17 -p1
%patch18 -p1
%patch19 -p1
%patch20 -p1
%patch21 -p1
%patch22 -p1
%patch23 -p1
%patch24 -p1
%patch25 -p1
%patch26 -p1
%patch27 -p1
%patch28 -p1
%patch29 -p1
%patch30 -p1
%patch31 -p1
%patch32 -p1
%patch33 -p1
%patch34 -p1
%patch35 -p1
%patch36 -p1
%patch37 -p1
%patch64 -p1
%patch100 -p1
%patch101 -p1
%patch156 -p1
%patch157 -p1
%patch200 -p1

%build
export CFLAGS="%{optflags} `ncursesw6-config --cflags`"
export LIBS="`ncursesw6-config --libs`"
AUTOPOINT=true autoreconf --force --install
%configure	--disable-static		\
		--enable-device-mapper=yes	\
		--enable-dynamic-loading=no 	\
		--enable-selinux		\
		--disable-silent-rules
make %{?_smp_mflags}

%install
%make_install
rm %{buildroot}%{_libdir}/*.la
%find_lang %{name}

%post
%install_info --info-dir=%{_infodir} %{_infodir}/%{name}.info.gz

%preun
%install_info_delete --info-dir=%{_infodir} %{_infodir}/%{name}.info.gz

%post -n libparted0 -p /sbin/ldconfig
%postun -n libparted0 -p /sbin/ldconfig

%files
%defattr(-,root,root)
%license COPYING
%doc AUTHORS BUGS ChangeLog NEWS README THANKS TODO
%{_sbindir}/*
%{_mandir}/man8/part*.8.gz
%doc %{_infodir}/*.info*

%files devel
%defattr(-,root,root)
%doc doc/API doc/FAT
%{_includedir}/*
%{_libdir}/pkgconfig/libparted*.pc
%{_libdir}/*.so

%files -n libparted0
%defattr(-,root,root)
%{_libdir}/*.so.*

%files lang -f %{name}.lang

%changelog
