#
# spec file for package libxml++
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


%define so_ver  5_0-1
%define base_ver 5.0

Name:           libxml++
Version:        5.2.1
Release:        0
Summary:        C++ Interface for XML Files
License:        LGPL-2.1-or-later
Group:          Development/Libraries/C and C++
URL:            https://libxmlplusplus.github.io/libxmlplusplus
Source0:        https://download.gnome.org/sources/libxml++/5.2/%{name}-%{version}.tar.xz

BuildRequires:  c++_compiler
BuildRequires:  fdupes
BuildRequires:  meson >= 0.60.0
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libxml-2.0) >= 2.7.7

%description
libXML++ provides a C++ interface for XML files. It presently uses
libxml2 to access the XML files.

%package -n libxml++-%{so_ver}
Summary:        C++ Interface for XML Files
Group:          Development/Libraries/C and C++
Provides:       %{name} = %{version}
Obsoletes:      %{name} < %{version}

%description -n libxml++-%{so_ver}
libXML++ provides a C++ interface for XML files. It presently uses
libxml2 to access the XML files.

%package devel
Summary:        C++ Interface for XML Files -- Development Files
Group:          Development/Libraries/C and C++
Requires:       libxml++-%{so_ver} = %{version}

%description devel
This package contains all necessary include files and libraries needed
to develop applications that require these.

%prep
%autosetup -p1
chmod -x NEWS libxml++config.h.in libxml++config.h.meson

%build
%meson \
	%{nil}
%meson_build

%install
%meson_install
%fdupes %{buildroot}%{_prefix}

%ldconfig_scriptlets -n libxml++-%{so_ver}

%check
%meson_test

%files -n libxml++-%{so_ver}
%license COPYING
%{_libdir}/*.so.*

%files devel
%doc ChangeLog NEWS README.md
%{_includedir}/libxml++-%{base_ver}
%dir %{_libdir}/libxml++-%{base_ver}
%dir %{_libdir}/libxml++-%{base_ver}/include
%{_libdir}/libxml++-%{base_ver}/include/*.h
%{_libdir}/pkgconfig/*.pc
%{_libdir}/*.so

%changelog
