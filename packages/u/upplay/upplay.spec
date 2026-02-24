#
# spec file for package upplay
#
# Copyright (c) 2026 SUSE LLC and contributors
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


Name:           upplay
Version:        1.9.10
Release:        0
Summary:        UPnP and OpenHome audio Control Point
License:        GPL-2.0-or-later
URL:            https://www.lesbonscomptes.com/upplay/
Source0:        https://www.lesbonscomptes.com/upplay/downloads/upplay-%{version}.tar.gz
Source1:        https://www.lesbonscomptes.com/upplay/downloads/upplay-%{version}.tar.gz.asc
Source2:        https://www.lesbonscomptes.com/pages/lesbonscomptes.gpg#/%{name}.keyring
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(Qt6WebEngineWidgets)
BuildRequires:  pkgconfig(jsoncpp)
BuildRequires:  pkgconfig(libupnpp) >= 1.0.0

%description
upplay is a Qt based audio Control Point for browsing and playing music
managed by your UPnP/DLNA media servers to your UPnP/DLNA/OpenHome players (renderers).

%prep
%autosetup

%build
# compilation fix for amber-mpris on Leap 15.6 caused by /bin not being a link to /usr/bin
(cd amber-mpris && sed -i 's:/bin/qmake6:/usr/bin/qmake6:' Makefile src/Makefile qtdbusextended/Makefile)
# temporary compilation fix: https://framagit.org/medoc92/upplay/-/commit/849e3e5ff469a864ac8a6a91f867d8fe6698da73
sed -i 's/config += dbus/QT += dbus/' upplay.pro
%qmake6 QMAKE_POST_LINK='$(STRIP) $(TARGET)' WEBPLATFORM=webengine
%make_build STRIP=%{_bindir}/strip

%install
make install INSTALL_ROOT=%{buildroot}
%suse_update_desktop_file -n -r %{name} "AudioVideo;Player"
%fdupes %{buildroot}/%{_prefix}

%files
%license COPYING
%doc AUTHORS
%{_bindir}/%{name}
%{_datadir}/applications/upplay.desktop
%{_datadir}/%{name}
%{_datadir}/icons/hicolor/48x48/apps/upplay.png
%{_datadir}/pixmaps/upplay.png

%changelog
