#
# spec file for package intel-hybrid-driver
#
# Copyright (c) 2020 SUSE LLC
# Copyright (c) 2017 Bjørn Lie, Bryne, Norway.
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


Name:           intel-hybrid-driver
Version:        1.0.2
Release:        0
Summary:        VA driver for Intel G45 & HD Graphics family
License:        MIT
URL:            https://github.com/intel/intel-hybrid-driver
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz
Patch0:         U_Update-the-dependency-to-libva-2.0.patch
Patch1:         n_libva-2.0-ABI-header-fix.patch
Patch2:         u_gcc10.patch

BuildRequires:  c++_compiler
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(libcmrt) >= 0.10.0
BuildRequires:  pkgconfig(libdrm) >= 2.4.45
BuildRequires:  pkgconfig(libva) >= 1.0.0
BuildRequires:  pkgconfig(libva-wayland)
BuildRequires:  pkgconfig(libva-x11)
BuildRequires:  pkgconfig(wayland-client)
# Obviously only for intel platform
ExclusiveArch:  %{ix86} x86_64 ia64

%description
This is the VA-API implementation for Intel G45 chipsets
and Intel HD Graphics for Intel Core processor family.

%prep
%autosetup -p1

%build
NOCONFIGURE=1 ./autogen.sh
%configure \
	--enable-drm \
	--enable-x11 \
	--enable-wayland \
	%{nil}
%make_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%license COPYING
%doc NEWS README
%dir %{_libdir}/dri
%{_libdir}/dri/hybrid_drv_video.so

%changelog
