#
# spec file for package thunderbolt-utils
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


Name:           thunderbolt-utils
Version:        0.1~rc1
Release:        0
Summary:        User-space utilities for Thunderbolt/USB4
License:        LGPL-2.0 AND GPL-2.0
Group:          Hardware/Other
URL:            https://github.com/intel/thunderbolt-utils
Source:         https://github.com/intel/thunderbolt-utils/archive/refs/tags/v0.1-rc1.tar.gz
Patch1:         pull-4.patch
Patch2:         pull-5.patch
BuildRequires:  c_compiler
BuildRequires:  make

%description
This software is a collection of various user-space functionalities
for the thunderbolt/USB4 subsystem.

%prep
%autosetup -p1 -n %name-0.1-rc1

%build
pushd lib
%make_build CFLAGS="%optflags"
popd

%install
pushd lib
b="%buildroot"
mkdir -p "$b/%_bindir"
cp -a lstbt "$b/%_bindir/"
popd

%files
%_bindir/ls*
%license LICENSES/*

%changelog
