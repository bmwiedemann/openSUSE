#
# spec file for package libad9361-iio
#
# Copyright (c) 2026 SUSE LLC and contributors
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


%define sover 0
%define libname libad9361
Name:           libad9361-iio
Version:        0.4.0
Release:        0
Summary:        Library for AD9361
# Legal-Review-Notice: LICENSE and COPYING.txt both carry the LGPL-2.1 text and
# every source file grants "version 2.1 of the License, or (at your option) any
# later version"; the bindings even declare SPDX-License-Identifier:
# LGPL-2.1-or-later. The GPL-3.0-only tag used before 0.4.0 was incorrect.
License:        LGPL-2.1-or-later
URL:            https://github.com/analogdevicesinc/libad9361-iio
Source:         %{url}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch0:         %{name}-lib-dir.patch
Patch1:         %{name}-link-libm.patch
BuildRequires:  cmake >= 3.5.0
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  pkgconfig
# Upstream still targets the libiio 0.x API, libiio >= 1.0 is not supported yet
BuildRequires:  pkgconfig(libiio)

%description
This is a simple library used for userspace, which manages multi-chip sync, on
platforms (FMCOMMS5) where multiple AD9361 devices are used.

%package -n %{libname}-%{sover}
Summary:        Library for AD9361

%description -n %{libname}-%{sover}
This is a simple library used for userspace, which manages multi-chip sync, on
platforms (FMCOMMS5) where multiple AD9361 devices are used.

%package devel
Summary:        Development files for libad9361
Requires:       %{libname}-%{sover} = %{version}

%description devel
This is a simple library used for userspace, which manages multi-chip sync, on
platforms (FMCOMMS5) where multiple AD9361 devices are used.

%package devel-doc
Summary:        Documentation for libad9361-iio
BuildArch:      noarch

%description devel-doc
Documentation for libad9361-iio library.

%prep
%autosetup -p1

%build
%cmake
%cmake_build

%install
%cmake_install

# Upstream forces its own documentation root, move it below %%{_docdir}
mkdir -p %{buildroot}%{_docdir}/%{name}
mv %{buildroot}%{_datadir}/doc/ad93610-doc/html %{buildroot}%{_docdir}/%{name}/
rmdir %{buildroot}%{_datadir}/doc/ad93610-doc

%fdupes -s %{buildroot}%{_docdir}

%check
# The remaining tests need a real AD936x device attached
%ctest --tests-regex '^(FilterDesignerTest|GenerateRatesTest)$'

%ldconfig_scriptlets -n %{libname}-%{sover}

%files -n %{libname}-%{sover}
%license LICENSE
%doc README.md
%{_libdir}/libad9361.so.%{sover}
%{_libdir}/libad9361.so.%{sover}.*

%files devel
%{_includedir}/ad9361.h
%{_libdir}/libad9361.so
%{_libdir}/pkgconfig/libad9361.pc

%files devel-doc
%dir %{_docdir}/%{name}
%{_docdir}/%{name}/html

%changelog
