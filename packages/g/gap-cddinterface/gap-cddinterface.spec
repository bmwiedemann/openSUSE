#
# spec file for package gap-cddinterface
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           gap-cddinterface
Version:        2024.09.02
Release:        0
Summary:        GAP: Interface to cddlib
License:        GPL-2.0-or-later
Group:          Productivity/Scientific/Math
URL:            https://homalg-project.github.io/CddInterface
#Git-Clone:	https://github.com/homalg-project/CddInterface
Source:         https://github.com/homalg-project/CddInterface/releases/download/v%version/CddInterface-%version.tar.gz
BuildRequires:  gap-devel
BuildRequires:  gap-rpm-devel
BuildRequires:  pkgconfig(cddlib)
Requires:       gap-core >= 4.12
Requires:       gap-gapdoc >= 1.5

%description
CddInterface is a GAP interface with the C package "cddlib" which,
among other things, can translate between H,V-representations of a
polyhedron P and solve linear programming problems over P, i.e. a
problem of maximizing and minimizing a linear function over P.

%prep
%autosetup -n CddInterface-%version

%build
%configure --with-gaproot="%gapdir"
%make_build

%install
%gappkg_simple_install
pushd "%buildroot/$fmoddir/"
rm -Rfv config.* configure* Makefile* src/
popd

%files -f %name.files

%changelog
