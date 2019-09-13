#
# spec file for package libsoc
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


%define sover   2
Name:           libsoc
Version:        0.8.2
Release:        0
Summary:        C library for interfacing with common SoC peripherals
License:        LGPL-2.1
Group:          Development/Libraries/C and C++
Url:            https://jackmitch.github.io/libsoc/
Source0:        https://github.com/jackmitch/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  fdupes
BuildRequires:  i2c-tools
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(python3)

%description
libsoc is a C library to interface with common peripherals found in System
on Chips (SoC) through generic Linux Kernel interfaces.

%package -n %{name}%{sover}
Summary:        C library for interfacing with common SoC peripherals
Group:          System/Libraries
Recommends:     %{name}-common

%description -n %{name}%{sover}
libsoc is a C library to interface with common peripherals found in System
on Chips (SoC) through generic Linux Kernel interfaces.

It targets reliability rather than speed. No guarantees are made
on its determinism and it should not be used in time critical routines.

%package -n %{name}-common
Summary:        Common files for %{name}
Group:          Development/Languages/C and C++

%description -n %{name}-common
libsoc is a C library to interface with common peripherals found in System
on Chips (SoC) through generic Linux Kernel interfaces.

It targets reliability rather than speed. No guarantees are made
on its determinism and it should not be used in time critical routines.

This package contains common config files for %{name}.

%package -n python3-%{name}
Summary:        Python3 bindings for %{name}
Group:          Development/Languages/Python
Requires:       %{name}%{sover} = %{version}

%description -n python3-%{name}
libsoc is a C library to interface with common peripherals found in System
on Chips (SoC) through generic Linux Kernel interfaces.

This package contains python3 bindings for %{name}.

%package devel
Summary:        Development files for %{name}
Group:          Development/Languages/C and C++
Requires:       %{name}%{sover} = %{version}

%description devel
libsoc is a C library to interface with common peripherals found in System
on Chips (SoC) through generic Linux Kernel interfaces.

This package contains development files for %{name}.

%prep
%setup -q

%build
autoreconf -fiv
%configure \
  --enable-python=3 \
  --enable-static=no \
  --with-board-configs
make %{?_smp_mflags} V=1

%install
%make_install
%fdupes -s %{buildroot}%{python3_sitearch}
rm -rf %{buildroot}%{_libdir}/libsoc.la

%post -n %{name}%{sover} -p /sbin/ldconfig
%postun -n %{name}%{sover} -p /sbin/ldconfig

%files -n %{name}%{sover}
%defattr(-,root,root)
%doc LICENCE
%{_libdir}/%{name}.so.%{sover}*

%files -n %{name}-common
%defattr(-,root,root)
%{_datadir}/%{name}

%files devel
%defattr(-,root,root)
%{_includedir}/%{name}*.h
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/%{name}.pc

%files -n python3-%{name}
%defattr(-,root,root)
%{python3_sitearch}/*

%changelog
