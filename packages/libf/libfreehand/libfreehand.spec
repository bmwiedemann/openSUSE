#
# spec file for package libfreehand
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define libname libfreehand-0_1-1
Name:           libfreehand
Version:        0.1.2
Release:        0
Summary:        Library for import of FreeHand drawings
License:        MPL-2.0
Group:          Productivity/Publishing/Word
Url:            http://www.freedesktop.org/wiki/Software/libfreehand
Source0:        http://dev-www.libreoffice.org/src/%{name}/%{name}-%{version}.tar.xz
# PATCH-FIX-UPSTREAM icu-build-fix.patch: fix build with icu 65.1.
Patch0:         icu-build-fix.patch
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  gperf
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(cppunit)
BuildRequires:  pkgconfig(icu-i18n)
BuildRequires:  pkgconfig(lcms2)
BuildRequires:  pkgconfig(librevenge-0.0)
BuildRequires:  pkgconfig(zlib)
%if 0%{?suse_version} > 1325
BuildRequires:  libboost_headers-devel
%else
BuildRequires:  boost-devel
%endif

%description
Libfreehand is library providing ability to interpret and import Adobe/Macromedia
drawings into various applications. You can find it being used in libreoffice.

%package -n %{libname}
Summary:        Library for parsing the Adobe/Macromedia drawings
Group:          System/Libraries

%description -n %{libname}
Libfreehand is library providing ability to interpret and import Adobe/Macromedia
drawings into various applications. You can find it being used in libreoffice.

%package devel
Summary:        Files for Developing with libfreehand
Group:          Development/Libraries/C and C++
Requires:       %{libname} = %{version}

%description devel
Libfreehand is library providing ability to interpret and import Adobe/Macromedia
drawings into various applications. You can find it being used in libreoffice.

This package contains the libfreehand development files.

%package devel-doc
Summary:        Documentation for the libfreehand API
Group:          Documentation/HTML
BuildArch:      noarch

%description devel-doc
This package contains documentation for the libfreehand API.

%package tools
Summary:        Tools to work with Adobe/Macromedia drawings
Group:          Productivity/Publishing/Word

%description tools
This package contains tools to work with Adobe/Macromedia drawings.

%prep
%autosetup -p1

%build
export CXXFLAGS="%{optflags} -fvisibility-inlines-hidden"
%configure \
	--disable-silent-rules \
	--disable-werror \
	--disable-static \
	--docdir=%{_docdir}/%{name}-devel/html
make %{?_smp_mflags}

%install
%make_install

find %{buildroot} -type f -name "*.la" -delete -print

cp -p AUTHORS COPYING ChangeLog %{buildroot}%{_docdir}/%{name}-devel/

%fdupes -s %{buildroot}

%check
make %{?_smp_mflags} check

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files -n %{libname}
%{_libdir}/*.so.*

%files devel
%doc %dir %{_docdir}/%{name}-devel/
%doc %{_docdir}/%{name}-devel/[A-Z]*
%{_libdir}/*.so
%{_libdir}/pkgconfig/lib*.pc
%{_includedir}/%{name}-*

%files devel-doc
%doc %{_docdir}/%{name}-devel/html/

%files tools
%doc AUTHORS COPYING ChangeLog
%{_bindir}/*

%changelog
