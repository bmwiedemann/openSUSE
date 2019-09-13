#
# spec file for package gnuhealth-client
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2015-2019 Dr. Axel Braun
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


%define majorver 3.4
Name:           gnuhealth-client
Version:        %{majorver}.4
Release:        0
Summary:        The client of the GNU Health Hospital system
License:        GPL-3.0-only
Group:          Productivity/Office/Management
Url:            http://health.gnu.org/
Source:         https://files.pythonhosted.org/packages/source/g/%{name}/%{name}-%{version}.tar.gz
Source1:        ftp://ftp.gnu.org/gnu/health/plugins/gnuhealth_plugin_camera-latest.tar.gz
Source2:        ftp://ftp.gnu.org/gnu/health/plugins/gnuhealth_plugin_crypto-latest.tar.gz
Source3:        ftp://ftp.gnu.org/gnu/health/plugins/gnuhealth_plugin_frl-latest.tar.gz
Source4:        %{name}.desktop
BuildRequires:  fdupes
BuildRequires:  python-Babel
BuildRequires:  python-Sphinx
# List of additional build dependencies
BuildRequires:  python-devel
BuildRequires:  python-gtk
BuildRequires:  python-python-dateutil
BuildRequires:  python-setuptools
BuildRequires:  python-simplejson
BuildRequires:  update-desktop-files
#Requires:       librsvg
#for the plugins:
Requires:       opencv
Requires:       python-cdecimal
Requires:       python-chardet
Requires:       python-dateutil
Requires:       python-gnupg
Requires:       python-gtk
Requires:       python-opencv
Requires:       python-pytz
Requires:       python-setuptools
Requires:       python-simplejson
Requires:       python-xml
Requires:       python2-GooCalendar < 0.5
#install Tryton or GNU Health Client
Conflicts:      tryton
BuildArch:      noarch

%description
The client of the GNU Health Hospital application

%prep
%setup -q
cp %{SOURCE4} .

pwd
cd tryton/plugins/
#tar --strip-components 1 -xzvf %{SOURCE1}
#tar --strip-components 1 -xzvf %{SOURCE2}
#tar --strip-components 1 -xzvf %{SOURCE3}

tar  -xzvf %{SOURCE1}
tar  -xzvf %{SOURCE2}
tar  -xzvf %{SOURCE3}

%build
:

%install
python setup.py install --prefix=%{_prefix} --root=%{buildroot}

# menu-entry
desktop-file-install --dir %{buildroot}%{_datadir}/applications %{name}.desktop
%suse_update_desktop_file %{name}

mkdir -p %{buildroot}%{_datadir}/pixmaps
cp %{buildroot}%{python_sitelib}/tryton/data/pixmaps/tryton/gnuhealth-icon.png %{buildroot}%{_datadir}/pixmaps/gnuhealth.png

##%fdupes %{buildroot}%{_datadir}
##%fdupes %{buildroot}%{_prefix}/lib

%post
%desktop_database_post
%icon_theme_cache_post

%postun
%desktop_database_postun
%icon_theme_cache_postun

%files
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%doc Changelog
%license COPYRIGHT COPYING
%{_datadir}/pixmaps/*
%{python_sitelib}/*

%changelog
