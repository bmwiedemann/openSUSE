#
# spec file for package libodfgen
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


%{!?make_build:%global make_build make %{?_smp_mflags}}
%define libname libodfgen-0_1-1
Name:           libodfgen
Version:        0.1.8
Release:        0
Summary:        Library to generate ODF documents from libwpd's and libwpg's api calls
License:        LGPL-2.1-or-later AND MPL-2.0
Group:          Productivity/Publishing/Word
URL:            http://libwpd.sourceforge.net
Source:         https://downloads.sourceforge.net/project/libwpd/%{name}/%{name}-%{version}/%{name}-%{version}.tar.xz
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  xz
BuildRequires:  pkgconfig(librevenge-0.0)
BuildRequires:  pkgconfig(librevenge-stream-0.0)
BuildRequires:  pkgconfig(libxml-2.0)

%description
libodfgen is a general purpose library designed to generate ODF documents
from api calls to libwpd and libwpg libraries.

%package -n %{libname}
Summary:        Library to generate ODF documents from libwpd's and libwpg's api calls
Group:          System/Libraries

%description -n %{libname}
libodfgen is a general purpose library designed to generate ODF documents
from api calls to libwpd and libwpg libraries.

%package devel
Summary:        Library to generate ODF documents from libwpd's and libwpg's api calls
Group:          Development/Libraries/C and C++
Requires:       %{libname} = %{version}
Requires:       libstdc++-devel

%description devel
libodfgen is a general purpose library designed to generate ODF documents
from api calls to libwpd and libwpg libraries.

%package devel-doc
Summary:        Documentation for the libodfgen API
Group:          Documentation/HTML
BuildArch:      noarch

%description devel-doc
This package contains documentation for the libodfgen API.

%prep
%setup -q

%build
export CXXFLAGS="%{optflags} -fvisibility-inlines-hidden"
%configure \
	--disable-silent-rules \
	--disable-werror \
	--disable-static \
	--docdir=%{_docdir}/%{name}-devel/html \
	--with-sharedptr=c++11

%make_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%fdupes -s %{buildroot}

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files -n %{libname}
%{_libdir}/*.so.*
%doc ChangeLog
%license COPYING.LGPL
%license COPYING.MPL
%doc NEWS

%files devel
%{_libdir}/*.so
%{_libdir}/pkgconfig/libodfgen*.pc
%{_includedir}/libodfgen*

%files devel-doc
%dir %{_docdir}/%{name}-devel
%doc %{_docdir}/%{name}-devel/html/

%changelog
