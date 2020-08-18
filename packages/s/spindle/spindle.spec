#
# spec file for package spindle
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


%define ver 0.12.git.4815692
Name:           spindle
Version:        %{ver}
Release:        0
Summary:        Scalable shared library loading in HPC environments
License:        LGPL-2.1-only
URL:            https://computing.llnl.gov/projects/spindle
Source:         spindle-%{ver}.tar.gz
BuildRequires:  gcc-c++
#BuildRequires:  launchmon-devel
BuildRequires:  munge-devel
# 32 bits builds are not supported
ExcludeArch:    %ix86 s390 armv7l


%description
Spindle is a tool for improving the performance of dynamic library
and python loading in HPC environments.

%package devel
Summary:        Development files for spindle

%description devel
Spindle is a tool for improving the performance of dynamic library
and python loading in HPC environments.

This package contains the development files for spindle.

%prep
%setup -q -n spindle-%{ver}

%build
%configure --disable-testsuite --disable-static --libexecdir=%{_libdir}
%make_build

%install
%make_install

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%license COPYRIGHT
%doc README VERSION
%{_bindir}/spindle
%{_mandir}/man1/*
%{_libdir}/libspindle*.so.*
%{_libdir}/spindle/


%files devel
%{_includedir}/spindle*
%{_libdir}/libspindle*.so
%exclude %{_libdir}/libspindle*.la

%changelog
