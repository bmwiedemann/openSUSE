#
# spec file for package buckygen
#
# Copyright (c) 2020 SUSE LLC
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


Name:           conauto
Version:        2.03
Release:        0
Summary:        Algorithm for graph isomorphism testing and automorphism group computation
License:        GPL-3.0-or-later
Group:          Productivity/Scientific/Math
URL:            https://sites.google.com/site/giconauto/
Source:         https://sites.google.com/site/giconauto/home/conauto-2.03.tar.gz
BuildRequires:  unzip

%description
The "conauto" algorithm tests whether two graphs are isomorphic. This is the
reference implementation.

%prep
%autosetup -p1

%build
pushd src/
%make_build OFLAGS="%optflags -fcommon"

%install
mkdir -p "%buildroot/%_bindir"
cp -a bin/conauto* "%buildroot/%_bindir/"

%files
%_bindir/conauto*
%doc src/*.txt

%changelog
