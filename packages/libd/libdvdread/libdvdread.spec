#
# spec file for package libdvdread
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


%define sover   8
Name:           libdvdread
Version:        7.0.1
Release:        0
Summary:        Library for Reading DVD Video Images
License:        GPL-2.0-or-later
URL:            https://www.videolan.org/developers/libdvdnav.html
Source0:        https://download.videolan.org/videolan/%{name}/%{version}/%{name}-%{version}.tar.xz
Source1:        https://download.videolan.org/videolan/%{name}/%{version}/%{name}-%{version}.tar.xz.asc
Source2:        %{name}.keyring
Source3:        baselibs.conf
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(openssl)

%description
This package contains shared libraries for accessing DVD images (this
package does not contain DeCSS algorithms).

%package -n libdvdread%{sover}
Summary:        Library for Reading DVD Video Images
Provides:       %{name} = %{version}
Obsoletes:      %{name} <= 0.9.7

%description -n libdvdread%{sover}
This package contains shared libraries for accessing DVD images (this
package does not contain DeCSS algorithms).

%package devel
Summary:        Development Environment for libdvdread
Requires:       glibc-devel
Requires:       libdvdread%{sover} = %{version}

%description devel
This package contains the include-files and static libraries for
libdvdread.

%prep
%autosetup

%build
%meson -Dlibdvdcss=disabled -Ddefault_library=shared
%meson_build

%install
%meson_install --tags runtime,devel

%post   -n libdvdread%{sover} -p /sbin/ldconfig
%postun -n libdvdread%{sover} -p /sbin/ldconfig

%files -n libdvdread%{sover}
%license COPYING
%doc AUTHORS NEWS README.md
%{_libdir}/libdvdread.so.%{sover}
%{_libdir}/libdvdread.so.%{sover}.*

%files devel
%{_includedir}/dvdread
%{_libdir}/libdvdread.so
%{_libdir}/pkgconfig/dvdread.pc

%changelog
