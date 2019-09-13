#
# spec file for package xfmpc
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


Name:           xfmpc
Version:        0.3.0
Release:        0
Summary:        MPD Client for the Xfce Desktop Environment
License:        GPL-2.0-or-later
Group:          Productivity/Multimedia/Sound/Players
Url:            https://goodies.xfce.org/projects/applications/xfmpc
Source:         https://archive.xfce.org/src/apps/xfmpc/0.3/%{name}-%{version}.tar.bz2
Source1:        xfmpc.png
BuildRequires:  intltool
BuildRequires:  sed
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(gthread-2.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libmpd)
BuildRequires:  pkgconfig(libxfce4ui-2)
BuildRequires:  pkgconfig(libxfce4util-1.0)
Recommends:     %{name}-lang = %{version}
Suggests:       mpd

%description
Xfmpc is a Music Player Daemon (MPD) client application for the
Xfce desktop environment.

%lang_package

%prep
%setup -q
sed -i 's/Icon=stock_volume/Icon=xfmpc/' xfmpc.desktop.in

%build
%configure
%make_build

%install
%make_install
install -D -m 0644 -p %{SOURCE1} %{buildroot}%{_datadir}/pixmaps/%{name}.png

%suse_update_desktop_file %{name}

rm -rf %{buildroot}%{_datadir}/locale/{ast,kk,tl_PH,ur_PK}

%find_lang %{name} %{?no_lang_C}

%files
%doc AUTHORS IDEAS NEWS README THANKS
%license COPYING
%{_bindir}/xfmpc
%{_mandir}/man1/*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png

%files lang -f %{name}.lang

%changelog
