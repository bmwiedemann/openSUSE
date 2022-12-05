#
# spec file for package msgpack-cxx
#
# Copyright (c) 2022 SUSE LLC
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


Name:           msgpack-cxx
Version:        4.1.3
Release:        0
Summary:        Object serialization library for cross-language communication (C++ interface)
License:        BSL-1.0
Group:          Development/Libraries/C and C++
URL:            https://msgpack.org
Source:         https://github.com/msgpack/msgpack-c/releases/download/cpp-%version/msgpack-cxx-%version.tar.gz
BuildRequires:  boost-devel
BuildRequires:  c++_compiler
BuildRequires:  cmake
BuildRequires:  pkg-config

%description
MessagePack is a binary-based object serialization library. It enables to
exchange structured objects between many languages like JSON.

%package devel
Summary:        Development headers for libmsgpack C++ library
Group:          Development/Libraries/C and C++
Requires:       libboost_headers-devel
Requires:       msgpack-c-devel >= 4
Provides:       libmsgpack-devel = %{version}-%{release}
Conflicts:      msgpack-devel < 4

%description devel
MessagePack is a binary-based object serialization library. It enables to
exchange structured objects between many languages like JSON.

This package provides C++ headers and other devel files.

%prep
%autosetup

%build
%cmake
%make_jobs

%install
%cmake_install

%files devel
%license COPYING
%doc NOTICE README.md
%_includedir/msgpack*
%_libdir/cmake/

%changelog
