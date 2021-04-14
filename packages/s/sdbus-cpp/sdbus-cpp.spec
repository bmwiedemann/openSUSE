#
# spec file for package sdbus-cpp
#
# Copyright (c) 2021 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2021 Luca Boccassi <bluca@debian.org>
# Copyright (c) 2020-2021 RedHat Inc.
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

%global version_major 0
%global version_minor 8
%global version_micro 3

Name:           sdbus-cpp
Version:        %{version_major}.%{version_minor}.%{version_micro}
Release:        0
Summary:        High-level C++ D-Bus library
License:        LGPL-2.1-only
Group:          Development/Libraries/C and C++

URL:            https://github.com/Kistler-Group/sdbus-cpp
Source0:        %{url}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
# https://github.com/Kistler-Group/sdbus-cpp/pull/171
Patch0:         0001-Find-and-link-against-pthread.patch

BuildRequires:  cmake >= 3.12
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(libsystemd) >= 236

%description
High-level C++ D-Bus library for Linux designed to provide easy-to-use
yet powerful API in modern C++

%package -n libsdbus-c++0
Summary:        Shared library for %{name}
Group:          Development/Libraries/C and C++

%description -n libsdbus-c++0
Shared library files for %{name}.

%package devel
Summary:        Development files for %{name}
Group:          Development/Libraries/C and C++
Requires:       libsdbus-c++0 = %{version}

%description devel
CMake, pkg-config, headers and other development files for %{name}.

%package devel-doc
Summary:        Developer documentation for %{name}
Group:          Development/Libraries/C and C++
BuildArch:      noarch
BuildRequires:  doxygen

%description devel-doc
READMEs and generated doxygen documentation for %{name}

%package xml2cpp
Summary:        Stub code generator for sdbus-c++
Group:          Development/Libraries/C and C++
Requires:       libsdbus-c++0 = %{version}
BuildRequires:  pkgconfig(expat)

%description xml2cpp
The stub code generator for generating the adapter and proxy interfaces
out of the D-Bus IDL XML description.


%prep
%autosetup -n %{name}-%{version}

%build
%cmake . \
    -DCMAKE_INSTALL_DOCDIR=/usr/share/doc/packages/sdbus-c++ \
    -DCMAKE_BUILD_TYPE=Release \
    -DBUILD_CODE_GEN=ON \
    -DBUILD_DOXYGEN_DOC=ON
%cmake_build
%cmake_build doc

%install
%cmake_install


%post -n libsdbus-c++0 -p /sbin/ldconfig

%postun -n libsdbus-c++0 -p /sbin/ldconfig

%files -n libsdbus-c++0
%license %{_docdir}/sdbus-c++/COPYING
%{_libdir}/libsdbus-c++.so.%{version_major}
%{_libdir}/libsdbus-c++.so.%{version}

%files devel
%dir %{_libdir}/cmake/sdbus-c++
%dir %{_docdir}/sdbus-c++
%doc %{_docdir}/sdbus-c++/AUTHORS
%doc %{_docdir}/sdbus-c++/ChangeLog
%doc %{_docdir}/sdbus-c++/NEWS
%doc %{_docdir}/sdbus-c++/README
%{_libdir}/cmake/sdbus-c++/*.cmake
%{_libdir}/pkgconfig/sdbus-c++.pc
%{_libdir}/libsdbus-c++.so
%{_includedir}/*

%files devel-doc
%dir %{_docdir}/sdbus-c++
%dir %{_docdir}/sdbus-c++/html
%doc %{_docdir}/sdbus-c++/html/*
%doc %{_docdir}/sdbus-c++/README.md
%doc %{_docdir}/sdbus-c++/sdbus-c++-class-diagram.png
%doc %{_docdir}/sdbus-c++/sdbus-c++-class-diagram.uml
%doc %{_docdir}/sdbus-c++/systemd-dbus-config.md
%doc %{_docdir}/sdbus-c++/using-sdbus-c++.md

%files xml2cpp
%{_bindir}/sdbus-c++-xml2cpp

%changelog
