#
# spec file for package kawaii-player
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


# See also http://en.opensuse.org/openSUSE:Specfile_guidelines

%define _over   4.2.0-1
%define _bver   4.2.0
Name:           kawaii-player
Version:        4.2.0.1
Release:        0
Summary:        Multimedia player, library manager and media server
License:        GPL-3.0-or-later
Group:          Productivity/Multimedia/Video/Players
URL:            https://github.com/kanishka-linux/kawaii-player
Source0:        https://github.com/kanishka-linux/kawaii-player/archive/v%{_over}.tar.gz#/%{name}-%{_over}.tar.gz
BuildRequires:  fdupes
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
Requires:       ffmpegthumbnailer
Requires:       mpv
Requires:       python3-Pillow
Requires:       python3-base
Requires:       python3-beautifulsoup4
Requires:       python3-certifi
Requires:       python3-libtorrent-rasterbar
Requires:       python3-lxml
Requires:       python3-mutagen
Requires:       python3-opengl
Requires:       python3-pycurl
Requires:       python3-pytaglib
Requires:       python3-qt5
Requires:       python3-qtwebengine-qt5
Requires:       python3-youtube-dl
BuildArch:      noarch

%description
Kawaii-Player is an audio/video manager and multimedia player based on mpv
and can also work as media server.

%prep
%setup -q -n %{name}-%{_over}
mv kawaii_player/resources/%{name}.desktop .
sed -e '/^Icon/cIcon = %{name}' -e '/^Exec/cExec = %{name} %f' -e '1{ /^#!/d; }' -i %{name}.desktop
sed -e "s/bs4/beautifulsoup4/g" -e "s/'PyQt5',//g" -i setup.py

%build
python3 setup.py build

%install
python3 setup.py install --root=%{buildroot} --prefix=%{_prefix}
mkdir -pv %{buildroot}/%{_datadir}/applications %{buildroot}/%{_datadir}/pixmaps
install -m 0644 %{name}.desktop %{buildroot}/%{_datadir}/applications/%{name}.desktop
install -m 0644 kawaii_player/resources/tray.png %{buildroot}/%{_datadir}/pixmaps/%{name}.png
%fdupes -s %{buildroot}%{python3_sitelib}

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_bindir}/%{name}-console
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/applications/%{name}.desktop
%{python3_sitelib}/kawaii_player
%{python3_sitelib}/kawaii_player-%{_bver}-py%{py3_ver}.egg-info

%changelog
