#
# spec file for package zdbsp
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           zdbsp
Version:        1.19
Release:        0
Summary:        Nodebuilder for ZDoom
License:        GPL-2.0+
Group:          Development/Tools/Building
Url:            https://zdoom.org/
Source:         https://github.com/rheit/zdbsp/archive/v%version/zdbsp-%version.tar.gz
Patch1:         zdbsp-bigendian.diff
Patch2:         zdbsp-notime.diff
Patch3:         install-binary.patch
BuildRequires:  cmake >= 2.4
BuildRequires:  gcc-c++
BuildRequires:  zlib-devel
BuildRoot:      %_tmppath/%name-%version-build

%description
ZDBSP is ZDoom's (internal and external) node builder. This node
builder was written with two design goals in mind: speed and
minimization of polyobject bleeding.

%prep
%setup -q
%patch -P 1 -P 2 -P 3 -p1

%build
%cmake

make %{?_smp_mflags}

%install
%cmake_install

%files
%defattr(-,root,root)
%doc zdbsp.html poly_*.png
%doc COPYING
%_bindir/zdbsp

%changelog
