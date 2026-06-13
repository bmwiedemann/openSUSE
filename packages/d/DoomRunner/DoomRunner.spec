#
# spec file for package DoomRunner
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

Name:           DoomRunner
Version:        1.9.2
Release:        0
Summary:        Preset-oriented graphical launcher for Doom engine source ports
License:        GPL-3.0-or-later
URL:            https://github.com/Youda008/DoomRunner
Source:         https://github.com/Youda008/DoomRunner/archive/refs/tags/v1.9.2.tar.gz#/%{name}-%{version}.tar.gz
# PATCH-FIX-UPSTREAM -- Commit 79a4519
Patch0:         fix-symlinks.patch
BuildRequires:  hicolor-icon-theme
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(Qt6Network)
BuildRequires:  pkgconfig(Qt6Widgets)
BuildRequires:  pkgconfig(minizip)

%description
Doom Runner is a graphical launcher for Doom/Heretic/Hexen source ports such as
GZDoom, Chocolate/Crispy Doom, International Doom and more.
It supports creating presets for each game (with mods) allowing for one-click
switching between them.

%prep
%autosetup -p1

%build
%qmake6 QMAKE_POST_LINK='$(STRIP) $(TARGET)'
%make_build STRIP=%{_bindir}/strip

%install
%qmake6_install

for size in 16 24 32 48 64 128
do
    install -D -m644 Install/XDG/DoomRunner.${size}x${size}.png %{buildroot}%{_datadir}/icons/hicolor/${size}x${size}/apps/%{name}.png
done

install -D -m644 -t %{buildroot}%{_datadir}/applications Install/XDG/DoomRunner.desktop
install -D -m644 -t %{buildroot}%{_datadir}/metainfo Install/XDG/io.github.Youda008.DoomRunner.appdata.xml

%files
%{_bindir}/DoomRunner
%{_datadir}/applications/DoomRunner.desktop
%{_datadir}/metainfo/io.github.Youda008.DoomRunner.appdata.xml
%{_datadir}/icons/hicolor/*x*/apps/DoomRunner.png

%changelog
