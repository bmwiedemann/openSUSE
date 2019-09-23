#
# spec file for package libcdr
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define libname libcdr-0_1-1
Name:           libcdr
Version:        0.1.4
Release:        0
Summary:        Library for parsing the Corel Draw file format structure
License:        MPL-2.0
Group:          Productivity/Publishing/Word
Url:            http://www.freedesktop.org/wiki/Software/libcdr
Source0:        http://dev-www.libreoffice.org/src/%{name}/%{name}-%{version}.tar.xz
Patch0:         libcdr-0.1.1-pkgconfig.patch
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  xz
BuildRequires:  pkgconfig(cppunit)
BuildRequires:  pkgconfig(icu-i18n)
BuildRequires:  pkgconfig(lcms2)
BuildRequires:  pkgconfig(librevenge-0.0)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(zlib)
%if 0%{?suse_version} > 1325
BuildRequires:  libboost_headers-devel
%else
BuildRequires:  boost-devel
%endif

%description
libcdr is a library and a set of tools for reading and converting
binary files produced by Corel Draw.

%package -n %{libname}
Summary:        Library for parsing the Corel Draw file format structure
Group:          System/Libraries

%description -n %{libname}
libcdr is a library for parsing the Corel Draw file format structure.

%package devel
Summary:        Files for Developing with libcdr
Group:          Development/Libraries/C and C++
Requires:       %{libname} = %{version}

%description devel
libcdr is a library for parsing the Corel Draw file format structure.

This package contains the libcdr development files.

%package devel-doc
Summary:        Documentation for the libcdr API
Group:          Documentation/HTML
BuildArch:      noarch

%description devel-doc
This package contains documentation for the libcdr API.

%package tools
Summary:        Tools to work with documents in Corel Draw file format
Group:          Productivity/Publishing/Word

%description tools
Tools to work with documents in Corel Draw file format.

%prep
%setup -q
%patch0 -p1

%build
export CXXFLAGS="%{optflags} -fvisibility-inlines-hidden"
%configure \
    --disable-werror \
    --disable-static \
    --docdir=%{_docdir}/%{name} \
    --disable-silent-rules
make %{?_smp_mflags}

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print
# documentation
mkdir -p %{buildroot}%{_docdir}/%{name}
cp -p AUTHORS COPYING.* ChangeLog %{buildroot}%{_docdir}/%{name}

%fdupes -s %{buildroot}

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files -n %{libname}
%{_libdir}/*.so.*

%files devel
%{_libdir}/*.so
%{_libdir}/pkgconfig/libcdr*.pc
%{_includedir}/libcdr-*

%files devel-doc
%doc %dir %{_docdir}/%{name}
%doc %{_docdir}/%{name}/html

%files tools
%{_bindir}/*
%doc %dir %{_docdir}/%{name}
%doc %{_docdir}/%{name}/[A-Z]*

%changelog
