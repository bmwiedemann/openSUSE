#
# spec file for package glmark2
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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
Version:        0.0+git.20190708
Release:        0
Summary:        OpenGL 2.0 and ES 2.0 benchmark
License:        GPL-3.0-only
Group:          System/X11/Utilities
URL:            https://github.com/glmark2/glmark2
Source0:        %{name}-%{version}.tar.xz
BuildRequires:  ImageMagick
BuildRequires:  fdupes
BuildRequires:  libjpeg-devel
BuildRequires:  pkgconfig
BuildRequires:  python2-base
BuildRequires:  xz
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(gbm)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(glesv2)
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(libpng16)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(x11)
# Skip wayland on SLE
%if 0%{?is_opensuse}
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-egl)
%endif
# C++14 capable compiler is required
%if 0%{?suse_version} > 1320
BuildRequires:  gcc-c++ >= 5.0
%else
BuildRequires:  gcc7-c++
%endif

%description
A benchmark for OpenGL (ES) 2.0 that uses only the OpenGL ES 2.0 compatible
API. It contains tests for standard OpenGL (ES) 2.0 features, such as vertex
arrays, VBOs, texturing and shaders.

%prep
%setup -q

%build
%if 0%{?suse_version} < 1320
export CXX=g++-7
%endif
export CXXFLAGS="%{optflags}"
python2 waf configure \
  %if 0%{?is_opensuse}
  --with-flavors=x11-gl,x11-glesv2,wayland-gl,wayland-glesv2,drm-gl,drm-glesv2 \
  %else
  --with-flavors=x11-gl,x11-glesv2,drm-gl,drm-glesv2 \
  %endif
  --prefix=%{_prefix}
python2 waf --verbose %{?_smp_mflags}

%install
python2 waf install --destdir=%{buildroot}
#FIXME Clean up runtime warning - libpng warning: iCCP: known incorrect sRGB profile
pushd %{buildroot}%{_datadir}/%{name}/textures
convert effect-2d.png -strip effect-2d.png
popd
%fdupes -s %{buildroot}

%files
%license COPYING COPYING.SGI
%doc NEWS
%{_bindir}/glmark2
%{_bindir}/glmark2-drm
%{_bindir}/glmark2-es2
%{_bindir}/glmark2-es2-drm
%if 0%{?is_opensuse}
%{_bindir}/glmark2-es2-wayland
%{_bindir}/glmark2-wayland
%endif
%{_datadir}/%{name}
%{_mandir}/man1/glmark2.1%{?ext_man}
%{_mandir}/man1/glmark2-drm.1%{?ext_man}
%{_mandir}/man1/glmark2-es2.1%{?ext_man}
%{_mandir}/man1/glmark2-es2-drm.1%{?ext_man}
%if 0%{?is_opensuse}
%{_mandir}/man1/glmark2-es2-wayland.1%{?ext_man}
%{_mandir}/man1/glmark2-wayland.1%{?ext_man}
%endif

%changelog
