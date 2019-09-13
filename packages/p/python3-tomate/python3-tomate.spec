#
# spec file for package python-tomate
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2014 Elio Esteves Duarte <elio.esteves.duarte@gmail.com>
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


Name:           python3-tomate
Version:        0.12.0
Release:        0
Summary:        A pomodoro timer
License:        GPL-3.0-or-later
Group:          Productivity/Other
URL:            https://github.com/eliostvs/tomate
Source:         tomate-%{version}.tar.gz
BuildRequires:  python3-setuptools
Requires:       /usr/bin/aplay
Requires:       dbus-1-python3
Requires:       python3-blinker
Requires:       python3-gobject
Requires:       python3-pyxdg
Requires:       python3-six
Requires:       python3-venusian
Requires:       python3-wiring
Requires:       python3-wrapt
Requires:       python3-yapsy
BuildArch:      noarch
# SECTION tests
BuildRequires:  dbus-1-python3
BuildRequires:  python3-blinker
BuildRequires:  python3-gobject
BuildRequires:  python3-pytest-cov
BuildRequires:  python3-pytest-flake8
BuildRequires:  python3-pytest-mock
BuildRequires:  python3-pytest-runner
BuildRequires:  python3-pyxdg
BuildRequires:  python3-venusian
BuildRequires:  python3-wiring
BuildRequires:  python3-wrapt
BuildRequires:  python3-yapsy
# /SECTION

%description
Provides the library for tomate, a Pomodoro timer.

%prep
%autosetup -n tomate-%{version}
touch tests/__init__.py

%build
%py3_build

%install
%py3_install

%check
pytest tests

%files
%{python3_sitelib}/*.egg-info
%{python3_sitelib}/tomate*
%license COPYING
%doc AUTHORS README.md

%changelog
