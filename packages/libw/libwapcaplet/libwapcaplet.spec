#
# spec file for package libwapcaplet
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
Name:           libwapcaplet
Version:        0.4.3
Release:        0
Summary:        A string internment library
License:        MIT
URL:            https://www.netsurf-browser.org/projects/libwapcaplet/
Source:         http://download.netsurf-browser.org/libs/releases/%{name}-%{version}-src.tar.gz
BuildRequires:  netsurf-buildsystem >= 1.1
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(check)

%description
LibWapcaplet is a string internment library, written in C. It provides
reference counted string interment and rapid string comparison
functionality. It was developed as part of the NetSurf project and is
available for use by other software under the MIT licence. For further
details, see the readme.

%package -n libwapcaplet0
Summary:        A string internment library

%description -n libwapcaplet0
LibWapcaplet is a string internment library, written in C. It provides
reference counted string interment and rapid string comparison
functionality. It was developed as part of the NetSurf project and is
available for use by other software under the MIT licence. For further
details, see the readme.

%package devel
Summary:        Development files for %{name}
Requires:       libwapcaplet0 = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -q

sed -i -e s@-Werror@@ Makefile

%build
%make_build %{make_vars} %{build_vars}

%install
%make_install %{make_vars}

%post -n libwapcaplet0 -p /sbin/ldconfig
%postun -n libwapcaplet0 -p /sbin/ldconfig

%check
%make_build test %{make_vars} %{build_vars}

%files -n libwapcaplet0
%license COPYING
%{_libdir}/%{name}.so.*

%files devel
%{_includedir}/%{name}
%doc README
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/%{name}.pc

%changelog
