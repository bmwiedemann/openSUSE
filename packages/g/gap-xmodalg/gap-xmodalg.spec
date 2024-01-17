#
# spec file for package gap-xmodalg
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           gap-xmodalg
Version:        1.23
Release:        0
Summary:        GAP: Crossed Modules and Cat1-Algebras
License:        GPL-2.0-or-later
Group:          Productivity/Scientific/Math
URL:            https://gap-packages.github.io/xmodalg/
#Git-Clone:     https://github.com/gap-packages/xmodalg
Source:         https://github.com/gap-packages/xmodalg/releases/download/v%version/XModAlg-%version.tar.gz
BuildRequires:  gap-rpm-devel
BuildArch:      noarch
Requires:       gap-core >= 4.11
Requires:       gap-laguna >= 3.9.3
Requires:       gap-xmod >= 2.87

%description
The XMod(Alg) package provides a collection of functions for
computing with crossed modules and cat1-algebras and morphisms of
these structures.

%prep
%autosetup -n XModAlg-%version

%build
find . -type f "(" -name "*.bak" -o -name ".log" -o -name "*~" ")" -delete

%install
%gappkg_simple_install

%files -f %name.files

%changelog
