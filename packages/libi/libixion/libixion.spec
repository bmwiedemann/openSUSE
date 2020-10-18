#
# spec file for package libixion
#
# Copyright (c) 2020 SUSE LLC
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


%define libname libixion-0_16-0
Name:           libixion
Version:        0.16.1
Release:        0
Summary:        Threaded multi-target formula parser & interpreter
License:        MIT
URL:            https://gitlab.com/ixion/ixion
Source:         http://kohei.us/files/ixion/src/%{name}-%{version}.tar.xz
BuildRequires:  coreutils
BuildRequires:  gcc-c++
BuildRequires:  libstdc++-devel
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(mdds-1.5)
BuildRequires:  pkgconfig(python3)
BuildRequires:  pkgconfig(spdlog) >= 0.16.0
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

%description -n %{libname}
Ixion is a general purpose formula parser & interpreter that can calculate
multiple named targets, or "cells".

%package devel
Summary:        Threaded multi-target formula parser & interpreter
Requires:       %{libname} = %{version}

%description devel
Ixion is a general purpose formula parser & interpreter that can calculate
multiple named targets, or "cells".

%package tools
Summary:        Spreadsheet file processing library
Requires:       %{libname} = %{version}

%description tools
Tools to use ixion parser and interpreter from cli.

%package -n python3-%{name}
Summary:        Python bindings for libixion
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
%make_build

%check
%make_build check

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
