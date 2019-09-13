#
# spec file for package libxml++26
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define _name   libxml++
Name:           libxml++26
Version:        2.40.1
Release:        0
Summary:        C++ Interface for XML Files
License:        LGPL-2.1-or-later
Group:          Development/Libraries/C and C++
URL:            http://sourceforge.net/projects/libxmlplusplus/
Source:         http://download.gnome.org/sources/libxml++/2.40/%{_name}-%{version}.tar.xz
Source1:        baselibs.conf
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(glibmm-2.4) >= 2.32.0
BuildRequires:  pkgconfig(libxml-2.0) >= 2.7.7

%description
libXML++ provides a C++ interface for XML files. It presently uses
libxml2 to access the XML files.

%package -n libxml++-2_6-2
Summary:        C++ Interface for XML Files
Group:          Development/Libraries/C and C++

%description -n libxml++-2_6-2
libXML++ provides a C++ interface for XML files. It presently uses
libxml2 to access the XML files.

%package devel
Summary:        C++ Interface for XML Files -- Development Files
Group:          Development/Libraries/C and C++
Requires:       libxml++-2_6-2 = %{version}

%description devel
This package contains all necessary include files and libraries needed
to develop applications that require these.

%prep
%setup -q -n %{_name}-%{version}

%build
%configure --disable-static --with-pic
make %{?_smp_mflags}

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print
%fdupes %{buildroot}

%post -n libxml++-2_6-2 -p /sbin/ldconfig
%postun -n libxml++-2_6-2 -p /sbin/ldconfig

%files -n libxml++-2_6-2
%license COPYING
%doc AUTHORS ChangeLog NEWS README
%{_libdir}/*.so.*

%files devel
%{_includedir}/libxml++-2.6
%dir %{_libdir}/libxml++-2.6
%dir %{_libdir}/libxml++-2.6/include
%{_libdir}/libxml++-2.6/include/*.h
%{_libdir}/pkgconfig/*.pc
%{_libdir}/*.so
%{_datadir}/devhelp/books/libxml++-2.6/
%{_datadir}/doc/libxml++-2.6/
# Avoid BuildRequires on devhelp
%dir %{_datadir}/devhelp
%dir %{_datadir}/devhelp/books

%changelog
