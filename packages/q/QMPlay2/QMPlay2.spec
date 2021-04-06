#
# spec file for package QMPlay2
#
# Copyright (c) 2021 SUSE LLC
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

Name:             QMPlay2
Version:          21.03.09
Release:          0
Summary:          A Qt based media player, streamer and downloader
License:          LGPL-3.0-or-later
Group:            Productivity/Multimedia/Video/Players
URL:              https://github.com/zaps166/QMPlay2
Source:           https://github.com/zaps166/QMPlay2/releases/download/%{version}/QMPlay2-src-%{version}.tar.xz
# PATCH-FEATURE-OPENSUSE
Patch1:           0001-add-opensuse-customizations.patch
# PATCH-FIX-UPSTREAM
Patch2:           0001-fix-kde-startup-warning.patch
# PATCH-FIX-UPSTREAM
Patch3:           0001-fix-driver-crash.patch
# PATCH-FIX-UPSTREAM
Patch4:           0001-fix-youtube-search.patch
BuildRequires:    cmake >= 3.16
BuildRequires:    gcc-c++
BuildRequires:    ninja
BuildRequires:    pkgconfig
BuildRequires:    cmake(Qt5LinguistTools) >= 5.10.0
BuildRequires:    pkgconfig(Qt5Concurrent) >= 5.10.0
BuildRequires:    pkgconfig(Qt5DBus) >= 5.10.0
BuildRequires:    pkgconfig(Qt5Qml) >= 5.10.0
BuildRequires:    pkgconfig(Qt5Svg) >= 5.10.0
BuildRequires:    pkgconfig(Qt5Widgets) >= 5.10.0
BuildRequires:    pkgconfig(Qt5X11Extras) >= 5.10.0
BuildRequires:    pkgconfig(alsa)
BuildRequires:    pkgconfig(libass)
BuildRequires:    pkgconfig(libavcodec) >= 58.18.100
BuildRequires:    pkgconfig(libavdevice)
BuildRequires:    pkgconfig(libavformat) >= 58.12.100
BuildRequires:    pkgconfig(libavutil) >= 56.14.100
BuildRequires:    pkgconfig(libcddb)
BuildRequires:    pkgconfig(libcdio)
BuildRequires:    pkgconfig(libgme)
# Enable PipeWire support on openSUSE Tumbleweed
%if 0%{?suse_version} >= 1550
BuildRequires:    pkgconfig(libpipewire-0.3) >= 0.3.22
%endif
BuildRequires:    pkgconfig(libpulse)
BuildRequires:    pkgconfig(libsidplayfp)
BuildRequires:    pkgconfig(libswresample) >= 3.1.100
BuildRequires:    pkgconfig(libswscale) >= 5.1.100
BuildRequires:    pkgconfig(libva)
BuildRequires:    pkgconfig(libva-glx)
BuildRequires:    pkgconfig(taglib) >= 1.9
BuildRequires:    pkgconfig(vdpau)
BuildRequires:    pkgconfig(xv)
Requires(post):   hicolor-icon-theme
Requires(post):   shared-mime-info
Requires(post):   update-desktop-files
Requires(postun): hicolor-icon-theme
Requires(postun): shared-mime-info
Requires(postun): update-desktop-files
Recommends:       youtube-dl
Requires:         python > 3.0.0

%description
QMPlay2 is a video player, it can play and stream all formats supported by
ffmpeg and libmodplug (including J2B). It has an integrated Youtube
browser.

%package          devel
Summary:          %{name} development files
Group:            Development/Libraries/Other
Requires:         %{name} = %{version}

%description    devel
It's a development package for %{name}.

%prep
%autosetup -p1 -n %{name}-src-%{version}

%build
# Build options
%cmake \
  -DCMAKE_SHARED_LINKER_FLAGS="%{?build_ldflags} -Wl,--as-needed -Wl,-z,now" \
  -DSOLID_ACTIONS_INSTALL_PATH="%{_datadir}/solid/actions" \
  -DUSE_LINK_TIME_OPTIMIZATION=ON \
  -DUSE_PCH=ON \
  -DUSE_GIT_VERSION=OFF \
  -DUSE_EXTENSIONS=ON \
  -DUSE_CHIPTUNE_SID=ON \
  -DUSE_GLSLC=OFF \
  -DUSE_MEDIABROWSER=ON \
  -DUSE_LASTFM=ON \
  -DUSE_LYRICS=ON \
  -DUSE_RADIO=ON \
  -DUSE_YOUTUBE=ON \
%if 0%{?suse_version} >= 1550
  -DUSE_PIPEWIRE=ON \
%else
  -DUSE_PIPEWIRE=OFF \
%endif
  -DUSE_UPDATES=OFF \
  -DUSE_YOUTUBEDL=ON

%ninja_build

%install
%ninja_install -C build

# Let's use %%doc macro. AUTHORS & ChangeLog are required for help window
cd %{buildroot}/%{_datadir}/qmplay2
rm LICENSE README.md

# WARNING: gzipped-svg-icon. Not all DE that support SVG icons support
# them gzipped (.svgz). Install the icon as plain uncompressed SVG.
gunzip -S svgz %{buildroot}/%{_datadir}/icons/hicolor/scalable/apps/%{name}.svgz

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
%{_datadir}/icons/hicolor/scalable/apps/%{name}.*
%{_datadir}/qmplay2
%{_mandir}/man?/%{name}.?%{ext_man}
%{_datadir}/mime/packages/x-*.xml

%files devel
%{_includedir}/%{name}

%changelog
