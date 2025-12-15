#
# spec file for package Photini
#
# Copyright (c) 2025 SUSE LLC and contributors
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
Version:        2025.10.0
Release:        0
Summary:        Digital photograph metadata (EXIF, IPTC, XMP) editing application
License:        GPL-3.0-or-later
Group:          Productivity/Graphics/Other
URL:            https://github.com/jim-easterbrook/Photini
Source0:        https://github.com/jim-easterbrook/Photini/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  desktop-file-utils
BuildRequires:  fdupes
BuildRequires:  hicolor-icon-theme
BuildRequires:  python3-pip
BuildRequires:  python3-platformdirs
BuildRequires:  python3-qtwebengine-qt5
BuildRequires:  python3-setuptools
BuildRequires:  python3-setuptools_scm
BuildRequires:  python3-wheel
Requires:       python3-Pillow
Requires:       python3-cachetools
Requires:       python3-chardet
Requires:       python3-exiv2
Requires:       python3-filetype
Requires:       python3-platformdirs
Requires:       python3-requests >= 2.4.0
Requires:       python3-requests-oauthlib
Requires:       python3dist(pyqtwebengine)
Requires:       typelib(GExiv2)
# For the flickr, Google Photos, Ipernity and Pixelfed/Mastodon plugins
Recommends:     python3-keyring
Conflicts:      python3-keyring-keyutils
# For the flickr, Ipernity and Pixelfed/Mastodon plugin
Recommends:     python3-requests-toolbelt
# For the spelling plugin
Recommends:     python3-pyenchant
# For the GPS plugin
Recommends:     python3-gpxpy
# For the camera import plugin
Recommends:     python3-gphoto2
BuildArch:      noarch

%description
A digital photograph metadata (EXIF, IPTC, XMP) editing application.

"Metadata" is said to mean "data about data". In the context of digital
photographs, this means information that is not essential in order to display
the image, but tells something about it. For example, a title and
description of the scene or the date and time and the GPS coordinates of the
camera's position when the picture was taken.

%prep
%autosetup -p1

%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%python3_pyproject_wheel

%install
%python3_pyproject_install
cp -r src/photini/data %{buildroot}%{python3_sitelib}/photini/data

# Generate the desktop file and copy icons
export PYTHONPATH=%{buildroot}%{python3_sitelib}
%{buildroot}%{_bindir}/photini-post-install

# Copy icons for the desktop file
mkdir -p %{buildroot}%{_datadir}/icons
mv  ~/.local/share/icons/* %{buildroot}%{_datadir}/icons

# Adapt desktop file
sed -i 's#^Exec=[^ ]\+#Exec=/usr/bin/photini#g' \
   ~/.local/share/applications/photini.desktop
install -Dm0644 ~/.local/share/applications/photini.desktop \
   %{buildroot}%{_datadir}/applications/photini.desktop

rm %{buildroot}%{_bindir}/photini-configure
rm %{buildroot}%{_bindir}/photini-post-install

%fdupes -s %{buildroot}

%files
%doc CHANGELOG.txt README.rst
%license LICENSE.txt
%{_bindir}/photini
%{python3_sitelib}/[Pp]hotini-%{version}.dist-info
%{python3_sitelib}/photini
%{_datadir}/applications/photini.desktop
%{_datadir}/icons/hicolor/*/apps/photini.png

%changelog
