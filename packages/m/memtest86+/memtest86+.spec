#
# spec file for package memtest86+
#
# Copyright (c) 2024 SUSE LLC
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
# needssslcertforbuild


Name:           memtest86+
Version:        7.20
Release:        0
Summary:        Memory Testing Image for x86 Architecture
License:        GPL-2.0-only
Group:          System/Boot
URL:            https://www.memtest.org
Source:         https://github.com/memtest86plus/memtest86plus/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        20_memtest86
#!BuildIgnore:  gcc-PIE
Provides:       lilo:/boot/memtest.bin
Obsoletes:      memtest86 <= 3.2
Provides:       memtest86 > 3.2
ExclusiveArch:  %{ix86} x86_64
%ifarch x86_64
BuildRequires:  glibc-devel-32bit
%endif
BuildRequires:  pesign-obs-integration
%define _binary_payload w1.gzdio
BuildRequires:  update-bootloader-rpm-macros
%{?update_bootloader_requires}

%description
Memtest86 is an image that can be booted instead of a real OS. Once booted,
it can be used to test the computer's memory.

%prep
%setup -q -n memtest86plus-%{version}

%build
# dependencies are broken for the package and it should not be built in parallel
%ifarch x86_64
cd build64
%else
cd build32
%endif
make

%install
# Script to generate memtest86+ menu entry
mkdir -p %{buildroot}/%{_sysconfdir}/grub.d
install -m 755 %{SOURCE1} %{buildroot}/%{_sysconfdir}/grub.d/
%ifarch x86_64
cd build64
%else
cd build32
%endif
install -Dpm 0644 memtest.bin \
  %{buildroot}%{_prefix}/lib/memtest86/memtest.bin
install -Dpm 0644 memtest.efi \
  %{buildroot}%{_prefix}/lib/memtest86/memtest.efi
export BRP_PESIGN_FILES="*.efi"

%post
%update_bootloader_check_type_refresh_post grub2 grub2-efi

%posttrans
%update_bootloader_posttrans

%files
%license LICENSE
%doc README.md
%doc doc
%dir %{_prefix}/lib/memtest86
%{_prefix}/lib/memtest86/memtest.*
%dir %{_sysconfdir}/grub.d
%config(noreplace) %{_sysconfdir}/grub.d/20_memtest86

%changelog
