#
# spec file for package libabw
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


%define libname libabw-0_1-1
Name:           libabw
Version:        0.1.3
Release:        0
Summary:        Library for parsing the Abiword file format structure
License:        MPL-2.0
Group:          Productivity/Publishing/Word
URL:            https://wiki.documentfoundation.org/DLP/Libraries/libabw
Source0:        http://dev-www.libreoffice.org/src/%{name}/%{name}-%{version}.tar.xz
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  gperf
BuildRequires:  pkgconfig
BuildRequires:  xz
BuildRequires:  pkgconfig(librevenge-0.0)
BuildRequires:  pkgconfig(librevenge-generators-0.0)
BuildRequires:  pkgconfig(librevenge-stream-0.0)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(zlib)
%if 0%{?suse_version} > 1325
BuildRequires:  libboost_headers-devel
%else
BuildRequires:  boost-devel
%endif

%description
Libabw is library providing ability to interpret and import AbiWord documents
into various applications.

%package -n %{libname}
Summary:        Library for parsing the AbiWord file format structure
Group:          System/Libraries

%description -n %{libname}
Libabw is library providing ability to interpret and import AbiWord documents
into various applications.

%package devel
Summary:        Files for Developing with libabw
Group:          Development/Libraries/C and C++
Requires:       %{libname} = %{version}

%description devel
Libabw is library providing ability to interpret and import AbiWord documents
into various applications.

This package contains the libabw development files.

%package devel-doc
Summary:        Documentation for the libabw API
Group:          Documentation/HTML
BuildArch:      noarch

%description devel-doc
This package contains documentation for the libabw API.

%package tools
Summary:        Tools to work with documents in AbiWord file-format
Group:          Productivity/Publishing/Word

%description tools
This package contains tools to work with documents in AbiWord file-format.

%prep
%setup -q

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

cp -p COPYING.* ChangeLog %{buildroot}%{_docdir}/%{name}-devel/

%fdupes -s %{buildroot}

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files -n %{libname}
%license COPYING.*
%doc ChangeLog
%{_libdir}/*.so.*

%files devel
%doc %dir %{_docdir}/%{name}-devel/
%doc %{_docdir}/%{name}-devel/[A-Z]*
%{_libdir}/*.so
%{_libdir}/pkgconfig/libabw*.pc
%{_includedir}/libabw-*

%files devel-doc
%doc %{_docdir}/%{name}-devel/html/

%files tools
%license COPYING.*
%doc ChangeLog
%{_bindir}/*

%changelog
