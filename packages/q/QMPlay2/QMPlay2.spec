#
# spec file for package QMPlay2
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


%define __builder Ninja
%bcond_without qt6

%define _mtime 1718569701
%define _commit 935a51e

Name:           QMPlay2
Version:        24.06.16
Release:        0
Summary:        A Qt based media player, streamer and downloader
License:        LGPL-3.0-or-later
Group:          Productivity/Multimedia/Video/Players
URL:            https://github.com/zaps166/QMPlay2
Source:         %{name}-%{version}.%{_mtime}.%{_commit}.tar.gz
# PATCH-FEATURE-OPENSUSE 0001-add-opensuse-customizations.patch -- Fix python executable detection and add branding
Patch1:         0001-add-opensuse-customizations.patch
BuildRequires:  clang
BuildRequires:  cmake >= 3.16
BuildRequires:  llvm-gold
BuildRequires:  ninja
BuildRequires:  pkgconfig
BuildRequires:  shaderc
%if %{with qt6}
BuildRequires:  cmake(Qt6LinguistTools) >= 6.0.0
BuildRequires:  pkgconfig(Qt6Concurrent) >= 6.0.0
BuildRequires:  pkgconfig(Qt6Core5Compat) >= 6.0.0
BuildRequires:  pkgconfig(Qt6DBus) >= 6.0.0
BuildRequires:  pkgconfig(Qt6OpenGL) >= 6.0.0
BuildRequires:  pkgconfig(Qt6OpenGLWidgets) >= 6.0.0
BuildRequires:  pkgconfig(Qt6Qml) >= 6.0.0
BuildRequires:  pkgconfig(Qt6Svg) >= 6.0.0
BuildRequires:  pkgconfig(Qt6Widgets) >= 6.0.0
%else
BuildRequires:  cmake(Qt5LinguistTools) >= 5.15.2
BuildRequires:  pkgconfig(Qt5Concurrent) >= 5.15.2
BuildRequires:  pkgconfig(Qt5DBus) >= 5.15.2
BuildRequires:  pkgconfig(Qt5Qml) >= 5.15.2
BuildRequires:  pkgconfig(Qt5Svg) >= 5.15.2
BuildRequires:  pkgconfig(Qt5Widgets) >= 5.15.2
BuildRequires:  pkgconfig(Qt5X11Extras) >= 5.15.2
%endif
BuildRequires:  pkgconfig(SPIRV-Tools)
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(libass)
BuildRequires:  pkgconfig(libavcodec) >= 58.18.100
BuildRequires:  pkgconfig(libavdevice)
BuildRequires:  pkgconfig(libavformat) >= 58.12.100
BuildRequires:  pkgconfig(libavutil) >= 56.14.100
BuildRequires:  pkgconfig(libcddb)
BuildRequires:  pkgconfig(libcdio)
BuildRequires:  pkgconfig(libgme)
BuildRequires:  pkgconfig(libpipewire-0.3)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(libsidplayfp)
BuildRequires:  pkgconfig(libswresample) >= 3.1.100
BuildRequires:  pkgconfig(libswscale) >= 5.1.100
BuildRequires:  pkgconfig(libva)
BuildRequires:  pkgconfig(portaudio-2.0)
# Enable rubberband support on openSUSE Tumbleweed and openSUSE Leap 15.5, SLE15SP5+
%if 0%{?suse_version} >= 1550 || 0%{?sle_version} >= 150500
BuildRequires:  pkgconfig(rubberband) >= 3.0.0
%endif
BuildRequires:  pkgconfig(shaderc)
BuildRequires:  pkgconfig(taglib) >= 1.9
BuildRequires:  pkgconfig(vdpau)
BuildRequires:  pkgconfig(vulkan)
BuildRequires:  pkgconfig(xv)
Requires(post): hicolor-icon-theme
Requires(post): shared-mime-info
Requires(post): update-desktop-files
Requires(postun): hicolor-icon-theme
Requires(postun): shared-mime-info
Requires(postun): update-desktop-files
Recommends:     yt-dlp
Requires:       python3

%description
QMPlay2 is a video player, it can play and stream all formats supported by
ffmpeg and libmodplug (including J2B). It has an integrated Youtube
browser.

%package        devel
Summary:        %{name} development files
Group:          Development/Libraries/Other
Requires:       %{name} = %{version}
BuildArch:      noarch

%description    devel
It's a development package for %{name}.

%prep
%autosetup -p1 -n %{name}-%{version}.%{_mtime}.%{_commit}
# %setup -q -n %{name}-%{version}.%{_mtime}.%{_commit}
# %patch1 -p1

%build
# Build options
# - Force DWARFv4 as DWARFv5 is not fully supported by dwz yet
%cmake \
  -DCMAKE_C_COMPILER=clang \
  -DCMAKE_CXX_COMPILER=clang++ \
  -DCMAKE_C_FLAGS="${CFLAGS:-%optflags} -gdwarf-4" \
  -DCMAKE_CXX_FLAGS="${CXXFLAGS:-%optflags} -gdwarf-4" \
  -DSOLID_ACTIONS_INSTALL_PATH="%{_datadir}/solid/actions" \
  -DCMAKE_INTERPROCEDURAL_OPTIMIZATION=ON \
  -DUSE_PCH=ON \
  -DUSE_GIT_VERSION=OFF \
  -DCMAKE_INSTALL_PREFIX=%{_prefix} \
  -DCMAKE_INSTALL_LIBDIR=%{_libdir} \
  -DUSE_GLSLC=ON \
%if %{with qt6}
  -DBUILD_WITH_QT6=ON \
%else
  -DBUILD_WITH_QT6=OFF \
%endif
  -DUSE_PORTAUDIO=ON \
  -DUSE_PIPEWIRE=ON \
%if 0%{?suse_version} >= 1550 || 0%{?sle_version} >= 150500
  -DUSE_RUBBERBAND=ON \
%else
  -DUSE_RUBBERBAND=OFF \
%endif
  -DUSE_UPDATES=OFF

%ninja_build

%install
%ninja_install -C build

# Let's use %%doc macro. AUTHORS & ChangeLog are required for help window
cd %{buildroot}/%{_datadir}/qmplay2
rm LICENSE README.md

# WARNING: gzipped-svg-icon. Not all DE that support SVG icons support
# them gzipped (.svgz). Install the icon as plain uncompressed SVG.
gunzip -S svgz %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/%{name}.svgz
mv %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/%{name}.{,svg}

%post
/sbin/ldconfig
%desktop_database_post
%icon_theme_cache_post
%mime_database_post

%postun
/sbin/ldconfig
%desktop_database_postun
%icon_theme_cache_postun
%mime_database_postun

%files
%doc README.md
%license LICENSE
%{_bindir}/%{name}
%{_libdir}/qmplay2
%{_libdir}/libqmplay2.so
%{_datadir}/applications/%{name}*.desktop
%dir %{_datadir}/solid
%dir %{_datadir}/solid/actions
%{_datadir}/solid/actions/%{name}*.desktop
%dir %{_datadir}/metainfo/
%{_datadir}/metainfo/%{name}.appdata.xml
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_datadir}/qmplay2
%{_mandir}/man?/%{name}.?%{ext_man}
%{_datadir}/mime/packages/x-*.xml

%files devel
%{_includedir}/%{name}

%changelog
