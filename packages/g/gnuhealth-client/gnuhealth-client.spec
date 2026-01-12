#
# spec file for package gnuhealth-client
#
# Copyright (c) 2026 SUSE LLC and contributors
# Copyright (c) 2015-2026 Dr. Axel Braun
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


%define majorver 5.0

%define pythons python3
%define mypython python3
%define mysitelib %python3_sitelib
%{?sle15_python_module_pythons}

Name:           gnuhealth-client
Version:        %{majorver}.1
Release:        0
Summary:        The client of the GNU Health Hospital system
License:        GPL-3.0-only
Group:          Productivity/Office/Management
URL:            http://health.gnu.org/
Source:         https://ftp.gnu.org/pub/gnu/health/%{name}-%{version}.tar.gz
##%Source:         %{name}-%{version}.tar.gz
##%Source1:        %{name}-plugins-%{version}.tar.gz
Source1:        ftp://ftp.gnu.org/gnu/health/plugins/gnuhealth_plugin_camera-latest.tar.gz
Source2:        ftp://ftp.gnu.org/gnu/health/plugins/gnuhealth_plugin_crypto-latest.tar.gz
Source3:        ftp://ftp.gnu.org/gnu/health/plugins/gnuhealth_plugin_frl-latest.tar.gz

Source5:        https://ftp.gnu.org/gnu/health/%{name}-%{version}.tar.gz.sig
Source6:        https://savannah.gnu.org/project/memberlist-gpgkeys.php?group=health&download=1#/%{name}.keyring

BuildRequires:  %{mypython}-Babel
BuildRequires:  %{mypython}-Sphinx
BuildRequires:  %{mypython}-devel
BuildRequires:  %{mypython}-gobject
BuildRequires:  %{mypython}-pip
BuildRequires:  %{mypython}-poetry-core >= 2.0.0
BuildRequires:  %{mypython}-python-dateutil
BuildRequires:  %{mypython}-setuptools
BuildRequires:  %{mypython}-simplejson
BuildRequires:  %{mypython}-wheel
BuildRequires:  fdupes
BuildRequires:  update-desktop-files

Requires:       %{mypython}-GooCalendar >= 0.5
Requires:       %{mypython}-cairo
Requires:       %{mypython}-chardet
Requires:       %{mypython}-dateutil
Requires:       %{mypython}-gobject
Requires:       %{mypython}-gobject-Gdk
Requires:       %{mypython}-gobject-cairo
Requires:       %{mypython}-numpy
Requires:       %{mypython}-opencv
Requires:       %{mypython}-python-gnupg
Requires:       %{mypython}-pytz
Requires:       %{mypython}-setuptools
Requires:       %{mypython}-simplejson
Requires:       %{mypython}-xml
Requires:       gnu-free-fonts
Requires:       gobject-introspection
Requires:       opencv

BuildArch:      noarch

## Conflicts:      tryton

%description
The client of the GNU Health Hospital application

%prep
%autosetup -n his-client

pwd
cd gnuhealth/plugins
tar  -xzvf %{SOURCE1}
tar  -xzvf %{SOURCE2}
tar  -xzvf %{SOURCE3}

#workaround for tryton bug: directory name with version is not considered
mv gnuhealth_camera* camera
## mv gnuhealth_crypto* crypto
##  mv gnuhealth_frl* frl

# Remove pycache
rm -rf */__pycache__

#shebag ersetzen
find . -iname "bin/gnuhealth-client" -exec sed -i "s/env python/%{mypython}/" '{}' \;

%build
%pyproject_wheel

%install
%pyproject_install

# menu-entry
desktop-file-install --dir %{buildroot}%{_datadir}/applications %{name}.desktop
%suse_update_desktop_file %{name}

mkdir -p %{buildroot}%{_datadir}/pixmaps

cp %{buildroot}%{mysitelib}/gnuhealth/data/pixmaps/gnuhealth/gnuhealth-icon.png %{buildroot}%{_datadir}/pixmaps/gnuhealth.png

%python_expand %fdupes %{buildroot}%{python3_sitelib}

%files
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%doc Changelog
%license COPYRIGHT COPYING
%{_datadir}/pixmaps/*
%{mysitelib}/gnuhealth_client-%{version}.dist-info
%{mysitelib}/gnuhealth
%{mysitelib}/gnuhealth_client-%{version}.dist-info/*

%changelog
