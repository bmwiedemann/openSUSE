#
# spec file for package parted
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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
Version:        3.2
Release:        0
Summary:        GNU partitioner
License:        GPL-3.0-or-later
Group:          System/Filesystems
Url:            http://www.gnu.org/software/parted/
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
Patch17:        dummy-bootcode-only-for-x86.patch
Patch18:        parted-type.patch
Patch19:        parted-mac.patch
Patch21:        libparted-use-BLKRRPART-for-DASD.patch.patch
Patch22:        libparted-allow-bigger-snap-radius-if-cylinders-are-used.patch
Patch23:        libparted-make-BLKRRPART-more-robust.patch
Patch24:        libparted-make-sure-not-to-treat-percentages-and-cyls-as-exact.patch
Patch25:        libparted-dasd-implicit-partition-disk-flag.patch
Patch26:        lib-fs-resize-prevent-crash-resizing-FAT16.patch
Patch27:        parted-dont-crash-in-disk_set-when-disk-label-not-found.patch
Patch28:        libparted-device-mapper-uses-512b-sectors.patch
# Remove following compatibility patch once bnc#931765 is resolved
Patch29:        parted-resize-alias-to-resizepart.patch
Patch30:        libparted-avoid-libdevice-mapper-warnings.patch
# Patch31 dropped for bsc#1058667
Patch32:        libparted-Use-read-only-when-probing-devices-on-linu.patch
Patch33:        libparted-open-the-device-RO-and-lazily-switch-to-RW.patch
Patch34:        parted-implement-wipesignatures-option.patch
# bsc#982169
Patch35:        libparted-Add-support-for-NVMe-devices.patch
Patch36:        libparted-fix-nvme-partition-naming.patch
Patch37:        libparted-dont-warn-if-no-HDIO_GET_IDENTITY.patch
# fate#320525 / bsc#935127
Patch38:        0001-fdasd-geometry-handling-updated-from-upstream-s390-t.patch
Patch39:        0002-dasd-enhance-device-probing.patch
Patch40:        0003-parted-fix-build-error-on-s390.patch
Patch41:        0004-fdasd.c-Safeguard-against-geometry-misprobing.patch
Patch42:        0005-libparted-Remove-fdasd-geometry-code-from-alloc_meta.patch
# fate#321531
Patch43:        libparted-dasd-unify-vtoc-handling-for-cdl-ldl.patch
Patch44:        libparted-dasd-update-and-improve-fdasd-functions.patch
Patch45:        libparted-dasd-add-new-fdasd-functions.patch
Patch46:        libparted-Add-support-for-RAM-drives.patch
# fate#314888
Patch47:        libparted-dasd-improve-lvm-raid-flag-handling.patch
Patch48:        parted-mkpart-set-a-swap-flag-if-available.patch
Patch49:        libparted-set-swap-flag-on-GPT-partitions.patch
Patch50:        libparted-dasd-add-swap-flag-handling-for-DASD-CDL.patch
Patch51:        parted-mkpart-allow-empty-gpt-part-name.patch
Patch52:        libparted-fix-starting-CHS-in-protective-MBR.patch
Patch53:        libparted-BLKPG_RESIZE_PARTITION-uses-bytes.patch
Patch54:        libparted-fix-udev-cookie-leak.patch
Patch55:        libparted-Add-support-for-NVDIMM-devices.patch
Patch56:        libparted-fix-NVDIMM-partition-naming.patch
Patch57:        parted-escape-printed-device-path.patch
Patch58:        parted-add-ignore-busy-option.patch
Patch59:        parted-fix-resizepart-and-rm-command.patch
Patch60:        libparted-use-BLKRRPART-only-when-needed.patch
Patch61:        libparted-canonicalize-dev-md-paths.patch
Patch62:        libparted-sysmacros.patch

# bsc#1136245
Patch63:        libparted-dasd-correct-the-offset-where-the-first-pa.patch
Patch64:        parted-fix-crash-due-to-improper-partition-number-in.patch	
Patch65:        parted-fix-wrong-error-label-jump-in-mkpart.patch 
Patch66:        clean-the-disk-information-when-commands-fail-in-int.patch 
Patch67:        parted-check-the-name-of-partition-first-when-to-nam.patch 
Patch68:        parted-ui-remove-unneccesary-information-of-command.patch 
Patch69:        libpartd-dasd-improve-flag-processing-for-DASD-LDL.patch 
Patch70:        libparted-dasd-add-an-exception-for-changing-DASD-LD.patch 
Patch71:        libparted-dasd-add-test-cases-for-the-new-fdasd-func.patch 

# Fatresize
Patch100:       parted-fatresize-autoconf.patch
Patch101:       fatresize-fix-getting-dev-name.patch
# Upstream tests patches
Patch150:       tests-set-optimal-blocks-for-scsi_debug.patch
Patch151:       tests-increase-scsi_debug-tmo.patch
Patch152:       tests-use-wait_for_dev_to_-functions.patch
Patch153:       tests-wait_for_-loop.patch
Patch154:       tests-update-t0220-t0280-for-swap-flag.patch
Patch155:       tests-check-extended-partition-length.patch
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
%patch17 -p1
%patch18 -p1
%patch19 -p1
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
%patch32 -p1
%patch33 -p1
%patch34 -p1
%patch35 -p1
%patch36 -p1
%patch37 -p1
%patch38 -p1
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
%patch49 -p1
%patch50 -p1
%patch51 -p1
%patch52 -p1
%patch53 -p1
%patch54 -p1
%patch55 -p1
%patch56 -p1
%patch57 -p1
%patch58 -p1
%patch59 -p1
%patch60 -p1
%patch61 -p1
%patch62 -p1
%patch63 -p1
%patch64 -p1
%patch65 -p1
%patch66 -p1
%patch67 -p1
%patch68 -p1
%patch69 -p1
%patch70 -p1
%patch71 -p1
%patch100 -p1
%patch101 -p1
%patch150 -p1
%patch151 -p1
%patch152 -p1
%patch153 -p1
%patch154 -p1
%patch155 -p1
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
%{_libdir}/pkgconfig/libparted.pc
%{_libdir}/*.so

%files -n libparted0
%defattr(-,root,root)
%{_libdir}/*.so.*

%files lang -f %{name}.lang

%changelog
