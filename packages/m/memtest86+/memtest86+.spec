#
# spec file for package memtest86+
#
# Copyright (c) 2026 SUSE LLC and contributors
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
Version:        8.10
Release:        0
Summary:        Memory Testing Image for x86 Architecture
License:        GPL-2.0-only
Group:          System/Boot
URL:            https://www.memtest.org
Source:         https://github.com/memtest86plus/memtest86plus/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        20_memtest86
Source2:        memtest86plus.conf
#!BuildIgnore:  gcc-PIE
Obsoletes:      memtest86 <= 3.2
Provides:       memtest86 > 3.2
ExclusiveArch:  %{ix86} x86_64
%ifarch x86_64
BuildRequires:  glibc-devel-32bit
%endif
BuildRequires:  pesign-obs-integration
%define _binary_payload w1.gzdio
Requires:       %{name}-bls = %{version}-%{release}
Requires:       (%{name}-grub2 if grub2-common)

%description
Memtest86 is an image that can be booted instead of a real OS. Once booted,
it can be used to test the computer's memory.

%package grub2
Summary:        Menu entry for GRUB2 bootloader
Requires:       %{name} = %{version}-%{release}
BuildRequires:  update-bootloader-rpm-macros
%{?update_bootloader_requires}
BuildArch:      noarch

%description grub2
Generates the menu entry for GRUB2 bootloader

%package bls
Summary:        Menu entry for BLS bootloader
Requires:       %{name} = %{version}-%{release}
Requires(postun): udev
Requires(posttrans): udev
BuildArch:      noarch

%description bls
Generates the menu entry for BLS bootloaders (GRUB2-EFI, systemd-boot)

%prep
%setup -q -n memtest86plus-%{version}

%build
# dependencies are broken for the package and it should not be built in parallel
%ifarch x86_64
cd build/x86_64
%else
cd build/i586
%endif
make

%install
# Script to generate memtest86+ menu entry (GRUB2)
mkdir -p %{buildroot}%{_sysconfdir}/grub.d
install -m 755 %{SOURCE1} %{buildroot}%{_sysconfdir}/grub.d/

# BLS menu entry
install -Dpm 0644 %{SOURCE2} %{buildroot}%{_prefix}/lib/memtest86/memtest86plus.conf
sed -i 's/\$VERSION\$/%{version}-%{release}/' %{buildroot}%{_prefix}/lib/memtest86/memtest86plus.conf

# Create file for sdbootutil
mkdir -p %{buildroot}%{_prefix}/lib/sdbootutil/entries.d
echo "# Menu entry and EFI binary for memtest86+" >> %{buildroot}%{_prefix}/lib/sdbootutil/entries.d/memtest86+.conf
echo "EFI=%{_prefix}/lib/memtest86/mt86plus.efi" >> %{buildroot}%{_prefix}/lib/sdbootutil/entries.d/memtest86+.conf
echo "ENTRY=%{_prefix}/lib/memtest86/memtest86plus.conf" >> %{buildroot}%{_prefix}/lib/sdbootutil/entries.d/memtest86+.conf

%ifarch x86_64
cd build/x86_64
%else
cd build/i586
%endif
install -Dpm 0644 mt86plus %{buildroot}%{_prefix}/lib/memtest86/mt86plus.efi
export BRP_PESIGN_FILES="*.efi"

%post grub2
%update_bootloader_check_type_refresh_post grub2 grub2-efi

%posttrans grub2
%update_bootloader_posttrans

%files
%license LICENSE
%doc README.md
%doc doc
%dir %{_prefix}/lib/memtest86
%{_prefix}/lib/memtest86/mt86plus.efi

%files grub2
%dir %{_sysconfdir}/grub.d
%config(noreplace) %{_sysconfdir}/grub.d/20_memtest86

%files bls
%dir %{_prefix}/lib/memtest86
%config(noreplace) %{_prefix}/lib/memtest86/memtest86plus.conf
%dir %{_prefix}/lib/sdbootutil
%dir %{_prefix}/lib/sdbootutil/entries.d
%config(noreplace) %{_prefix}/lib/sdbootutil/entries.d/memtest86+.conf

%changelog
