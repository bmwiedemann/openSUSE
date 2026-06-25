#
# spec file for package quimup
#
# Copyright (c) 2026 SUSE LLC and contributors
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

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


%define _mainv  2.1.2
Name:           quimup
Version:        2.1.2
Release:        0
Summary:        A client for the music player daemon (MPD)
# was http://www.coonsden.com
License:        GPL-3.0-or-later
Group:          Productivity/Multimedia/Sound/Players
URL:            https://quimup.sourceforge.io
Source0:        https://sourceforge.net/projects/quimup/files/Quimup%20%{_mainv}/quimup_%{version}_source.tar.gz
BuildRequires:  hicolor-icon-theme
%if 0%{suse_version} >= 1600 && 0%{suse_version} < 1699
BuildRequires:  gcc15-PIE
BuildRequires:  gcc15-c++
%endif
BuildRequires:  pkgconfig(Qt6Core)
BuildRequires:  pkgconfig(Qt6Gui)
BuildRequires:  pkgconfig(Qt6Network)
BuildRequires:  pkgconfig(Qt6Widgets)
BuildRequires:  pkgconfig(libmpdclient)
Requires:       mpd

%description
QUIMUP is a client for the music player daemon (MPD) written in C++ and QT3.

The program can be used with most Linux desktops (KDE, GNOME, XFCE).
The interface offers controlling MPD's many features.
The focus is on mouse handling: playlist management is done entirely by drag-&-drop;
playback functions are directly accessible from the system tray.

%prep
%autosetup -p1 -n quimup_%{version}_source
rm build -r
rm .qmake.stash Makefile
for f in changelog faq readme; do
  mv -f RPM_DEB_build/share/doc/quimup/${f} .
done

%build
%if 0%{suse_version} >= 1600 && 0%{suse_version} < 1699
export CC=gcc-15 CXX=g++-15
%endif
%qmake6
%qmake6_build

%install
install -D -m 0755 %{name} %{buildroot}/%{_bindir}/%{name}
install -D -m 0644 RPM_DEB_build/share/applications/Quimup.desktop \
  %{buildroot}/%{_datadir}/applications/%{name}.desktop
cp -r RPM_DEB_build/share/icons %{buildroot}/%{_datadir}
install -D -m 0644 RPM_DEB_build/share/man/man1/quimup.1 \
  %{buildroot}/%{_mandir}/man1/%{name}.1

%files
%doc changelog description faq readme
%license COPYING
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.*
%{_mandir}/man1/%{name}.1%{?ext_man}

%changelog
