#
# spec file for package libmspub
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


%define libname libmspub-0_1-1
Name:           libmspub
Version:        0.1.4
Release:        0
Summary:        Microsoft Publisher file format parser library
License:        MPL-2.0
Group:          Productivity/Publishing/Word
Url:            https://wiki.documentfoundation.org/DLP/Libraries/libmspub
Source:         http://dev-www.libreoffice.org/src/libmspub/libmspub-%{version}.tar.xz
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  xz
BuildRequires:  pkgconfig(icu-i18n)
BuildRequires:  pkgconfig(librevenge-0.0)
BuildRequires:  pkgconfig(librevenge-generators-0.0)
BuildRequires:  pkgconfig(librevenge-stream-0.0)
BuildRequires:  pkgconfig(zlib)
%if 0%{?suse_version} > 1325
BuildRequires:  libboost_headers-devel
%else
BuildRequires:  boost-devel
%endif

%description
libmspub is a library for parsing the Microsoft Publisher file format structure.

%package -n %{libname}
Summary:        Microsoft Publisher file format parser library
Group:          System/Libraries

%description -n %{libname}
libmspub is a library for parsing the Corel Draw file format structure. It is
cross-platform, at the moment it can be build on Microsoft Windows and Linux.

%package devel
Summary:        Files for Developing with libmspub
Group:          Development/Libraries/C and C++
Requires:       %{libname} = %{version}

%description devel
libmspub is a library for parsing the Microsoft Publisher file format structure.

This package contains the libmspub development files.

%package devel-doc
Summary:        Documentation for the libmspub API
Group:          Documentation/HTML
BuildArch:      noarch

%description devel-doc
This package contains documentation for the libmspub API.

%package tools
Summary:        Tools to work with publications in Microsoft Publisher file-format
Group:          Productivity/Publishing/Word

%description tools
Command line tools to work with publications in Microsoft Publisher file-format.

%prep
%setup -q

%build
export CXXFLAGS="%{optflags} -fvisibility-inlines-hidden"
%configure \
    --disable-silent-rules \
    --disable-werror \
    --disable-static \
    --docdir=%{_docdir}/%{name}
make %{?_smp_mflags}

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print
# docs have duped pictures
%fdupes %{buildroot}

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files -n %{libname}
%doc AUTHORS
%license COPYING.*
%{_libdir}/*.so.*

%files devel
%{_libdir}/*.so
%{_libdir}/pkgconfig/libmspub*.pc
%{_includedir}/libmspub-*

%files devel-doc
%dir %{_docdir}/%{name}
%doc %{_docdir}/%{name}/html

%files tools
%{_bindir}/*

%changelog
