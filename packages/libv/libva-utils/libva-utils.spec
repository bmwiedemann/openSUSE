#
# spec file for package libva-utils
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


Name:           libva-utils
Version:        2.9.1
Release:        0
Summary:        A collection of utilities and examples to exercise VA-API
License:        MIT AND EPL-1.0
Group:          Development/Tools/Other
URL:            https://github.com/intel/libva-utils
Source0:        %{url}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libdrm) >= 2.4
BuildRequires:  pkgconfig(libva) >= 1.1.0
BuildRequires:  pkgconfig(libva-drm)
BuildRequires:  pkgconfig(libva-wayland)
BuildRequires:  pkgconfig(libva-x11) >= 0.39.4
BuildRequires:  pkgconfig(wayland-client) >= 1.11.0
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xfixes)
Provides:       vaapi-tools = %{version}
Obsoletes:      vaapi-tools < %{version}
Provides:       vaapi-wayland-tools = %{version}
Obsoletes:      vaapi-wayland-tools < %{version}

%description
libva-utils is a collection of utilities and examples to exercise
VA-API in accordance with the libva project.
A driver implementation is necessary to properly operate.

%prep
%autosetup -p1

%build
%meson \
	-Ddrm=true \
	-Dx11=true \
	-Dwayland=true \
	-Dtests=false \
	%{nil}
%meson_build

%install
%meson_install

%files
%license COPYING
%doc NEWS
%{_bindir}/avcenc
%{_bindir}/avcstreamoutdemo
%{_bindir}/h264encode
%{_bindir}/jpegenc
%{_bindir}/loadjpeg
%{_bindir}/mpeg2vaenc
%{_bindir}/mpeg2vldemo
%{_bindir}/putsurface
%{_bindir}/putsurface_wayland
%{_bindir}/vainfo
%{_bindir}/vavpp
%{_bindir}/vp8enc
%{_bindir}/vp9enc
%{_bindir}/hevcencode
%{_bindir}/sfcsample
%{_bindir}/vppblending
%{_bindir}/vppchromasitting
%{_bindir}/vppdenoise
%{_bindir}/vppscaling_csc
%{_bindir}/vppscaling_n_out_usrptr
%{_bindir}/vppsharpness

%changelog
