#
# spec file for package trustedgrub2
#
# Copyright (c) 2022 SUSE LLC
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


Name:           trustedgrub2
Version:        1.4.0
Release:        0
Summary:        Bootloader with TCG (TPM) support
License:        GPL-3.0-or-later
Group:          System/Boot
URL:            https://github.com/Sirrix-AG/TrustedGRUB2
Source0:        %{name}-%{version}.tar.gz
Source1:        trustedgrub2.rpmlintrc
Source2:        HOWTO.luks-keyfile
Patch1:         use-grub2-as-a-package-name.patch
Patch2:         grub2-linguas.sh-no-rsync.patch
Patch3:         0001-build-Use-AC_HEADER_MAJOR-to-find-device-macros.patch
Patch4:         0002-configure-fix-check-for-sys-sysmacros.h-under-glibc-.patch
# from upstream a3e9da054d00260f274cfd9d1b9611c32ecd437c
Patch5:         trustedgrub2-no-pie.patch
# from upstream b53f595b3ed989335d7cd1618a5502270cdb26de
Patch6:         trustedgrub2-no-pie2.patch
# fix build against gcc-7
Patch7:         0001-btrfs-avoid-used-uninitialized-error-with-GCC7.patch
Patch8:         0002-i386-x86_64-ppc-fix-switch-fallthrough-cases-with-GC.patch
Patch9:         0003-Add-gnulib-fix-gcc7-fallthrough.diff.patch
# fix build against flex-2.6.4
Patch10:        grub2-fix-build-with-flex-2.6.4.patch
# fix build against GCC-8
Patch11:        0001-Fix-packed-not-aligned-error-on-GCC-8.patch
# fix "no symbol table" error on new binutil, backport patches
Patch12:        0001-Verify-modules-on-build-time-rather-than-failing-in-.patch
Patch13:        0002-module-verifier-Check-range-limited-relative-relocat.patch
Patch14:        0003-support-modules-without-symbol-table.patch
# fix build against GCC-9
Patch15:        0001-cpio-Disable-gcc9-Waddress-of-packed-member.patch
Patch16:        0002-jfs-Disable-gcc9-Waddress-of-packed-member.patch
Patch17:        0003-hfs-Fix-gcc9-error-Waddress-of-packed-member.patch
Patch18:        0004-hfsplus-Fix-gcc9-error-with-Waddress-of-packed-membe.patch
Patch19:        0005-acpi-Fix-gcc9-error-Waddress-of-packed-member.patch
Patch20:        0006-usbtest-Disable-gcc9-Waddress-of-packed-member.patch
Patch21:        0007-chainloader-Fix-gcc9-error-Waddress-of-packed-member.patch
Patch22:        0008-efi-Fix-gcc9-error-Waddress-of-packed-member.patch
# fix build against GCC-10
Patch23:        0001-mdraid1x_linux-Fix-gcc10-error-Werror-array-bounds.patch
Patch24:        0002-zfs-Fix-gcc10-error-Werror-zero-length-bounds.patch
Patch25:        0003-linux-Fix-gcc10-error-Werror-zero-length-bounds.patch
# fix very large image file produced by recent gcc version
Patch26:        0001-build-Fix-GRUB-i386-pc-build-with-Ubuntu-gcc.patch
# Btrfs snapshot booting related patches
Patch101:       grub2-btrfs-01-add-ability-to-boot-from-subvolumes.patch
Patch102:       grub2-btrfs-02-export-subvolume-envvars.patch
Patch103:       grub2-btrfs-03-follow_default.patch
Patch104:       grub2-btrfs-04-subvol-mount.patch
Patch105:       grub2-btrfs-05-subvol-fallback.patch
Patch110:       grub2-menu-unrestricted.patch
Patch111:       0001-Fix-Werror-array-bounds-array-subscript-0-is-outside.patch
Patch112:       0002-reed_solomon-Fix-array-subscript-0-is-outside-array-.patch
BuildRequires:  automake
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  gcc
BuildRequires:  python3
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
ExclusiveArch:  %{ix86} x86_64

%define _unpackaged_files_terminate_build 0

# Modules code is dynamically loaded and collected from a _fixed_ path.
%define _libdir %{_exec_prefix}/lib

%ifarch %{ix86} x86_64
%define grubcpu i386
%define platform pc
%endif

%define grubarch %{grubcpu}-%{platform}

%description
This package provides the alternatives made to transform a standard GRUB2
into a version that offers TCG (TPM) support for granting the integrity of the
boot process (trusted boot). This project was highly inspired by the former
projects TrustedGrub1 and GRUB-IMA. However TrustedGRUB2 was completely written
from scratch.

%package %{grubarch}

Summary:        Bootloader with TCG (TPM) support
Group:          System/Boot
BuildArch:      noarch

%description %{grubarch}
This package provides the alternatives made to transform a standard GRUB2
into a version that offers TCG (TPM) support for granting the integrity of the
boot process (trusted boot). This project was highly inspired by the former
projects TrustedGrub1 and GRUB-IMA. However TrustedGRUB2 was completely written
from scratch.

This package contains modules for %{platform} systems.

%prep
%autosetup -p1

# HOWTO.luks-keyfile
cp %{SOURCE2} .

mkdir build

%build
export PYTHON="python3"
./autogen.sh
# We don't want to let rpm override *FLAGS with default a.k.a bogus values.
CFLAGS="-fno-strict-aliasing -fno-inline-functions-called-once "
CXXFLAGS=" "
FFLAGS=" "
export CFLAGS CXXFLAGS FFLAGS

cd build

%define _configure ../configure
%configure \
	--target=%{grubcpu} \
	--with-platform=%{platform} \
	--program-transform-name=s,grub,%{name},

make %{?_smp_mflags}

%install
cd build
make install-data DESTDIR=%{buildroot} %{?_smp_mflags}

# *.module files are installed with executable bits due to the way grub2 build
# system works. Clear executable bits to not confuse find-debuginfo.sh
find $RPM_BUILD_ROOT%{_libdir}/%{name} \
       \( -name '*.module' -o -name '*.image' -o -name '*.exec' \) -print0 | \
       xargs --no-run-if-empty -0 chmod a-x

%post

%postun

%files
%defattr(-,root,root,-)
%doc COPYING README.md Changelog.md HOWTO.luks-keyfile

%files %{grubarch}
%defattr(-,root,root,-)
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/%{grubarch}
%{_libdir}/%{name}/%{grubarch}/*

%changelog
