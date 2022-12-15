#
# spec file for package gnuhealth-client
#
# Copyright (c) 2022 SUSE LLC
# Copyright (c) 2015-2022 Dr. Axel Braun
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


%define majorver 4.0
Name:           gnuhealth-client
Version:        %{majorver}.2
Release:        0
Summary:        The client of the GNU Health Hospital system
License:        GPL-3.0-only
Group:          Productivity/Office/Management
URL:            http://health.gnu.org/
Source:         https://ftp.gnu.org/pub/gnu/health/%{name}-%{version}.tar.gz
##Source:         %{name}-%{version}.tar.gz
##urce1:        %{name}-plugins-%{version}.tar.gz
Source1:        ftp://ftp.gnu.org/gnu/health/plugins/gnuhealth_plugin_camera-latest.tar.gz
Source2:        ftp://ftp.gnu.org/gnu/health/plugins/gnuhealth_plugin_crypto-latest.tar.gz
Source3:        ftp://ftp.gnu.org/gnu/health/plugins/gnuhealth_plugin_frl-latest.tar.gz
Source4:        %{name}.desktop
Source5:        https://ftp.gnu.org/gnu/health/%{name}-%{version}.tar.gz.sig
Source6:        https://savannah.gnu.org/project/memberlist-gpgkeys.php?group=health&download=1#/%{name}.keyring

BuildRequires:  fdupes
BuildRequires:  python3-Babel
BuildRequires:  python3-Sphinx
BuildRequires:  python3-devel
BuildRequires:  python3-gobject
BuildRequires:  python3-python-dateutil
BuildRequires:  python3-setuptools
BuildRequires:  python3-simplejson
BuildRequires:  update-desktop-files

Requires:       gnu-free-fonts
Requires:       gobject-introspection
Requires:       opencv
Requires:       python3-GooCalendar >= 0.5
Requires:       python3-cairo
Requires:       python3-chardet
Requires:       python3-dateutil
Requires:       python3-gnupg
Requires:       python3-gobject
Requires:       python3-gobject-Gdk
Requires:       python3-gobject-cairo
Requires:       python3-numpy
Requires:       python3-opencv
Requires:       python3-pytz
Requires:       python3-setuptools
Requires:       python3-simplejson
Requires:       python3-xml

BuildArch:      noarch

## Conflicts:      tryton

%description
The client of the GNU Health Hospital application

%prep
%setup -q
### cp %{SOURCE4} .

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

%build
%python3_build

%install
%python3_install --prefix=%{_prefix} --root=%{buildroot}

# menu-entry
desktop-file-install --dir %{buildroot}%{_datadir}/applications %{name}.desktop
%suse_update_desktop_file %{name}

mkdir -p %{buildroot}%{_datadir}/pixmaps

cp %{buildroot}$(ls -d /usr/lib/python3.* )/site-packages/gnuhealth/data/pixmaps/gnuhealth/gnuhealth-icon.png %{buildroot}%{_datadir}/pixmaps/gnuhealth.png

%python_expand %fdupes %{buildroot}%{python3_sitelib}

%files
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%doc Changelog
%license COPYRIGHT COPYING
%{_datadir}/pixmaps/*
%{python3_sitelib}/*

%changelog
