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


Name:           buckygen
Version:        1.1
Release:        0
Summary:        Generator for nonisomorphic fullerenes
License:        GPL-3.0-or-later
Group:          Productivity/Scientific/Math
URL:            http://caagt.ugent.be/buckygen/
Source:         http://caagt.ugent.be/buckygen/%name-%version.zip
BuildRequires:  unzip

%description
Buckygen is a program for the efficient generation of all
nonisomorphic fullerenes. These are triangulations where all vertices
have degree 5 or 6. Or if the dual representation is used: cubic
plane graphs where all faces are pentagons or hexagons.

%prep
%autosetup -p1

%build
%make_build CFLAGS="%optflags"

%install
mkdir -p "%buildroot/%_bindir"
cp -a buckygen "%buildroot/%_bindir/"

%files
%_bindir/buckygen
%doc *.txt

%changelog
