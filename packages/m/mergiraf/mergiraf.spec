#
# spec file for package mergiraf
#
# Copyright (c) 2024, Martin Hauke <mardnh@gmx.de>
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


Name:           mergiraf
Version:        0.3.1
Release:        0
Summary:        A syntax-aware git merge driver
License:        GPL-3.0-or-later
Group:          Development/Tools/Version Control
URL:            https://mergiraf.org/
#Git-Clone:     https://codeberg.org/mergiraf/mergiraf.git
Source:         %{name}-%{version}.tar.gz
Source1:        vendor.tar.zst
BuildRequires:  cargo-packaging
BuildRequires:  git-core
ExclusiveArch:  %{rust_tier1_arches}

%description
Mergiraf can solve a wide range of Git merge conflicts.
That's because it's aware of the trees in your files!

Thanks to its understanding of your language, it can often
reconcile the needs of both sides.

%prep
%autosetup -a 1

%build
%{cargo_build}

%install
%{cargo_install}

%check
%{cargo_test}

%files
%license LICENSE.txt
%doc README.md
%{_bindir}/mergiraf
%{_bindir}/mgf_dev

%changelog
