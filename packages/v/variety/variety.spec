#
# spec file for package variety
#
# Copyright (c) 2023 SUSE LLC
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
Version:        0.8.10
Release:        0
Summary:        Wallpaper changer
License:        GPL-3.0-only
Group:          Productivity/Multimedia/Other
URL:            https://launchpad.net/variety/
Source0:        https://github.com/varietywalls/variety/archive/%{version}.tar.gz#/variety-%{version}.tar.gz
Source1:        variety.desktop
# Todo: Variety should follow FDO icon standards
Source2:        VarietyIcons.tar.gz
# PATCH-FIX-OPENSUSE variety-appdata-path.patch malcolmlewis@opensuse.org -- Set correct name/path for appdata not metadata.
Patch0:         variety-appdata-path.patch
# PATCH-FIX-OPENSUSE variety-fix-data-path.patch malcolmlewis@opensuse.org -- Set user data path to /usr/share/variety
Patch1:         variety-fix-data-path.patch
BuildRequires:  fdupes
BuildRequires:  gobject-introspection
BuildRequires:  hicolor-icon-theme
BuildRequires:  intltool
BuildRequires:  python-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3-distutils-extra
BuildRequires:  python3-setuptools
BuildRequires:  update-desktop-files
# MANUAL BEGIN
Requires:       ImageMagick
Requires:       libnotify4
Requires:       python3-Pillow
Requires:       python3-beautifulsoup4
Requires:       python3-configobj
Requires:       python3-dbus-python
Requires:       python3-gexiv2
Requires:       python3-gobject-Gdk
Requires:       python3-httplib2
Requires:       python3-lxml
Requires:       python3-pycairo
Requires:       python3-pycurl
Requires:       python3-requests
Requires:       yelp
# MANUAL END
BuildArch:      noarch

%description
Variety changes the desktop wallpaper on a regular basis, using user-specified
or automatically downloaded images.

Variety sits conveniently as an indicator in the panel and can be easily paused
and resumed. The mouse wheel can be used to scroll wallpapers back and forth
until you find the perfect one for your current mood.

Apart from displaying images from local folders, several different online sources
can be used to fetch wallpapers according to user-specified criteria.

%prep
%setup -q -n %{name}-%{version} -a 2
%patch0 -p1
%patch1 -p1

%build
%{python3_build}

%install
%{python3_install}
# Create our own desktop file and remove the pre-installed version
rm build/share/applications/%{name}.desktop
cp %{SOURCE1} .
%if 0%{?suse_version} <= 1500
install -Dm0644 data/media/variety.svg %{buildroot}%{_datadir}/pixmaps/variety.svg
%endif
cp VarietyIcons/* %{buildroot}%{_datadir}/variety/media/
%suse_update_desktop_file -i %{name}
%fdupes -s %{buildroot}
# Remove README.md as we install in %%doc
rm -rf %{buildroot}%{_datadir}/doc/variety

# Not sure why Leap 15 doesn't pick up translations.
%if 0%{?suse_version} > 1500
%find_lang variety
%endif

%if 0%{?suse_version} > 1500
%files -f variety.lang
%else

%files
%endif
%defattr(-,root,root)
%doc AUTHORS README.md
%license LICENSE
%{_bindir}/%{name}
%{python3_sitelib}/jumble
%{python3_sitelib}/%{name}
%{python3_sitelib}/%{name}_lib
%{python3_sitelib}/%{name}-%{version}-py%{py3_ver}.egg-info
%dir %{_datadir}/appdata
%{_datadir}/appdata/variety.appdata.xml
%{_datadir}/applications/%{name}.desktop
%if 0%{?suse_version} > 1500
%{_datadir}/icons/hicolor/scalable/apps/variety.svg
%{_datadir}/icons/hicolor/22x22/apps/variety-indicator-dark.png
%{_datadir}/icons/hicolor/22x22/apps/variety-indicator.png
%else
%{_datadir}/pixmaps/variety.svg
%endif
%{_datadir}/%{name}

%changelog
