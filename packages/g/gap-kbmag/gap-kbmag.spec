#
# spec file for package gap-kbmag
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


Name:           gap-kbmag
Version:        1.5.11
Release:        0
Summary:        GAP: Knuth-Bendix on Monoids and Automatic Groups
License:        GPL-2.0-or-later
Group:          Productivity/Scientific/Math
URL:            https://gap-packages.github.io/kbmag/
#Git-Clone:     https://github.com/gap-packages/kbmag
Source:         https://github.com/gap-packages/kbmag/releases/download/v%version/kbmag-%version.tar.gz
BuildRequires:  gap-devel
BuildRequires:  gap-rpm-devel
BuildRequires:  xz
Requires:       gap-core >= 4.7

%description
The kbmag package is a GAP interface to some C programs for running
the Knuth-Bendix completion program on finite semigroup, monoid or
group presentations, and for attempting to compute automatic
structures of finitely presented groups.

%prep
%setup -qn kbmag-%version

%build
find . -type f "(" -name "*.g" -o -name "*.gd" ")" -exec chmod a-x "{}" "+"
./configure "%gapdir"
%make_build

%install
rm -Rf standalone scripts
%gappkg_simple_install

%files -f %name.files

%changelog
