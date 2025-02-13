#
# spec file for package libzia
#
# Copyright (c) 2021 Walter Fey DL8FCL
# Copyright (c) 2022 Walter Fey DL8FCL
# Copyright (c) 2025 Andreas Stieger <Andreas.Stieger@gmx.de>
#
# This file is under MIT license
#
# Please submit bugfixes or comments via https://bugs.opensuse.org/
#

%define soname 4_67
Name:           libzia
Version:        4.67
Release:        0
Summary:        Libraries for tucnak
License:        GPL-2.0-or-later
Group:          Development/Libraries/C and C++
URL:            https://tucnak.nagano.cz
Source:         https://tucnak.nagano.cz/%{name}-%{version}.tar.gz
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(SDL2_ttf) >= 2.0.12
BuildRequires:  pkgconfig(glib-2.0) >= 2.30.0
BuildRequires:  pkgconfig(gnutls) >= 3.5.8
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.0.0
BuildRequires:  pkgconfig(libftdi1) >= 1.00
BuildRequires:  pkgconfig(libpng) >= 1.2.0
BuildRequires:  pkgconfig(sdl2) >= 2.0.5

%description
Libzia contains architecture-dependent code used by Tucnak and others.

%package -n %{name}-%{soname}
Summary:        Libraries for tucnak

%description -n %{name}-%{soname}
Libzia contains architecture-dependent code used by Tucnak and others.

This package contains the shared library.

%package devel
Summary:        Libzia header files
Group:          Development/Libraries/C and C++
Requires:       %{name}-%{soname} = %{version}

%description devel
Libzia contains architecture-dependent code used by Tucnak and others.

This package contains files needed for development with %{name}.

%prep
%autosetup -p1

%build
%configure \
	--disable-static \
	%{nil}
%make_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -print -delete

%check
%make_build check

%ldconfig_scriptlets -n %{name}-%{soname}

%files -n %{name}-%{soname}
%license COPYING
%{_libdir}/libzia-%{version}.so
%{_datadir}/libzia/

%files devel
%license COPYING
%{_bindir}/zia-config
%{_libdir}/libzia.so
%{_includedir}/libzia
%{_libdir}/pkgconfig/libzia.pc
%exclude %{_prefix}/lib/libzia

%changelog
