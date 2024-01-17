#
# spec file for package noson-app
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


Name:           noson-app
Version:        5.4.0
Release:        0
Summary:        SONOS device controller
License:        GPL-3.0-or-later
Group:          Productivity/Multimedia/Sound/Players
URL:            https://janbar.github.io/noson-app/index.html
Source0:        https://github.com/janbar/noson-app/archive/refs/tags/%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  extra-cmake-modules
BuildRequires:  flac-devel
BuildRequires:  gcc-c++
BuildRequires:  libopenssl-devel
BuildRequires:  libpulse-devel
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  zlib-devel
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Qml)
BuildRequires:  pkgconfig(Qt5QuickControls2)
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  pkgconfig(Qt5Xml)
BuildRequires:  pkgconfig(noson) >= 2.10.0

%description
A controller for SONOS devices. It allows for browsing the music
library, and playing tracks or radio on any zones. Zone groups,
queues and playlists can be managed, and playback be controlled.

%prep
%setup -q

%build
%cmake \
    -DCMAKE_BUILD_TYPE=Release \
    -DBUILD_DEPENDENCIES=OFF \
    -DBUILD_LIBNOSON=OFF
%make_jobs

%install
%make_install -C build
%suse_update_desktop_file -i io.github.janbar.noson Music

%if 0%{?suse_version} < 1330
%post
%desktop_database_post
%endif

%if 0%{?suse_version} < 1330
%postun
%desktop_database_postun
%endif

%files
%doc README.md
%license LICENSE
%{_bindir}/noson-app
%{_datadir}/applications/io.github.janbar.noson.desktop
%{_datadir}/icons/hicolor/
%{_datadir}/metainfo/io.github.janbar.noson.appdata.xml
%{_libdir}/noson/

%changelog
