#
# spec file for package libetonyek
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


%{!?make_build:%global make_build make %{?_smp_mflags}}
%define libname libetonyek-0_1-1
Name:           libetonyek
Version:        0.1.10
Release:        0
Summary:        Library for Apple Keynote presentations
License:        MPL-2.0
Group:          Productivity/Publishing/Word
URL:            https://wiki.documentfoundation.org/DLP/Libraries/libetonyek
Source0:        http://dev-www.libreoffice.org/src/%{name}/%{name}-%{version}.tar.xz
Patch0:         resolve-ambiguities.patch
Patch1:         stdcxx17.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  glm-devel
BuildRequires:  gperf
BuildRequires:  help2man
BuildRequires:  liblangtag-devel
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  xz
BuildRequires:  pkgconfig(cppunit)
BuildRequires:  pkgconfig(librevenge-0.0)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(mdds-2.1)
BuildRequires:  pkgconfig(zlib)
%if 0%{?suse_version} > 1325
BuildRequires:  libboost_headers-devel
%else
BuildRequires:  boost-devel
%endif
%if 0%{?suse_version} < 1500
BuildRequires:  gcc7
BuildRequires:  gcc7-c++
%else
BuildRequires:  gcc >= 7
BuildRequires:  gcc-c++ >= 7
%endif

%description
Libetonyek is library providing ability to interpret and import Apple Keynote
presentations into various applications.

%package -n %{libname}
Summary:        Library for parsing the Apple Keynote presentations
Group:          System/Libraries

%description -n %{libname}
Libetonyek is library providing ability to interpret and import Apple Keynote
presentations into various applications.

%package devel
Summary:        Files for Developing with libetonyek
Group:          Development/Libraries/C and C++
Requires:       %{libname} = %{version}
Requires:       libwpd-devel

%description devel
Libetonyek is library providing ability to interpret and import Apple Keynote
presentations into various applications.

This package contains the libetonyek development files.

%package devel-doc
Summary:        Documentation for the libetonyek API
Group:          Documentation/HTML
BuildArch:      noarch

%description devel-doc
This package contains documentation for the libetonyek API.

%package tools
Summary:        Tools to work with Apple Keynote presentations
Group:          Productivity/Publishing/Word

%description tools
This package contains tools to work with Apple Keynote presentations

%prep
%autosetup -p1

%build
autoreconf -fvi
export CXXFLAGS="%{optflags} -fvisibility-inlines-hidden"
%if 0%{?suse_version} < 1500
export CC="gcc-7"
export CXX="g++-7"
%endif
%configure \
	--with-mdds="2.1" \
	--disable-silent-rules \
	--disable-werror \
	--disable-static \
	--docdir=%{_docdir}/%{name}-devel/html
%make_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

mkdir -p %{buildroot}%{_mandir}/man1
for i in %{buildroot}%{_bindir}/*; do
  LD_LIBRARY_PATH=%{buildroot}%{_libdir} \
  help2man -N -o %{buildroot}%{_mandir}/man1/$(basename $i).1 $i
done

cp -p AUTHORS COPYING ChangeLog %{buildroot}%{_docdir}/%{name}-devel/

%fdupes -s %{buildroot}

%check
%make_build check

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
%license COPYING
%doc AUTHORS ChangeLog
%{_bindir}/*
%{_mandir}/man1/*.1%{?ext_man}

%changelog
