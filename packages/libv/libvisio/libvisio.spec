#
# spec file for package libvisio
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


%define libname libvisio-0_1-1
Name:           libvisio
Version:        0.1.7
Release:        0
Summary:        Library for parsing the MS Visio file format structure
License:        MPL-2.0
Group:          Productivity/Publishing/Word
URL:            https://www.freedesktop.org/wiki/Software/libvisio
Source0:        http://dev-www.libreoffice.org/src/%{name}/%{name}-%{version}.tar.xz
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  gperf
BuildRequires:  help2man
BuildRequires:  pkgconfig
BuildRequires:  xz
BuildRequires:  pkgconfig(cppunit)
BuildRequires:  pkgconfig(icu-i18n)
BuildRequires:  pkgconfig(librevenge-0.0) >= 0.0.0
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(zlib)
%if 0%{?suse_version} > 1325
BuildRequires:  libboost_headers-devel
%else
BuildRequires:  boost-devel
%endif

%description
libvisio is a library for parsing the MS Visio file format structure. It is
cross-platform, at the moment it can be build on Microsoft Windows and Linux.

%package -n %{libname}
Summary:        Library for parsing the MS Visio file format structure
Group:          System/Libraries

%description -n %{libname}
libvisio is a library for parsing the MS Visio file format structure. It is
cross-platform, at the moment it can be build on Microsoft Windows and Linux.

%package devel
Summary:        Files for Developing with libvisio
Group:          Development/Libraries/C and C++
Requires:       %{libname} = %{version}

%description devel
libvisio is a library for parsing the MS Visio file format structure. It is
cross-platform, at the moment it can be build on Microsoft Windows and Linux.

This package contains the libvisio development files.

%package devel-doc
Summary:        Documentation for the libvisio API
Group:          Documentation/HTML
%if 0%{?suse_version} > 1200
BuildArch:      noarch
%endif

%description devel-doc
This package contains documentation for the libvisio API.

%package tools
Summary:        Tools to work with documents in MS Visio file-format
Group:          Productivity/Publishing/Word

%description tools
This package contains tools to work with documents in MS Visio file-format.

%prep
%setup -q

%build
export CXXFLAGS="%{optflags} -fvisibility-inlines-hidden"
%configure \
	--disable-werror \
	--disable-static \
	--disable-silent-rules \
	--docdir=%{_docdir}/%{name}-devel/html
make %{?_smp_mflags}

%install
%make_install

find %{buildroot} -type f -name "*.la" -delete -print

mkdir -p %{buildroot}%{_mandir}/man1
for i in %{buildroot}%{_bindir}/*; do
	LD_LIBRARY_PATH=%{buildroot}%{_libdir} \
	help2man -N -o %{buildroot}%{_mandir}/man1/$(basename $i).1 $i
done

cp -p AUTHORS COPYING.* ChangeLog %{buildroot}%{_docdir}/%{name}-devel/

%fdupes -s %{buildroot}

%check
make check %{?_smp_mflags}

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files -n %{libname}
%{_libdir}/*.so.*

%files devel
%doc %dir %{_docdir}/%{name}-devel/
%doc %{_docdir}/%{name}-devel/[A-Z]*
%{_libdir}/*.so
%{_libdir}/pkgconfig/libvisio*.pc
%{_includedir}/libvisio-*

%files devel-doc
%doc %{_docdir}/%{name}-devel/html/

%files tools
%license COPYING.*
%doc AUTHORS ChangeLog
%{_bindir}/*
%{_mandir}/man1/*.1%{?ext_man}

%changelog
