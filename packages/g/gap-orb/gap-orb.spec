#
# spec file for package gap-orb
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


Name:           gap-orb
Version:        4.9.2
Release:        0
Summary:        GAP: Methods to enumerate Orbits
License:        GPL-3.0-or-later
Group:          Productivity/Scientific/Math
URL:            https://gap-packages.github.io/orb
#Git-Clone:	https://github.com/gap-packages/orb
Source:         https://github.com/gap-packages/orb/releases/download/v%version/orb-%version.tar.gz
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gap-devel >= 4.12
BuildRequires:  gap-rpm-devel
BuildRequires:  gmp-devel
BuildRequires:  libtool
Requires:       gap-core >= 4.12
Suggests:       gap-io >= 3.3

%description
The orb package is about enumerating orbits in various ways.

%prep
%autosetup -n orb-%version

%build
./configure --with-gaproot="%gapdir"
%make_build

%install
%gappkg_simple_install
pushd "%buildroot/$moddir"
rm -Rf src
popd

%files -f %name.files

%changelog
