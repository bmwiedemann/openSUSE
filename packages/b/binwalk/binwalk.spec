#
# spec file for package binwalk
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


Name:           binwalk
Version:        3.1.0
Release:        0
Summary:        Firmware Analysis Tool
License:        MIT
URL:            https://github.com/ReFirmLabs/binwalk/
Source0:        https://github.com/ReFirmLabs/binwalk/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        vendor.tar.zst
BuildRequires:  cargo
BuildRequires:  cargo-packaging
BuildRequires:  fdupes
BuildRequires:  help2man
BuildRequires:  pkgconfig
BuildRequires:  zstd
BuildRequires:  pkgconfig(fontconfig)

%description
Binwalk can identify, and optionally extract, files and data that
have been embedded inside of other files.

While its primary focus is firmware analysis, it supports a wide
variety of file and data types.

Through entropy analysis, it can even help to identify unknown
compression or encryption!

%prep
%autosetup -p1 -a1

%build
%{cargo_build}

%install
%{cargo_install}

help2man %{buildroot}%{_bindir}/binwalk --no-discard-stderr --version-string="%{version}" --no-info > binwalk.1
install -Dpm 0644 %{name}.1 %{buildroot}%{_mandir}/man1/%{name}.1

%files
%license LICENSE
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1%{?ext_man}

%changelog
