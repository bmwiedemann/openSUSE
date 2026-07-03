#
# spec file for package libchdr
#
# Copyright (c) 2026 SUSE LLC and contributors
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


Name:           libchdr
%define lname   libchdr0
Version:        0.3.0
Release:        0
Summary:        Library for reading MAME's CHDv1 to v5 formats
License:        BSD-3-Clause
Group:          Development/Libraries/C and C++
URL:            https://github.com/rtissera/libchdr
Source:         https://github.com/rtissera/libchdr/archive/refs/tags/v%version.tar.gz
BuildRequires:  cmake
BuildRequires:  pkg-config

%description
libchdr is a standalone library for reading MAME's CHDv1-v5 formats

%package -n %lname
Summary:        Library for reading MAME's CHDv1 to v5 formats
Group:          System/Libraries

%description -n %lname
libchdr is a standalone library for reading MAME's CHDv1-v5 formats

%package devel
Summary:        Development headers for libchdr
Group:          Development/Libraries/C and C++
Requires:       %lname = %{version}

%description devel
Development headers for libchdr

%prep
%autosetup -p1

%build
%cmake
%cmake_build

%install
%cmake_install

%ldconfig_scriptlets -n %lname

%files -n %lname
%license LICENSE.txt
%doc README.md
%_libdir/libchdr.so.0*

%files devel
%_includedir/libchdr/
%_libdir/pkgconfig/libchdr.pc
%_libdir/libchdr.so

%changelog
