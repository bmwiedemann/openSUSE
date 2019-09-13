#
# spec file for package quimup
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2016 Packman team: http://packman.links2linux.org/
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           quimup
Version:        1.4.4
Release:        0
Summary:        A client for the music player daemon (MPD)
# was http://www.coonsden.com
License:        GPL-3.0-or-later
Group:          Productivity/Multimedia/Sound/Players
URL:            https://quimup.sourceforge.io
Source0:        https://sourceforge.net/projects/quimup/files/Quimup_%{version}_source.tar.gz
Source1:        %{name}.desktop
BuildRequires:  libmpdclient-devel
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(taglib)
Requires:       mpd

%description
QUIMUP is a client for the music player daemon (MPD) written in C++ and QT3.

The program can be used with most Linux desktops (KDE, GNOME, XFCE).
The interface offers controlling MPD's many features.
The focus is on mouse handling: playlist management is done entirely by drag-&-drop;
playback functions are directly accessible from the system tray.

%prep
%setup -q -n Quimup_%{version}_source
chmod -x COPYING changelog description FAQ.txt README

%build
%qmake5
make %{?_smp_mflags}

%install
%make_install
install -D -m 755 %{name} %{buildroot}/%{_bindir}/%{name}
install -D -m 644 %{SOURCE1} %{buildroot}/%{_datadir}/applications/%{name}.desktop
install -D -m 644 src/resources/mn_icon.png %{buildroot}/%{_datadir}/pixmaps/%{name}.png
%suse_update_desktop_file -r %{name} AudioVideo Player

%files
%doc changelog description FAQ.txt README
%license COPYING
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png

%changelog
