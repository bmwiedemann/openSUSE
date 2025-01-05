#
# spec file for package intel-vaapi-driver
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


Name:           intel-vaapi-driver
Version:        2.4.1
Release:        0
Summary:        Intel Driver for Video Acceleration (VA) API for Linux
License:        EPL-1.0 AND MIT
Group:          System/Libraries
URL:            https://github.com/intel/%{name}/
Source0:        %{name}-%{version}.tar.bz2
Source1:        %{name}-%{version}.tar.bz2.sha1sum
Source2:        baselibs.conf
Patch0:         https://patch-diff.githubusercontent.com/raw/intel/%{name}/pull/566.patch
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(libdrm) >= 2.4.45
BuildRequires:  pkgconfig(libdrm_intel)
BuildRequires:  pkgconfig(libva) >= 1.4.0
BuildRequires:  pkgconfig(libva-drm)
BuildRequires:  pkgconfig(libva-wayland)
BuildRequires:  pkgconfig(libva-x11) >= 0.39.4
BuildRequires:  pkgconfig(wayland-client) >= 1.11.0
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xfixes)

# Intel graphics hardware only available on these platforms
ExclusiveArch:  %ix86 x86_64
# due to pkg rename vaapi-intel-driver > intel-vaapi-driver
Provides:       vaapi-intel-driver = %{version}
Obsoletes:      vaapi-intel-driver < %{version}

%description
Intel Driver for Libva is a library providing the VA API video acceleration API.

%prep
%autosetup -p1

%build
%meson \
	-Dwith_x11=yes \
	-Dwith_wayland=yes \
	-Denable_hybrid_codec=true \
	-Denable_tests=false \
	%{nil}
%meson_build

%install
%meson_install

%files
%dir %{_libdir}/dri
%{_libdir}/dri/i965_drv_video.so

%changelog
