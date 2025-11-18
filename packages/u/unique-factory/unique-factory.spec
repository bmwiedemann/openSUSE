#
# spec file for package unique-factory
#
# Copyright (c) 2025 SUSE LLC and contributors
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


Name:           unique-factory
Version:        0.2.2
Release:        0
Summary:        Header-only C++ UniqueFactory
License:        GPL-2.0-or-later
Group:          Productivity/Scientific/Math
URL:            https://github.com/flatsurf/unique-factory
Source:         https://github.com/flatsurf/unique-factory/releases/download/%version/%name-%version.tar.gz
BuildRequires:  autoconf-archive
BuildRequires:  gcc-c++
BuildRequires:  libtool

%description
Header-only C++ UniqueFactory

%package devel
Summary:        Header-only C++ UniqueFactory
Group:          Development/Libraries/C and C++

%description devel
Header-only C++ UniqueFactory

%prep
%autosetup -p1

%build
autoreconf -fi
%configure --disable-static --without-googletest --without-benchmark
%make_build

%install
%make_install

%files devel
%_includedir/*
%license COPYING

%changelog
