#
# spec file for package neatvnc
#
# Copyright (c) 2020 SUSE LLC
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


Name:           neatvnc
Version:        0.3.2
Release:        0
Summary:        A VNC server library
License:        ISC
Group:          System/GUI/Other
URL:            https://github.com/any1/neatvnc
Source0:        https://github.com/any1/neatvnc/archive/v%{version}.tar.gz
BuildRequires:  aml-devel
BuildRequires:  libdrm-devel
BuildRequires:  libgnutls-devel
BuildRequires:  libjpeg8-devel
BuildRequires:  libpixman-1-0-devel
BuildRequires:  libuv-devel
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  zlib-devel

%description
This is a VNC server library.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Libraries/C and C++
Requires:       libneatvnc0 = %{version}

%description    devel
Development files and headers for %{name}.

%package -n     libneatvnc0
Summary:        A VNC server library
Group:          System/Libraries

%description -n libneatvnc0
A VNC server library.

%prep
%autosetup -p1

%build
%meson

%meson_build

%install
%meson_install

%post -n libneatvnc0 -p /sbin/ldconfig
%postun -n libneatvnc0 -p /sbin/ldconfig

%files devel
%license COPYING
%doc README.md
%{_includedir}/neatvnc.h
%{_libdir}/libneatvnc.so
%{_libdir}/pkgconfig/neatvnc.pc

%files -n libneatvnc0
%{_libdir}/libneatvnc.so.0
%{_libdir}/libneatvnc.so.0.0.0

%changelog
