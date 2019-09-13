#
# spec file for package variety
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2014-2018 Malcolm J Lewis <malcolmlewis@opensuse.org>
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


Name:           variety
Version:        0.7.1
Release:        0
Summary:        Wallpaper changer
License:        GPL-3.0-only
Group:          Productivity/Multimedia/Other
Url:            https://launchpad.net/variety/
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
Requires:       python3-httplib2
Requires:       python3-lxml
Requires:       python3-pycurl
Requires:       yelp
# MANUAL END
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
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
# Todo: Add support for FDO icon standard upstream
install -Dm0644 data/media/variety.svg %{buildroot}%{_datadir}/pixmaps/variety.svg
cp VarietyIcons/* %{buildroot}%{_datadir}/variety/media/
%suse_update_desktop_file -i %{name}
%fdupes -s %{buildroot}
# Remove README.md as we install in %%doc
rm -rf %{buildroot}%{_datadir}/doc/variety

%files
%defattr(-,root,root)
%doc AUTHORS README.md
%license COPYING
%{_bindir}/%{name}
%{python3_sitelib}/jumble
%{python3_sitelib}/%{name}
%{python3_sitelib}/%{name}_lib
%{python3_sitelib}/%{name}-%{version}-py%{py3_ver}.egg-info
%dir %{_datadir}/appdata
%{_datadir}/appdata/variety.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/variety.svg
%{_datadir}/%{name}

%changelog
