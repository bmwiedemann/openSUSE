#
# spec file for package Photini
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


Name:           Photini
Version:        2020.10.1
Release:        0
Summary:        Digital photograph metadata (EXIF, IPTC, XMP) editing application
License:        GPL-3.0-or-later
Group:          Productivity/Graphics/Other
URL:            https://github.com/jim-easterbrook/Photini
Source0:        https://github.com/jim-easterbrook/Photini/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  ImageMagick
BuildRequires:  fdupes
BuildRequires:  hicolor-icon-theme
BuildRequires:  python3-appdirs >= 1.3
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-six >= 1.5
Requires:       ffmpeg
Requires:       libgexiv2-2 >= 0.5
Requires:       python3-appdirs >= 1.3
Requires:       python3-flickrapi
Requires:       python3-gobject
Requires:       python3-gpxpy
Requires:       python3-keyring
Requires:       python3-qt5
Requires:       python3-requests >= 2.4.0
Requires:       python3-requests-oauthlib
Requires:       python3-sip
Requires:       python3-six >= 1.5
Requires:       typelib(GExiv2)
BuildArch:      noarch

%description
A digital photograph metadata (EXIF, IPTC, XMP) editing application.

"Metadata" is said to mean "data about data". In the context of digital
photographs, this means information that is not essential in order to display
the image, but tells something about it. For example, a title and
description of the scene or the date and time and the GPS coordinates of the
camera's position when the picture was taken.

%prep
%setup -q
sed -e 's/{exec_path}/photini/' -e 's/{icon_path}/photini/' -i src/linux/photini.desktop.template

%build
python3 setup.py build
for s in 22 32 48 64 96 128 192 256 512; do
    convert -strip src/misc/icon_master.png -resize ${s}x${s} ${s}.png
done

%install
python3 setup.py install --prefix=%{_prefix} --root=%{buildroot}
for s in 22 32 48 64 96 128 192 256 512; do
mkdir -pv %{buildroot}%{_datadir}/icons//hicolor/${s}x${s}/apps
install -m0644 ${s}.png -T \
          %{buildroot}%{_datadir}/icons//hicolor/${s}x${s}/apps/photini.png
done
%fdupes %{buildroot}

%files
%doc CHANGELOG.txt README.rst
%license LICENSE.txt
%{_bindir}/photini
%{python3_sitelib}/%{name}-%{version}-py%{py3_ver}.egg-info
%{python3_sitelib}/photini
%{_datadir}/applications/photini.desktop
%{_datadir}/icons/hicolor/*/apps/photini.png

%changelog
