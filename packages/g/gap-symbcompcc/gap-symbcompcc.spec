#
# spec file for package gap-symbcompcc
#
# Copyright (c) 2023 SUSE LLC
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


Name:           gap-symbcompcc
Version:        1.3.2
Release:        0
Summary:        GAP: Computing with parametrised presentations for p-groups of fixed coclass
License:        GPL-2.0-or-later
Group:          Productivity/Scientific/Math
URL:            https://gap-packages.github.io/SymbCompCC/
#Git-Clone:     https://github.com/gap-packages/SymbCompCC
Source:         https://github.com/gap-packages/SymbCompCC/releases/download/v%version/SymbCompCC-%version.tar.gz
BuildArch:      noarch
BuildRequires:  gap-rpm-devel
Requires:       gap-core >= 4.7
Requires:       gap-polycyclic >= 2.11

%description
The SymbCompCC package computes with parametrised presentations for
finite p-groups of fixed coclass.

%prep
%autosetup -n SymbCompCC-%version

%build
find . -type f -name "*~" -delete
find . -type f -name "*.gi" -exec chmod a-x "{}" "+"

%install
%gappkg_simple_install

%files -f %name.files

%changelog
