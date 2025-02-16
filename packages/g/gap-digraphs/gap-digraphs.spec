#
# spec file for package gap-digraphs
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


Name:           gap-digraphs
Version:        1.10.0
Release:        0
Summary:        GAP: Digraphs and multigraphs
License:        GPL-3.0-or-later
Group:          Productivity/Scientific/Math
URL:            https://digraphs.github.io/Digraphs/
#Git-Clone:     https://github.com/digraphs/Digraphs
Source:         https://github.com/digraphs/Digraphs/releases/download/v%version/digraphs-%version.tar.gz
BuildRequires:  edge-addition-planarity-suite-devel
BuildRequires:  fdupes
BuildRequires:  gap-devel
BuildRequires:  gap-rpm-devel
BuildRequires:  gcc-c++
BuildRequires:  gmp-devel
Requires:       gap-core >= 4.10
Requires:       gap-datastructures >= 0.2.5
Requires:       gap-io >= 4.5.1
Requires:       gap-orb >= 4.8.2
Suggests:       gap-autodoc >= 2020.08.11
Suggests:       gap-gapdoc >= 1.6.3
Suggests:       gap-grape >= 4.8.1
Suggests:       gap-nautytracesinterface >= 0.2
# Source contains a modified copy of bliss-0.73, so we cannot reuse bliss-devel
Provides:       bundled(bliss) = 0.73

%description
The Digraphs package is a GAP package containing methods for digraphs
and multidigraphs.

%prep
%autosetup -n digraphs-%version

%build
%configure --with-gaproot="%gapdir" --without-intrinsics \
	--with-external-planarity
%make_build
find . -type f -name "*~" -print -delete

%install
%gappkg_simple_install
pushd "%buildroot/$fmoddir/"
find . -type f -name .dirstamp -print -delete
# delete tests and assets
rm -Rf tst data/symmetric-closure.ds6.gz data/test-1.d6
# delete sources and build artifacts, user is not expected to rebuild in distribution tree
rm -Rf autom4te.cache src cnf config* m4 autogen.sh aclocal.m4 *.la Makefile*
rm -Rf extern/edge* extern/bliss*/[a-z]* extern/bliss*/.deps extern/bliss*/.libs extern/bliss*/.clang*
popd
%fdupes %buildroot/%_prefix

%files -f %name.files

%changelog
