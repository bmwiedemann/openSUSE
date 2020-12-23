#
# spec file for package libxml++
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


Name:           libxml++
Version:        3.2.2
Release:        0
Summary:        C++ Interface for XML Files
License:        LGPL-2.1-or-later
Group:          Development/Libraries/C and C++
URL:            https://libxmlplusplus.github.io/libxmlplusplus
Source0:        https://download.gnome.org/sources/libxml++/3.2/%{name}-%{version}.tar.xz
Source1:        baselibs.conf

BuildRequires:  c++_compiler
BuildRequires:  fdupes
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(glibmm-2.4) >= 2.32.0
BuildRequires:  pkgconfig(libxml-2.0) >= 2.7.7

%description
libXML++ provides a C++ interface for XML files. It presently uses
libxml2 to access the XML files.

%package -n libxml++-3_0-1
Summary:        C++ Interface for XML Files
Group:          Development/Libraries/C and C++
Provides:       %{name} = %{version}
Obsoletes:      %{name} < %{version}

%description -n libxml++-3_0-1
libXML++ provides a C++ interface for XML files. It presently uses
libxml2 to access the XML files.

%package devel
Summary:        C++ Interface for XML Files -- Development Files
Group:          Development/Libraries/C and C++
Requires:       glibmm2-devel
Requires:       libxml++-3_0-1 = %{version}

%description devel
This package contains all necessary include files and libraries needed
to develop applications that require these.

%prep
%autosetup -p1

%build
%meson \
	%{nil}
%meson_build

%install
%meson_install
%fdupes %{buildroot}/%{_prefix}

%post -n libxml++-3_0-1 -p /sbin/ldconfig
%postun -n libxml++-3_0-1 -p /sbin/ldconfig

%files -n libxml++-3_0-1
%license COPYING
%doc AUTHORS ChangeLog NEWS README
%{_libdir}/*.so.*

%files devel
%{_includedir}/libxml++-3.0
%dir %{_libdir}/libxml++-3.0
%dir %{_libdir}/libxml++-3.0/include
%{_libdir}/libxml++-3.0/include/*.h
%{_libdir}/pkgconfig/*.pc
%{_libdir}/*.so

%changelog
