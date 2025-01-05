#
# spec file for package gap-cvec
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


Name:           gap-cvec
Version:        2.8.3
Release:        0
Summary:        GAP: Compact vectors over finite fields
License:        GPL-2.0-or-later
Group:          Productivity/Scientific/Math
URL:            https://gap-packages.github.io/cvec/
#Git-Clone:	https://github.com/gap-packages/cvec
Source:         https://github.com/gap-packages/cvec/releases/download/v%version/cvec-%version.tar.bz2
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gap-devel >= 4.12
BuildRequires:  gap-rpm-devel
BuildRequires:  gmp-devel
BuildRequires:  libtool
BuildRequires:  xz
Requires:       gap-core >= 4.12
Requires:       gap-gapdoc >= 1.2
Requires:       gap-io >= 4.1
Requires:       gap-orb >= 4.2

%description
This package provides an implementation of compact vectors over
finite fields. Contrary to earlier implementations no table lookups
are used but only word-based processor arithmetic. This allows for
bigger finite fields and higher speed.

%prep
%autosetup -n cvec-%version

%build
./configure "%gapdir"
%make_build
rm -v doc/clean

%install
%gappkg_simple_install
pushd "%buildroot/$fmoddir/"
rm -Rf autom4* aclocal* config* cnf m4 gen src
find . -type f -name "*.la" -print -delete
popd

%files -f %name.files

%changelog
