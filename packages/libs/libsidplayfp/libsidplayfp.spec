#
# spec file for package libsidplayfp
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


%define soname 7
%define stilview_soname 0
Name:           libsidplayfp
Version:        3.0.2
Release:        0
Summary:        A library to play Commodore 64 music
License:        GPL-2.0-or-later
URL:            https://github.com/libsidplayfp/libsidplayfp
Source0:        https://github.com/libsidplayfp/libsidplayfp/releases/download/v%{version}/%{name}-%{version}.tar.gz
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libftdi1)
BuildRequires:  pkgconfig(libgcrypt)
BuildRequires:  pkgconfig(libresidfp)

%description
A library to play Commodore 64 music based on libsidplay2.

%package -n %{name}%{soname}
Summary:        A library to play Commodore 64 music

%description -n %{name}%{soname}
A library to play Commodore 64 music based on libsidplay2.

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{soname} = %{version}

%description devel
This package contains headers and libraries required to build applications that
use libsidplayfp.

%package -n libstilview%{stilview_soname}
Summary:        A library to play Commodore 64 music

%description -n libstilview%{stilview_soname}
A library to play Commodore 64 music based on libsidplay2.

%package -n libstilview-devel
Summary:        Development files for libstilview
Requires:       libstilview%{stilview_soname} = %{version}

%description -n libstilview-devel
This package contains headers and libraries required to build applications that
use libstilview.

%prep
%autosetup -p1

%build
%ifarch x86_64
EXTRA="--with-simd=none"
%endif

%configure --disable-static $EXTRA
%make_build

%install
%make_install
rm %{buildroot}%{_libdir}/{%{name},libstilview}.la

%ldconfig_scriptlets -n %{name}%{soname}
%ldconfig_scriptlets -n libstilview%{stilview_soname}

%files -n %{name}%{soname}
%license COPYING
%{_libdir}/%{name}.so.%{soname}*

%files -n libstilview%{stilview_soname}
%license COPYING
%{_libdir}/libstilview.so.%{stilview_soname}*

%files devel
%doc AUTHORS.md NEWS.md README.md
%{_libdir}/%{name}.so
%{_includedir}/sidplayfp
%{_libdir}/pkgconfig/%{name}.pc

%files -n libstilview-devel
%doc AUTHORS.md NEWS.md README.md
%{_libdir}/libstilview.so
%{_includedir}/stilview
%{_libdir}/pkgconfig/libstilview.pc

%changelog
