#
# spec file for package memtest86+
#
# Copyright (c) 2021 SUSE LLC
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


Name:           memtest86+
Version:        5.31b
Release:        0
Summary:        Memory Testing Image for x86 Architecture
License:        BSD-3-Clause
Group:          System/Boot
URL:            https://www.memtest.org
Source:         https://www.memtest.org/download/%{version}/memtest86+-%{version}.tar.gz
Patch0:         fix-destdir
Patch1:         memtest86+-5.01-no-optimization.patch
Patch2:         memtest86+-5.31b-discard-note_gnu_property.patch
#!BuildIgnore:  gcc-PIE
Provides:       lilo:/boot/memtest.bin
Obsoletes:      memtest86 <= 3.2
Provides:       memtest86 > 3.2
ExclusiveArch:  %{ix86} x86_64
%ifarch x86_64
BuildRequires:  glibc-devel-32bit
%endif
%define _binary_payload w1.gzdio
BuildRequires:  update-bootloader-rpm-macros
%{?update_bootloader_requires}

%description
Memtest86 is an image that can be booted instead of a real OS. Once booted,
it can be used to test the computer's memory.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
# dependencies are broken for the package and it should not be built in parallel
make

%install
install -Dpm 0644 memtest.bin \
  %{buildroot}/boot/memtest.bin

%post
%update_bootloader_check_type_refresh_post grub2

%posttrans
%update_bootloader_posttrans

%files
/boot/memtest.bin
%doc README* changelog FAQ

%changelog
