#
# spec file for package libwapcaplet
#
# Copyright (c) 2014 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


%global make_vars COMPONENT_TYPE=lib-shared PREFIX=%{_prefix} LIBDIR=%{_lib} Q=
%global build_vars OPTCFLAGS='%{optflags}' OPTLDFLAGS="$RPM_LD_FLAGS"
Name:           libwapcaplet
Version:        0.2.1
Release:        0
Summary:        A string internment library
License:        MIT
Group:          System Environment/Libraries
Url:            http://www.netsurf-browser.org/projects/libwapcaplet/
Source:         http://download.netsurf-browser.org/libs/releases/%{name}-%{version}-src.tar.gz
BuildRequires:  check-devel
BuildRequires:  netsurf-buildsystem >= 1.1
BuildRequires:  pkg-config
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
LibWapcaplet is a string internment library, written in C. It provides
reference counted string interment and rapid string comparison
functionality. It was developed as part of the NetSurf project and is
available for use by other software under the MIT licence. For further
details, see the readme.

%package -n libwapcaplet0
Summary:        A string internment library
Group:          System Environment/Libraries

%description -n libwapcaplet0
LibWapcaplet is a string internment library, written in C. It provides
reference counted string interment and rapid string comparison
functionality. It was developed as part of the NetSurf project and is
available for use by other software under the MIT licence. For further
details, see the readme.

%package devel
Summary:        Development files for %{name}
Group:          Development/Libraries
Requires:       libwapcaplet0 = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -q

sed -i -e s@-Werror@@ Makefile

%build
make %{?_smp_mflags} %{make_vars} %{build_vars}

%install
make install DESTDIR=%{buildroot} %{make_vars}

%post -n libwapcaplet0 -p /sbin/ldconfig

%postun -n libwapcaplet0 -p /sbin/ldconfig

%check
# BUILDVARS disabled as optflags are too strict here
make %{?_smp_mflags} test %{make_vars}

%files -n libwapcaplet0
%defattr(-,root,root)
%{_libdir}/%{name}.so.*

%files devel
%defattr(-,root,root)
%{_includedir}/%{name}
%doc COPYING README
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/%{name}.pc

%changelog
