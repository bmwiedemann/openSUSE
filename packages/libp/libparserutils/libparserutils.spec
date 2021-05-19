#
# spec file for package libparserutils
#
# Copyright (c) 2021 SUSE LLC
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
Name:           libparserutils
Version:        0.2.4
Release:        0
Summary:        A library for building efficient parsers
License:        MIT
URL:            https://www.netsurf-browser.org/projects/libparserutils/
Source:         http://download.netsurf-browser.org/libs/releases/%{name}-%{version}-src.tar.gz
Patch0:         libparserutils-optflags.patch
BuildRequires:  netsurf-buildsystem >= 1.1
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(check)

%description
LibParserUtils is a library for building efficient parsers, written in
C. It was developed as part of the NetSurf project.

Features:
* No mandatory dependencies (iconv() implementation optional for
  enhanced charset support)
* A number of built-in character set converters
* Mapping of character set names to/from MIB enum values
* UTF-8 and UTF-16 (host endian) support functions
* Various simple data structures (resizeable buffer, stack, vector)
* A UTF-8 input stream
* Simple C API
* Portable

LibParserUtils has the following built-in charset converters:
* UTF-8
* UTF-16 (platform-native endian)
* ISO-8859-n
* Windows-125n
* US-ASCII

%package -n libparserutils0
Summary:        A library for building efficient parsers

%description -n libparserutils0
LibParserUtils is a library for building efficient parsers, written in
C. It was developed as part of the NetSurf project.

%package devel
Summary:        Development files for %{name}
Requires:       libparserutils0 = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%global make_vars COMPONENT_TYPE=lib-shared PREFIX=%{_prefix} LIBDIR=%{_lib} Q= INCLUDEDIR=include CC=gcc BUILD_CC=gcc
%global build_vars OPTCFLAGS='%{optflags}' OPTLDFLAGS="$RPM_LD_FLAGS"

%prep
%setup -q
%patch0 -p1

%build
%make_build %{make_vars} %{build_vars}

%install
make install DESTDIR=%{buildroot} %{make_vars}

%post -n libparserutils0 -p /sbin/ldconfig
%postun -n libparserutils0 -p /sbin/ldconfig

%check
%make_build test %{make_vars}

%files -n libparserutils0
%license COPYING
%{_libdir}/%{name}.so.*

%files devel
%{_includedir}/parserutils
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/%{name}.pc

%changelog
