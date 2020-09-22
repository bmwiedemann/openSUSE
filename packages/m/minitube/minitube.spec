#
# spec file for package minitube
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


Name:           minitube
Version:        3.5.1
Release:        0
Summary:        Native YouTube Client
License:        GPL-3.0-or-later
Group:          Productivity/Multimedia/Video/Players
URL:            https://flavio.tordini.org/minitube
Source:         %{name}-%{version}.tar.xz
# Manpage written by Jakob Haufe <sur5r@sur5r.net> for the Debian project.
Source1:        minitube.1
# PATCH-FIX-OPENSUSE minitube-no-update-check.patch -- Disable build of internal updater
Patch0:         %{name}-no-update-check.patch
BuildRequires:  fdupes
BuildRequires:  hicolor-icon-theme
BuildRequires:  libqt5-linguist
BuildRequires:  libqt5-qtdeclarative-devel
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5Script)
BuildRequires:  pkgconfig(Qt5Sql)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5X11Extras)
BuildRequires:  pkgconfig(Qt5Xml)
BuildRequires:  pkgconfig(mpv) >= 0.29.0
Recommends:     %{name}-lang

%description
Minitube is a native YouTube client. With it you can watch YouTube
videos in a new way: you type a keyword, Minitube gives you an
endless video stream.

Minitube is not about cloning the original YouTube web interface,
it strives to create a new TV-like experience.

%lang_package

%prep
%setup -q
%patch0 -p1

# Remove build time references so build-compare can do its work
FAKE_BUILDDATE="$(LC_ALL=C date -u -d "@${SOURCE_DATE_EPOCH}" '+%%b %%e %%Y')"
sed -i "s/__DATE__/\"$FAKE_BUILDDATE\"/" src/aboutview.cpp

%build
%qmake5 \
  PREFIX=%{_prefix}
%make_build

%install
%qmake5_install
install -Dpm 0644 %{SOURCE1} %{buildroot}%{_mandir}/man1/%{name}.1
%suse_update_desktop_file -r %{name} AudioVideo Video Player
# symlink for german translation file de_DE -> de
pushd %{buildroot}%{_datadir}/%{name}/locale
ln -s de_DE.qm de.qm
popd
%fdupes %{buildroot}%{_datadir}/

%files
%license COPYING
%doc AUTHORS CHANGES TODO
%{_bindir}/%{name}
%{_datadir}/%{name}/
%exclude %{_datadir}/%{name}/locale/
%{_datadir}/applications/%{name}.desktop
%dir %{_datadir}/icons/hicolor/*/
%dir %{_datadir}/icons/hicolor/*/apps/
%{_datadir}/icons/hicolor/*/apps/%{name}*
%dir %{_datadir}/appdata/
%{_datadir}/appdata/%{name}.appdata.xml
%{_mandir}/man?/%{name}.?%{?ext_man}

%files lang
%{_datadir}/%{name}/locale/

%changelog
