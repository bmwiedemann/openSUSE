#
# spec file for package syncplay
#
# Copyright (c) 2023 SUSE LLC
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
Version:        1.7.0
Release:        0
Summary:        Client/server to synchronize media playback on mpv/VLC on multiple computers
License:        Apache-2.0
URL:            https://syncplay.pl/
Source:         https://github.com/Syncplay/syncplay/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
#PATCH-FIX-SUSE switch-env-to-python.patch nopeinomicon@posteo.net -- Sets interpreter to python3 as opposed to env python3
Patch0:         switch-env-to-python.patch
BuildRequires:  hicolor-icon-theme
BuildRequires:  make
BuildRequires:  python-rpm-generators
BuildRequires:  update-desktop-files
%{?python_enable_dependency_generator}

%description
Client/server to synchronize media playback on mpv/VLC on multiple
computers.

%package common
Summary:        The common files for the Syncplay client and server

%description common
The common files for the Syncplay client and server

%package client
Summary:        Client to synchronize media playback on mpv/VLC on multiple computers
Requires:       %{name}-common
Requires:       python3-Twisted >= 16.4.0
Recommends:     python3-certifi >= 2018.11.29
Recommends:     python3-idna >= 0.6
Recommends:     python3-pem >= 21.2.0
Recommends:     python3-pyOpenSSL >= 16.0.0
Recommends:     python3-service_identity
Suggests:       mpv
%if 0%{?suse_version} > 1500
Recommends:     python3-pyside6
%else
Recommends:     python3-pyside2 >= 5.12.0
%endif

%description client
The client application for Syncplay, allows you to play media in
synchronization with other users around the world, making movie
nights even across countries possible.

%package server
Summary:        Server for the Syncplay media synchronizing application
Requires:       %{name}-common
Requires:       python3-Twisted >= 16.4.0
Recommends:     python3-certifi >= 2018.11.29
Recommends:     python3-idna >= 0.6
Recommends:     python3-pem >= 21.2.0
Recommends:     python3-pyOpenSSL >= 16.0.0
Recommends:     python3-service_identity

%description server
The server applciation for Syncplay, acts as a hub for other users
to connect to and watch videos together in synchronization.

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
%dir %{_prefix}/lib/syncplay/
%dir %{_prefix}/lib/syncplay/syncplay/
%{_prefix}/lib/syncplay/syncplay/*
%{_datadir}/icons/hicolor/*/apps/syncplay.png
%{_datadir}/pixmaps/syncplay.png

%files client
%license LICENSE
%doc README.md
%{_bindir}/syncplay
%{_prefix}/lib/syncplay/syncplayClient.py
%{_datadir}/applications/syncplay.desktop
%{_mandir}/man1/syncplay.1%{?ext_man}

%files server
%license LICENSE
%doc README.md
%{_bindir}/syncplay-server
%{_prefix}/lib/syncplay/syncplayServer.py
%{_datadir}/applications/syncplay-server.desktop
%{_mandir}/man1/syncplay-server.1%{?ext_man}

%changelog
