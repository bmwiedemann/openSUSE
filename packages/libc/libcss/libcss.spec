#
# spec file for package libcss
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
%global make_vars COMPONENT_TYPE=lib-shared PREFIX=%{_prefix} LIBDIR=%{_lib} CC=cc Q=
%global build_vars OPTCFLAGS='%{optflags}' OPTLDFLAGS="$RPM_LD_FLAGS"
Name:           libcss
Version:        0.9.1
Release:        0
Summary:        A CSS parser and selection engine
License:        MIT
URL:            https://www.netsurf-browser.org/projects/libcss/
Source:         http://download.netsurf-browser.org/libs/releases/%{name}-%{version}-src.tar.gz
Patch0:         libcss-buildopts.patch
Patch1:         fix-test-includes.patch
BuildRequires:  netsurf-buildsystem >= 1.1
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(check)
BuildRequires:  pkgconfig(libparserutils) >= 0.2.0
BuildRequires:  pkgconfig(libwapcaplet) >= 0.2.1

%description
LibCSS is a CSS (Cascading Style Sheet) parser and selection engine,
written in C. It was developed as part of the NetSurf project.

%package -n libcss0
Summary:        A CSS parser and selection engine

%description -n libcss0
LibCSS is a CSS (Cascading Style Sheet) parser and selection engine,
written in C. It was developed as part of the NetSurf project.

Features:
* Parses CSS, good and bad
* Simple C API
* Low memory usage
* Fast selection engine
* Portable

%package devel
Summary:        Development files for %{name}
Requires:       libcss0 = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -q
%autopatch -p1

%build
%make_build %{make_vars} %{build_vars}

%install
%make_install %{make_vars}

%check
%make_build test %{make_vars} %{build_vars}

%post -n libcss0 -p /sbin/ldconfig
%postun -n libcss0 -p /sbin/ldconfig

%files -n libcss0
%license COPYING
%{_libdir}/%{name}.so.*

%files devel
%doc docs/*
%doc README
%{_includedir}/%{name}
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/%{name}.pc

%changelog
