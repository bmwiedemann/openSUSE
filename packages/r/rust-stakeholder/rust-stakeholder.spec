#
# spec file for package rust-stakeholder
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


Name:           rust-stakeholder
Version:        20250316
Release:        0
Summary:        Terminal output generator
License:        MIT
Group:          Amusements/Toys/Other
URL:            https://github.com/giacomo-b/rust-stakeholder
Source0:        %{name}-%{version}.tar.zst
Source1:        vendor.tar.zst
BuildRequires:  cargo >= 1.78
BuildRequires:  cargo-packaging
ExclusiveArch:  %{rust_tier1_arches}

%description
This package generates impressive-looking terminal output to look busy when
stakeholders walk by.

%prep
%autosetup -p1 -a1

%build
%{cargo_build}

%install
%{cargo_install}

%check
%{cargo_test}

%files
%license LICENSE
%doc README.md
%{_bindir}/rust-stakeholder

%changelog
