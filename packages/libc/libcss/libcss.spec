#
# spec file for package libcss
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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
Name:           libcss
Version:        0.4.0
Release:        0
Summary:        A CSS parser and selection engine
License:        MIT
Group:          Development/Libraries/C and C++
Url:            http://www.netsurf-browser.org/projects/libcss/
Source:         http://download.netsurf-browser.org/libs/releases/%{name}-%{version}-src.tar.gz
BuildRequires:  check-devel
BuildRequires:  libparserutils-devel >= 0.2.0
BuildRequires:  libwapcaplet-devel >= 0.2.1
BuildRequires:  netsurf-buildsystem >= 1.1
BuildRequires:  pkg-config
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Patch:          libcss-buildopts.patch

%description
LibCSS is a CSS (Cascading Style Sheet) parser and selection engine,
written in C. It was developed as part of the NetSurf project.

%package -n libcss0
Summary:        A CSS parser and selection engine
Group:          System/Libraries

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
Group:          Development/Libraries/C and C++
Requires:       libcss0 = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -q
%patch -p1

%build
make %{?_smp_mflags} %{make_vars} %{build_vars}

%install
make install DESTDIR=%{buildroot} %{make_vars}

%post -n libcss0 -p /sbin/ldconfig

%postun -n libcss0 -p /sbin/ldconfig

%check
make %{?_smp_mflags} test %{make_vars}

%files -n libcss0
%defattr(-,root,root)
%{_libdir}/%{name}.so.*

%files devel
%defattr(-,root,root)
%doc docs/*
%doc COPYING README
%{_includedir}/%{name}
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/%{name}.pc

%changelog
