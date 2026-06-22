#
# spec file for package variety
#
# Copyright (c) 2026 SUSE LLC and contributors
# Copyright (c) 2014-2021 Malcolm J Lewis <malcolmlewis@opensuse.org>
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


%global __requires_exclude typelib\\(AyatanaAppIndicator3\\)
Name:           variety
Version:        0.9.0
Release:        0
Summary:        Wallpaper changer
License:        GPL-3.0-only
Group:          Productivity/Multimedia/Other
URL:            https://github.com/varietywalls/variety/
Source0:        https://github.com/varietywalls/variety/archive/%{version}.tar.gz#/variety-%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  gobject-introspection
BuildRequires:  hicolor-icon-theme
BuildRequires:  python-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3-packaging
BuildRequires:  python3-setuptools >= 62.3.0
BuildRequires:  python3-setuptools-gettext
BuildRequires:  update-desktop-files
BuildArch:      noarch
# MANUAL BEGIN
Requires:       ImageMagick
Requires:       python3-Pillow
Requires:       python3-beautifulsoup4
Requires:       python3-configobj
Requires:       python3-dbus-python
Requires:       python3-gexiv2
Requires:       python3-gobject-Gdk
Requires:       python3-httplib2
Requires:       python3-lxml
Requires:       python3-packaging
Requires:       python3-pycairo
Requires:       python3-requests
Requires:       yelp
# MANUAL END

%description
Variety changes the desktop wallpaper on a regular basis, using user-specified
or automatically downloaded images.

Variety sits conveniently as an indicator in the panel and can be easily paused
and resumed. The mouse wheel can be used to scroll wallpapers back and forth
until you find the perfect one for your current mood.

Apart from displaying images from local folders, several different online sources
can be used to fetch wallpapers according to user-specified criteria.

%prep
%autosetup -p1 -n %{name}-%{version}

# Fix shebangs in scripts to follow openSUSE packaging guidelines
sed -i 's|#!%{_bindir}/env bash|#!/bin/bash|' variety/data/scripts/*

%build
%python3_build

%install
%python3_install
# Install desktop file, as this is not handled by setuptools automatically
install -Dm0644 variety.desktop %{buildroot}%{_datadir}/applications/%{name}.desktop
%suse_update_desktop_file %{name}

%if 0%{?suse_version} <= 1500
install -Dm0644 variety/data/media/variety.svg %{buildroot}%{_datadir}/pixmaps/variety.svg
%endif

# Install application icons manually as they are no longer handled by setup.py
install -Dm0644 variety/data/icons/scalable/apps/variety.svg %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/variety.svg
install -Dm0644 variety/data/icons/22x22/apps/variety-indicator.png %{buildroot}%{_datadir}/icons/hicolor/22x22/apps/variety-indicator.png
install -Dm0644 variety/data/icons/22x22/apps/variety-indicator-dark.png %{buildroot}%{_datadir}/icons/hicolor/22x22/apps/variety-indicator-dark.png

%fdupes -s %{buildroot}

%find_lang %{name}

%files -f %{name}.lang
%doc AUTHORS README.md
%license LICENSE
%{_bindir}/%{name}
%{python3_sitelib}/jumble
%{python3_sitelib}/%{name}
%{python3_sitelib}/%{name}_lib
%{python3_sitelib}/%{name}-%{version}*-info
%{_datadir}/applications/%{name}.desktop
%if 0%{?suse_version} > 1500
%{_datadir}/icons/hicolor/scalable/apps/variety.svg
%{_datadir}/icons/hicolor/22x22/apps/variety-indicator-dark.png
%{_datadir}/icons/hicolor/22x22/apps/variety-indicator.png
%else
%{_datadir}/pixmaps/variety.svg
%endif
%{_datadir}/metainfo/variety.appdata.xml

%changelog
