#
# spec file for package rapid-photo-downloader
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2012 Togan Muftuoglu toganm@opensuse.org
# Copyright (c) 2009-2011 Pascal Blesser pascal.bleser@opensuse.org
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


%global __requires_exclude ^typelib\\(Unity\\).*$
Name:           rapid-photo-downloader
Version:        0.9.14
Release:        0
Summary:        Parallel downloader for camera and smartphone photos
License:        GPL-3.0-or-later
Group:          Productivity/Graphics/Other
Url:            https://damonlynch.net/rapid/
Source:         https://launchpad.net/rapid/pyqt/%{version}/+download/%{name}-%{version}.tar.gz
# PATCH-FEATURE-OPENSUSE disable-version-check.patch
Patch0:         disable-version-check.patch
# PATCH-FIX-OPENSUSE oldsetuptools.patch use old syntax -- aloisio@gmx.com
Patch1:         oldsetuptools.patch
BuildRequires:  fdupes
BuildRequires:  gobject-introspection
BuildRequires:  hicolor-icon-theme
BuildRequires:  intltool
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  update-desktop-files
Requires:       exiftool
Requires:       python3-PyPrind
Requires:       python3-arrow
Requires:       python3-cairo >= 1.11.1
Requires:       python3-colorlog
Requires:       python3-colour
Requires:       python3-easygui
Requires:       python3-gobject2
Requires:       python3-gphoto2 >= 1.4.0
Requires:       python3-psutil >= 3.4.2
Requires:       python3-pymediainfo >= 2.2.0
Requires:       python3-python-dateutil >= 2.2
Requires:       python3-pyxdg
Requires:       python3-pyzmq >=  16.0.2
Requires:       python3-qt5 >= 5.4
Requires:       python3-rawkit
Requires:       python3-sortedcontainers
Requires:       python3-tornado
BuildArch:      noarch
%if 0%{?suse_version} < 1500
Requires:       python3-scandir
Requires:       python3-typing
%endif

%description
Rapid Photo Downloader downloads images in parallel from multiple devices,
from every camera supported by gphoto2, including smartphones.

RPD has a timeline, which groups photos and videos based on how much
time elapsed between consecutive shots. It can be used to identify
photos and videos taken at different periods in a single day or over
consecutive days.

%lang_package

%prep
%setup -q
%patch0 -p1
%if 0%{?sle_version} == 120300
%patch1 -p1
%endif
rm -rf rapid_photo_downloader.egg-info
find raphodo -type f -name '*.py' -exec sed -i -e '/^#!\//, 1d' {} \;

%build
python3 setup.py build

%install
python3 setup.py install \
    --prefix="%{_prefix}" \
    --root=%{buildroot}

%find_lang %{name}
%fdupes -s %{buildroot}

%files
%doc README.rst CHANGES.rst
%{_bindir}/analyze-pv-structure
%{_bindir}/%{name}
%{_datadir}/appdata/net.damonlynch.%{name}.appdata.xml
%{_datadir}/applications/net.damonlynch.%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%dir %{_datadir}/solid
%dir %{_datadir}/solid/actions
%{_datadir}/solid/actions/net.damonlynch.%{name}.desktop
%{_mandir}/man1/analyze-pv-structure.1%{ext_man}
%{_mandir}/man1/%{name}.1%{ext_man}
%{python3_sitelib}/raphodo
%{python3_sitelib}/rapid_photo_downloader-%{version}-py%{python3_version}.egg-info

%files lang -f %{name}.lang

%changelog
