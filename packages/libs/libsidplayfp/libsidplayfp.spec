#
# spec file for package libsidplayfp
#
# Copyright (c) 2024 SUSE LLC
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


%define soname 6
%define stilview_soname 0
Name:           libsidplayfp
Version:        2.8.0
Release:        0
Summary:        A library to play Commodore 64 music
License:        GPL-2.0-or-later
Group:          System/Libraries
#Git-Clone:     https://github.com/libsidplayfp/libsidplayfp.git
URL:            https://sourceforge.net/projects/sidplay-residfp/
Source0:        https://sourceforge.net/projects/sidplay-residfp/files/libsidplayfp/2.8/libsidplayfp-%{version}.tar.gz
BuildRequires:  gcc-c++
BuildRequires:  libgcrypt-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libftdi1)

%description
A library to play Commodore 64 music based on libsidplay2.

%package -n libsidplayfp%{soname}
Summary:        A library to play Commodore 64 music
Group:          System/Libraries

%description -n libsidplayfp%{soname}
A library to play Commodore 64 music based on libsidplay2.

%package devel
Summary:        Development files for libsidplayfp
Group:          Development/Libraries/C and C++
Requires:       libsidplayfp%{soname} = %{version}

%description devel
This package contains headers and libraries required to build applications that
use libsidplayfp.

%package -n libstilview%{stilview_soname}
Summary:        A library to play Commodore 64 music
Group:          System/Libraries

%description -n libstilview%{stilview_soname}
A library to play Commodore 64 music based on libsidplay2.

%package -n libstilview-devel
Summary:        Development files for libstilview
Group:          Development/Libraries/C and C++
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
%ifarch aarch64
EXTRA="--with-simd=neon"
%endif

%configure --disable-static $EXTRA
%make_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%ldconfig_scriptlets -n libsidplayfp%{soname}
%ldconfig_scriptlets -n libstilview%{stilview_soname}

%check

%files -n libsidplayfp%{soname}
%license COPYING
%{_libdir}/libsidplayfp.so.%{soname}*

%files -n libstilview%{stilview_soname}
%license COPYING
%{_libdir}/libstilview.so.%{stilview_soname}*

%files devel
%doc AUTHORS NEWS README TODO
%{_libdir}/libsidplayfp.so
%{_includedir}/sidplayfp/
%{_libdir}/pkgconfig/libsidplayfp.pc

%files -n libstilview-devel
%doc AUTHORS NEWS README TODO
%{_libdir}/libstilview.so
%{_includedir}/stilview/
%{_libdir}/pkgconfig/libstilview.pc

%changelog
