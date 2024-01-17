#
# spec file for package gap-io
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


Name:           gap-io
Version:        4.8.2
Release:        0
Summary:        GAP: Bindings for low level C library IO
License:        GPL-3.0-or-later
Group:          Productivity/Scientific/Math
URL:            https://gap-packages.github.io/io/
#Git-Clone:     https://github.com/gap-packages/io
Source:       	https://github.com/gap-packages/io/releases/download/v%version/io-%version.tar.bz2
BuildRequires:  fdupes
BuildRequires:  gap-devel >= 4.11
BuildRequires:  gap-rpm-devel
BuildRequires:  gmp-devel
Requires:       gap-core >= 4.11

%description
The IO package provides bindings for GAP to the lower levels of
Input/Output functionality in the C library.

%prep
%autosetup -n io-%version

%build
%configure --with-gaproot="%gapdir"
%make_build
rm -v doc/clean

%install
%gappkg_simple_install
pushd "%buildroot/$fmoddir/"
rm -Rf aclocal* autom4* cnf config* m4 gen src
find . -type f -name "*.la" -print -delete
popd
%fdupes %buildroot/%_prefix

%files -f %name.files

%changelog
