#
# spec file for package pcr-oracle
#
# Copyright (c) 2025 SUSE LLC
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


Name:           pcr-oracle
Version:        0.5.8
Release:        0
Summary:        Predict TPM PCR values
License:        GPL-2.0-or-later
Group:          System/Boot
URL:            https://github.com/openSUSE/pcr-oracle
Source:         %{name}-%{version}.tar.xz
BuildRequires:  libelf-devel
BuildRequires:  libfdisk-devel
BuildRequires:  libopenssl-devel >= 3.0.0
BuildRequires:  tpm2-0-tss-devel >= 2.4.0
Requires:       libtss2-tcti-device0
ExclusiveArch:  x86_64 aarch64 ppc64le riscv64 %{arm}

%description
This utility tries to predict the values of the TPM's Platform
Configuration Registers following an update of system components
like shim, grub, etc.

%prep
%autosetup -p1

%build
# beware, this is not autoconf
./configure --prefix /usr
make CCOPT="%optflags"

%install
make install DESTDIR=%{buildroot}
install -d %{buildroot}/%{_bindir}
mv %{buildroot}/bin/pcr-oracle %{buildroot}/%{_bindir}
rmdir %{buildroot}/bin

%files
%defattr(-,root,root)
%doc README.md
%doc test-authorized.sh
%{_bindir}/pcr-oracle
%{_mandir}/man8/pcr-oracle.8*

%changelog
