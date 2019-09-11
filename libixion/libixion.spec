#
# spec file for package libixion
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


%define libname libixion-0_14-0
Name:           libixion
Version:        0.14.1
Release:        0
Summary:        Threaded multi-target formula parser & interpreter
License:        MIT
Group:          Productivity/Publishing/Word
Url:            https://gitlab.com/ixion/ixion
Source:         http://kohei.us/files/ixion/src/%{name}-%{version}.tar.xz
BuildRequires:  coreutils
BuildRequires:  gcc-c++
BuildRequires:  libstdc++-devel
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(mdds-1.4)
BuildRequires:  pkgconfig(python3)
%if 0%{?suse_version} > 1325
BuildRequires:  libboost_filesystem-devel
BuildRequires:  libboost_program_options-devel
BuildRequires:  libboost_system-devel
%else
BuildRequires:  boost-devel
%endif

%description
Ixion is a general purpose formula parser & interpreter that can calculate
multiple named targets, or "cells".

%package -n %{libname}
Summary:        Threaded multi-target formula parser & interpreter
Group:          System/Libraries

%description -n %{libname}
Ixion is a general purpose formula parser & interpreter that can calculate
multiple named targets, or "cells".

%package devel
Summary:        Threaded multi-target formula parser & interpreter
Group:          Development/Libraries/C and C++
Requires:       %{libname} = %{version}

%description devel
Ixion is a general purpose formula parser & interpreter that can calculate
multiple named targets, or "cells".

%package tools
Summary:        Spreadsheet file processing library
Group:          Productivity/Publishing/Word
Requires:       %{libname} = %{version}

%description tools
Tools to use ixion parser and interpreter from cli.

%package -n python3-%{name}
Summary:        Python bindings for libixion
Group:          Productivity/Publishing/Word
Obsoletes:      %{name}-python
# Renamed in 15.0
Provides:       %{name}-python3 = %{version}

%description -n python3-%{name}
Python 3 bindings for %{name}.

%prep
%setup -q

%build
%configure \
	--disable-silent-rules \
	--disable-static \
	--docdir=%{_docdir}/%{name}
make %{?_smp_mflags}

%check
make check %{?_smp_mflags}

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files -n %{libname}
%license LICENSE
%{_libdir}/*.so.*

%files devel
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc

%files tools
%{_bindir}/*

%files -n python3-%{name}
%{python3_sitearch}/ixion.so

%changelog
