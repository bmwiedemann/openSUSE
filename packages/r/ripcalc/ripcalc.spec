#
# spec file for package ripcalc
#
# Copyright (c) 2025 Andreas Stieger <Andreas.Stieger@gmx.de>
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


Name:           ripcalc
Version:        0.1.13
Release:        0
Summary:        Tool for network addresses
License:        GPL-3.0-or-later
URL:            https://www.usenix.org.uk/content/ripcalc.html
# git: https://gitlab.com/edneville/ripcalc
Source0:        %{name}-%{version}.tar.xz
Source1:        vendor.tar.zst
BuildRequires:  cargo-packaging
BuildRequires:  rust >= 1.69
ExclusiveArch:  %{rust_tier1_arches}

%description
Ripcalc is a tool for calculate or looking up network addresses. Supports CSV
file formats for network information lists.

%prep
%autosetup -p1 -a1
%if 0%{?suse_version} < 1600
find Cargo.lock vendor/ -type f -name Cargo.lock -exec sed -Ei 's/^version = 4$/version = 3/g' {} \;
%endif

%build
%{cargo_build}

%install
%{cargo_install}
mkdir -p %{buildroot}%{_mandir}/man1/
cp -v ripcalc.1 %{buildroot}%{_mandir}/man1/

%check
%{cargo_test}

%files
%license LICENSE
%{_bindir}/ripcalc
%doc changelog.md README.md ripcalc.md
%{_mandir}/man1/ripcalc.1%{?ext_man}

%changelog
