#
# spec file for package CalcMySky
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


%if 0%{?suse_version} && 0%{?suse_version} < 1590
%global force_gcc_version 12
%endif

%define sover 15
%if 0%{?suse_version} > 1690
%define qtver 6
%else
%define qtver 5
%endif

Name:           CalcMySky
Version:        0.3.2
Release:        0
Summary:        Software package that simulates scattering of light by the atmosphere
License:        GPL-3.0-or-later
URL:            https://github.com/10110111/CalcMySky
Source:         https://github.com/10110111/CalcMySky/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  gcc%{?force_gcc_version}-c++ >= 12
BuildRequires:  libeigen3-devel >= 3.4.0
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(glm)
%if 0%{?suse_version} > 1550
BuildRequires:  pkgconfig(Qt6OpenGL)
BuildRequires:  pkgconfig(Qt6OpenGLWidgets)
BuildRequires:  pkgconfig(Qt6Widgets)
%else
BuildRequires:  pkgconfig(Qt5OpenGL)
BuildRequires:  pkgconfig(Qt5Widgets)
%endif

%description
CalcMySky is a software package that simulates scattering of light by the atmosphere to render daytime and twilight skies (without stars). Its primary purpose is to enable realistic view of the sky in applications such as planetaria. Secondary objective is to make it possible to explore atmospheric effects such as glories, fogbows etc., as well as simulate unusual environments such as on Mars or an exoplanet orbiting a star with a non-solar spectrum of radiation.

%package devel
Summary:        Development files for CalcMySky
Requires:       %{name} = %{version}

%description devel
Devel files needed by software that have to use CalcMySky (e.g. Stellarium >= 1.0)

%package -n libShowMySky-Qt%{qtver}-%{sover}
Summary:        ShowMySky library

%description -n libShowMySky-Qt%{qtver}-%{sover}
This package contains the library libShowMySky.

%package -n libShowMySky-Qt%{qtver}-devel
Summary:        Devel files for libShowMySky
Requires:       libShowMySky-Qt%{qtver}-%{sover} = %{version}
# fix packaging issue that was done when package was created
Provides:       libShowMySky-Qt6-14-devel = %{version}
Obsoletes:      libShowMySky-Qt6-14-devel < %{version}

%description -n libShowMySky-Qt%{qtver}-devel
This package contains the devel files for libShowMySky.

%prep
%autosetup -p1

%build
export CFLAGS="%{optflags} -fpie -fPIC"
export LDFLAGS="$LDFLAGS -pie"

%cmake \
%if 0%{?suse_version} > 1590
  -DQT_VERSION=6 \
%else
  -DQT_VERSION=5 \
%endif
%if 0%{?force_gcc_version}
    -DCMAKE_CXX_COMPILER=%{_bindir}/g++-%{?force_gcc_version} \
%endif
  -DCMAKE_CXX_STANDARD=17
%cmake_build

%install
%cmake_install

%post -n libShowMySky-Qt%{qtver}-%{sover} -p /sbin/ldconfig
%postun -n libShowMySky-Qt%{qtver}-%{sover} -p /sbin/ldconfig

%files
%license COPYING
%doc README.mdown
%{_bindir}/calcmysky
%{_bindir}/showmysky
%dir %{_datadir}/CalcMySky
%dir %{_datadir}/CalcMySky/shaders
%{_datadir}/CalcMySky/shaders/accumulate-single-scattering-texture.frag
%{_datadir}/CalcMySky/shaders/calc-view-dir.h.glsl
%{_datadir}/CalcMySky/shaders/common-functions.frag
%{_datadir}/CalcMySky/shaders/common-functions.h.glsl
%{_datadir}/CalcMySky/shaders/compute-direct-irradiance.frag
%{_datadir}/CalcMySky/shaders/compute-eclipsed-double-scattering.frag
%{_datadir}/CalcMySky/shaders/compute-eclipsed-single-scattering.frag
%{_datadir}/CalcMySky/shaders/compute-indirect-irradiance.frag
%{_datadir}/CalcMySky/shaders/compute-light-pollution-multiple-scattering.frag
%{_datadir}/CalcMySky/shaders/compute-light-pollution-single-scattering.frag
%{_datadir}/CalcMySky/shaders/compute-multiple-scattering.frag
%{_datadir}/CalcMySky/shaders/compute-scattering-density.frag
%{_datadir}/CalcMySky/shaders/compute-single-scattering.frag
%{_datadir}/CalcMySky/shaders/compute-transmittance-functions.h.glsl
%{_datadir}/CalcMySky/shaders/compute-transmittance.frag
%{_datadir}/CalcMySky/shaders/copy-scattering-texture-2d.frag
%{_datadir}/CalcMySky/shaders/copy-scattering-texture-3d.frag
%{_datadir}/CalcMySky/shaders/direct-irradiance.frag
%{_datadir}/CalcMySky/shaders/direct-irradiance.h.glsl
%{_datadir}/CalcMySky/shaders/eclipsed-direct-irradiance.frag
%{_datadir}/CalcMySky/shaders/eclipsed-direct-irradiance.h.glsl
%{_datadir}/CalcMySky/shaders/multiple-scattering-light-pollution.frag
%{_datadir}/CalcMySky/shaders/multiple-scattering-light-pollution.h.glsl
%{_datadir}/CalcMySky/shaders/multiple-scattering.frag
%{_datadir}/CalcMySky/shaders/multiple-scattering.h.glsl
%{_datadir}/CalcMySky/shaders/render.frag
%{_datadir}/CalcMySky/shaders/shader.geom
%{_datadir}/CalcMySky/shaders/shader.vert
%{_datadir}/CalcMySky/shaders/single-scattering-eclipsed.frag
%{_datadir}/CalcMySky/shaders/single-scattering-eclipsed.h.glsl
%{_datadir}/CalcMySky/shaders/single-scattering-light-pollution.frag
%{_datadir}/CalcMySky/shaders/single-scattering-light-pollution.h.glsl
%{_datadir}/CalcMySky/shaders/single-scattering.frag
%{_datadir}/CalcMySky/shaders/single-scattering.h.glsl
%{_datadir}/CalcMySky/shaders/texture-coordinates.frag
%{_datadir}/CalcMySky/shaders/texture-coordinates.h.glsl
%{_datadir}/CalcMySky/shaders/texture-sampling-functions.frag
%{_datadir}/CalcMySky/shaders/texture-sampling-functions.h.glsl
%{_datadir}/CalcMySky/shaders/version.h.glsl

%files -n libShowMySky-Qt%{qtver}-%{sover}
%{_libdir}/libShowMySky-Qt%{qtver}.so.%{sover}
%{_libdir}/libShowMySky-Qt%{qtver}.so.%{sover}.0.0

%files -n libShowMySky-Qt%{qtver}-devel
%{_libdir}/libShowMySky-Qt%{qtver}.so
%dir %{_libdir}/cmake/ShowMySky-Qt%{qtver}
%{_libdir}/cmake/ShowMySky-Qt%{qtver}/ShowMySky-Qt%{qtver}Config-relwithdebinfo.cmake
%{_libdir}/cmake/ShowMySky-Qt%{qtver}/ShowMySky-Qt%{qtver}Config.cmake

%files devel
%dir %{_includedir}/ShowMySky
%{_includedir}/ShowMySky/AtmosphereRenderer.hpp
%{_includedir}/ShowMySky/Exception.hpp
%{_includedir}/ShowMySky/Settings.hpp

%changelog
