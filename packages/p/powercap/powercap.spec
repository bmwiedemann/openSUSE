#
# spec file for package powercap
#
# Copyright (c) 2022 SUSE LLC
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


Name:           powercap
Version:        0.6.0
Release:        0
Summary:        Tools for the Linux Power Capping Framework
License:        GPL-2.0-only
Group:          System/Monitoring
URL:            https://github.com/powercap/powercap
Source0:        https://github.com/powercap/powercap/archive/v%{version}.tar.gz
BuildRequires:  c++_compiler
BuildRequires:  cmake

%description
This project provides the powercap library -- a generic C interface to the
Linux power capping framework (sysfs interface). It includes an implementation
for working with Intel Running Average Power Limit (RAPL).

It also provides the following applications:

powercap-info - view powercap control type hierarchies or zone/constraint-specific configurations
powercap-set - set powercap control type zone/constraint-specific configurations

%package devel
Summary:        development files for the Linux Power Capping Framework
Requires:       %{name} = %{version}

%description devel
This project provides the powercap library -- a generic C interface to the
Linux power capping framework (sysfs interface). It includes an implementation
for working with Intel Running Average Power Limit (RAPL).

This package provides the devel files.

%prep
%setup -q

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}-set
%{_bindir}/%{name}-info
%{_bindir}/rapl-info
%{_bindir}/rapl-set
%{_mandir}/man1/powercap-info.1%{?ext_man}
%{_mandir}/man1/powercap-set.1%{?ext_man}
%{_mandir}/man1/rapl-info.1%{?ext_man}
%{_mandir}/man1/rapl-set.1%{?ext_man}
%{_libdir}/libpowercap.so.*

%files devel
%{_includedir}/powercap
%{_libdir}/pkgconfig/powercap.pc
%{_libdir}/libpowercap.so
%{_libdir}/cmake/powercap

%changelog
