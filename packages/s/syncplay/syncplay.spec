#
# spec file for package syncplay
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


Name:           syncplay
Version:        1.6.7
Release:        0
Summary:        Client/server to synchronize media playback on mpv/VLC on multiple computers
License:        Apache-2.0
Group:          Productivity/Multimedia/Other
URL:            https://syncplay.pl/
Source0:        %{name}-%{version}.tar.gz
#PATCH-FIX-SUSE switch-env-to-python.patch nopeinomicon@posteo.net -- Sets interpreter to python3 as opposed to env python3
Patch0:         switch-env-to-python.patch
BuildRequires:  hicolor-icon-theme
BuildRequires:  make
BuildRequires:  python-rpm-generators
BuildRequires:  update-desktop-files
%{?python_enable_dependency_generator}

%description
Client/server to synchronize media playback on mpv/VLC on multiple computers

%package common
Summary:        The common files for the Syncplay client and server
Group:          Productivity/Multimedia/Other

%description common
The common files for the Syncplay client and server

%package client
Summary:        Client to synchronize media playback on mpv/VLC on multiple computers
Group:          Productivity/Multimedia/Other
Requires:       %{name}-common
Requires:       python >= 3.4.0
Requires:       python3-Twisted >= 16.4.0
Recommends:     python3-certifi >= 2018.11.29
Recommends:     python3-idna >= 0.6
Recommends:     python3-pyOpenSSL >= 16.0.0
Recommends:     python3-pyside2 >= 5.12.0
Recommends:     python3-service_identity
Suggests:       mpv

%description client
The client application for Syncplay, allows you to play media in sync with other users around the world, making movie nights even across countries possible

%package server
Summary:        Server for the Syncplay media synchronizing application
Group:          Productivity/Multimedia/Other
Requires:       %{name}-common
Requires:       python >= 3.4.0
Requires:       python3-Twisted >= 16.4.0
Recommends:     python3-certifi >= 2018.11.29
Recommends:     python3-idna >= 0.6
Recommends:     python3-pyOpenSSL >= 16.0.0
Recommends:     python3-pyside2 >= 5.12.0
Recommends:     python3-service_identity

%description server
The server applciation for Syncplay, acts as a hub for other users to connect to and watch videos together in sync

%prep
%autosetup -p1

%build
# Nothing to build

%install
%make_install
%suse_update_desktop_file -r %{name} AudioVideo Player Network
%suse_update_desktop_file -r %{name}-server AudioVideo Network

%files common
%license LICENSE
%doc README.md
%{_prefix}/lib/syncplay/syncplay/*
%dir %{_prefix}/lib/syncplay
%dir %{_prefix}/lib/syncplay/syncplay
%{_datadir}/icons/hicolor/16x16/apps/syncplay.png
%{_datadir}/icons/hicolor/24x24/apps/syncplay.png
%{_datadir}/icons/hicolor/32x32/apps/syncplay.png
%{_datadir}/icons/hicolor/48x48/apps/syncplay.png
%{_datadir}/icons/hicolor/64x64/apps/syncplay.png
%{_datadir}/icons/hicolor/96x96/apps/syncplay.png
%{_datadir}/icons/hicolor/128x128/apps/syncplay.png
%{_datadir}/icons/hicolor/256x256/apps/syncplay.png
%{_datadir}/pixmaps/syncplay.png

%files client
%license LICENSE
%doc README.md
%{_bindir}/syncplay
%{_prefix}/lib/syncplay/syncplayClient.py
%{_datadir}/applications/syncplay.desktop

%files server
%license LICENSE
%doc README.md
%{_bindir}/syncplay-server
%{_prefix}/lib/syncplay/syncplayServer.py
%{_datadir}/applications/syncplay-server.desktop

%changelog
