#
# spec file for package qalculate
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

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


%define major   21
%define libname libqalculate
Name:           qalculate
Version:        3.4.0
Release:        0
Summary:        Multi-purpose desktop calculator application
License:        GPL-2.0-or-later
Group:          Productivity/Scientific/Math
URL:            https://qalculate.github.io/
Source:         https://github.com/Qalculate/libqalculate/releases/download/v%{version}/%{libname}-%{version}.tar.gz
BuildRequires:  gcc-c++
BuildRequires:  gmp-devel
BuildRequires:  intltool
BuildRequires:  libxml2-devel
BuildRequires:  mpfr-devel
BuildRequires:  perl-XML-Parser
BuildRequires:  pkgconfig
BuildRequires:  readline-devel
BuildRequires:  pkgconfig(icu-uc)
BuildRequires:  pkgconfig(libcurl)
Requires:       %{name}-data >= %{version}

%description
Qalculate is a multi-purpose desktop calculator. Features include
customizable functions, units, arbitrary precision, plotting, and a
graphical interface that uses a one-line fault-tolerant expression
entry (although it supports optional traditional buttons).
This is the commandline interface, named qalc.

%package -n %{libname}%{major}
Summary:        Calulator Library
Group:          System/Libraries
Recommends:     %{name}-data >= %{version}
Provides:       %{libname} = %{version}

%description -n %{libname}%{major}
Qalculate is a multi-purpose desktop calculator. Features include
customizable functions, units, arbitrary precision, plotting, and a
graphical interface that uses a one-line fault-tolerant expression
entry.
This is the shared library package.

%package data
Summary:        Additional data for the qalculator calulator library
Group:          Productivity/Scientific/Math
Requires:       %{libname} = %{version}
Provides:       %{name}:%{_datadir}/%{name}/units.xml
# Files were split out into -data with 2.6.2
Conflicts:      %{name} < 2.6.2
BuildArch:      noarch

%description data
Qalculate is a multi-purpose desktop calculator. Features include
customizable functions, units, arbitrary precision, plotting, and a
graphical interface that uses a one-line fault-tolerant expression
entry.
This provides definitions of additional units, functions, etc. on top
of the built-in ones.

%package -n %{libname}-devel
Summary:        Header files, libraries and development documentation for %{libname}
Group:          Development/Libraries/C and C++
Requires:       %{libname} = %{version}
Requires:       gmp-devel
Requires:       libxml2-devel
Requires:       mpfr-devel

%description -n %{libname}-devel
This package contains the header files and development
documentation for %{libname}. If you like to develop programs using %{libname},
you will need to install %{libname}-devel.

%prep
%setup -q -n %{libname}-%{version}

%build
%configure --disable-static
make %{?_smp_mflags}

%install
%make_install
%find_lang libqalculate
find %{buildroot} -type f -name "*.la" -delete -print

%post -n %{libname}%{major} -p /sbin/ldconfig
%postun -n %{libname}%{major} -p /sbin/ldconfig

%files -f libqalculate.lang
%license COPYING
%doc README ChangeLog INSTALL AUTHORS TODO
%{_bindir}/qalc
%{_datadir}/doc/%{libname}
%{_mandir}/man1/qalc.1%{?ext_man}

%files -n %{name}-data
%{_datadir}/%{name}

%files -n %{libname}%{major}
%license COPYING
%{_libdir}/%{libname}.so.%{major}
%{_libdir}/%{libname}.so.%{major}.*

%files -n %{libname}-devel
%license COPYING
%{_includedir}/%{libname}
%{_libdir}/%{libname}.so
%{_libdir}/pkgconfig/%{libname}.pc

%changelog
