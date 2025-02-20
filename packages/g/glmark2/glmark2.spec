#
# spec file for package glmark2
#
# Copyright (c) 2025 SUSE LLC
# Copyright (c) 2015-2016 Malcolm J Lewis <malcolmlewis@opensuse.org>
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


Name:           glmark2
Version:        20250212
Release:        0
Summary:        OpenGL 2.0 and ES 2.0 benchmark
License:        GPL-3.0-only
Group:          System/X11/Utilities
URL:            https://github.com/glmark2/glmark2
Source0:        %{name}-%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  gcc-c++ >= 5.0
BuildRequires:  libjpeg-devel
BuildRequires:  meson >= 0.45
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(gbm)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(glesv2)
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-egl)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(x11)

%description
A benchmark for OpenGL (ES) 2.0 that uses only the OpenGL ES 2.0 compatible
API. It contains tests for standard OpenGL (ES) 2.0 features, such as vertex
arrays, VBOs, texturing and shaders.

%prep
%autosetup

%build
%meson \
  -Dflavors=x11-gl,x11-glesv2,wayland-gl,wayland-glesv2,drm-gl,drm-glesv2
%meson_build

%install
%meson_install

%fdupes -s %{buildroot}

%files
%license COPYING COPYING.SGI
%doc NEWS
%{_bindir}/glmark2
%{_bindir}/glmark2-drm
%{_bindir}/glmark2-es2
%{_bindir}/glmark2-es2-drm
%{_bindir}/glmark2-es2-wayland
%{_bindir}/glmark2-wayland
%{_datadir}/%{name}
%{_mandir}/man1/glmark2.1%{?ext_man}
%{_mandir}/man1/glmark2-drm.1%{?ext_man}
%{_mandir}/man1/glmark2-es2.1%{?ext_man}
%{_mandir}/man1/glmark2-es2-drm.1%{?ext_man}
%{_mandir}/man1/glmark2-es2-wayland.1%{?ext_man}
%{_mandir}/man1/glmark2-wayland.1%{?ext_man}

%changelog
