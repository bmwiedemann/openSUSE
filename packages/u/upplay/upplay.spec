#
# spec file for package upplay
#
# Copyright (c) 2025 SUSE LLC
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
Version:        1.8.1
Release:        0
Summary:        UPnP and OpenHome audio Control Point
License:        GPL-2.0-or-later
URL:            https://www.lesbonscomptes.com/upplay/
Source0:        https://www.lesbonscomptes.com/upplay/downloads/upplay-%{version}.tar.gz
Source1:        https://www.lesbonscomptes.com/upplay/downloads/upplay-%{version}.tar.gz.asc
Source2:        https://www.lesbonscomptes.com/pages/jf-at-dockes.org.pub#/%{name}.keyring
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
BuildRequires:  libqt5-qtbase-common-devel
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(Qt5WebEngine)
BuildRequires:  pkgconfig(jsoncpp)
BuildRequires:  pkgconfig(libupnpp) >= 0.24.1
BuildRequires:  pkgconfig(mpris-qt5)

%description
upplay is a Qt5-based audio Control Point for browsing and playing music
managed by your UPnP/DLNA media servers to your UPnP/DLNA/OpenHome players (renderers).

%prep
%autosetup

%build
%qmake5 QMAKE_POST_LINK='$(STRIP) $(TARGET)' WEBPLATFORM=webengine
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
