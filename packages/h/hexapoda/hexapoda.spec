#
# spec file for package hexapoda
#
# Copyright (c) 2026, Martin Hauke <mardnh@gmx.de>
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


Name:           hexapoda
Version:        1.0.0
Release:        0
Summary:        A colorful modal hex editor
License:        GPL-2.0-or-later
URL:            https://github.com/simonomi/hexapoda
#Git-Clone:     https://github.com/simonomi/hexapoda.git
Source:         %{name}-%{version}.tar.gz
Source1:        vendor.tar.zst
BuildRequires:  cargo-packaging
Requires(post): permissions

%description
A colorful modal hex editor.

%prep
%autosetup -p 1 -a 1

%build
%{cargo_build}

%install
%{cargo_install}

%check
%{cargo_test}

%files
%license LICENSE
%doc README.md
%{_bindir}/hexapoda

%changelog
