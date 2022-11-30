#
# spec file for package QMPlay2
#
# Copyright (c) 2022 SUSE LLC
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

Name:           QMPlay2
Version:        22.10.23
Release:        0
Summary:        A Qt based media player, streamer and downloader
License:        LGPL-3.0-or-later
Group:          Productivity/Multimedia/Video/Players
URL:            https://github.com/zaps166/QMPlay2
Source:         https://github.com/zaps166/QMPlay2/releases/download/%{version}/QMPlay2-src-%{version}.tar.xz
# PATCH-FEATURE-OPENSUSE
Patch1:         0001-add-opensuse-customizations.patch
BuildRequires:  cmake >= 3.16
BuildRequires:  gcc-c++
# Use gcc 10 for openSUSE Leap 15.3+ and SLE15SP3+
%if 0%{?suse_version} < 1550 && 0%{?sle_version} >= 150400
BuildRequires:  gcc11-c++
%endif
BuildRequires:  ninja
BuildRequires:  pkgconfig
BuildRequires:  shaderc
BuildRequires:  cmake(Qt5LinguistTools) >= 5.10.0
BuildRequires:  pkgconfig(Qt5Concurrent) >= 5.10.0
BuildRequires:  pkgconfig(Qt5DBus) >= 5.10.0
BuildRequires:  pkgconfig(Qt5Qml) >= 5.10.0
BuildRequires:  pkgconfig(Qt5Svg) >= 5.10.0
BuildRequires:  pkgconfig(Qt5Widgets) >= 5.10.0
BuildRequires:  pkgconfig(Qt5X11Extras) >= 5.10.0
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
BuildRequires:  pkgconfig(libva-glx)
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

%description    devel
It's a development package for %{name}.

%prep
%autosetup -p1 -n %{name}-src-%{version}
# %setup -q -n %{name}-src-%{version}
# %patch1 -p1

%build
# Build options
%cmake \
  -DCMAKE_SHARED_LINKER_FLAGS="%{?build_ldflags} -Wl,--as-needed -Wl,-z,now" \
%if 0%{?suse_version} < 1550 && 0%{?sle_version} >= 150400
  -DCMAKE_C_COMPILER=gcc-11 \
  -DCMAKE_CXX_COMPILER=g++-11 \
%endif
  -DSOLID_ACTIONS_INSTALL_PATH="%{_datadir}/solid/actions" \
  -DUSE_LINK_TIME_OPTIMIZATION=ON \
  -DUSE_PCH=ON \
  -DUSE_GIT_VERSION=OFF \
  -DCMAKE_INSTALL_PREFIX=%{_prefix} \
  -DCMAKE_INSTALL_LIBDIR=%{_libdir} \
  -DUSE_GLSLC=ON \
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
