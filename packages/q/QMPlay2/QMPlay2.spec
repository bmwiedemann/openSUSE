#
# spec file for package QMPlay2
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           QMPlay2
Version:        19.09.03
Release:        0
Summary:        A Qt based media player, streamer and downloader
License:        LGPL-3.0-or-later
URL:            https://github.com/zaps166/QMPlay2
Source:         https://github.com/zaps166/QMPlay2/releases/download/%{version}/QMPlay2-src-%{version}.tar.xz
%if 0%{?suse_version} > 1320
BuildRequires:  gcc
BuildRequires:  gcc-c++
%else
# Leap 42.3 / SLE12SP3Backports
BuildRequires:  gcc7
BuildRequires:  gcc7-c++
%endif
BuildRequires:  cmake >= 3.5
BuildRequires:  pkgconfig
BuildRequires:  cmake(Qt5LinguistTools)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Qml)
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5X11Extras)
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(libass)
BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  pkgconfig(libavdevice)
BuildRequires:  pkgconfig(libavformat)
BuildRequires:  pkgconfig(libavutil)
BuildRequires:  pkgconfig(libcddb)
BuildRequires:  pkgconfig(libcdio)
BuildRequires:  pkgconfig(libgme)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(libsidplayfp)
BuildRequires:  pkgconfig(libswresample)
BuildRequires:  pkgconfig(libswscale)
BuildRequires:  pkgconfig(libva)
BuildRequires:  pkgconfig(libva-glx)
BuildRequires:  pkgconfig(taglib)
BuildRequires:  pkgconfig(vdpau)
BuildRequires:  pkgconfig(xv)
Requires(post): hicolor-icon-theme
Requires(post): shared-mime-info
Requires(post): update-desktop-files
Requires(postun): hicolor-icon-theme
Requires(postun): shared-mime-info
Requires(postun): update-desktop-files
Recommends:     youtube-dl

%description
QMPlay2 is a video player, it can play and stream all formats supported by
ffmpeg and libmodplug (including J2B). It has an integrated Youtube
browser.

%package        devel
Summary:        %{name} development files
Requires:       %{name} = %{version}

%description    devel
It's a development package for %{name}.

%prep
%setup -q -n %{name}-src-%{version}

%build
test -x "$(type -p gcc)" && export CC="$_"
test -x "$(type -p g++)" && export CXX="$_"
test -x "$(type -p gcc-7)" && export CC="$_"
test -x "$(type -p g++-7)" && export CXX="$_"
%cmake \
  -DUSE_PROSTOPLEER=OFF \
  -DSOLID_ACTIONS_INSTALL_PATH="/usr/share/solid/actions" \
%make_jobs

%install
%cmake_install

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
%doc LICENSE README.md
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
%if 0%{?suse_version} == 1315
%dir %{_datadir}/icons/hicolor/*
%dir %{_datadir}/icons/hicolor/*/apps
%endif
%{_datadir}/qmplay2
%{_mandir}/man?/%{name}.?%{ext_man}
%{_datadir}/mime/packages/x-*.xml

%files devel
%{_includedir}/%{name}

%changelog
