#
# spec file for package python-tomate
#
# Copyright (c) 2020 SUSE LLC
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%define skip_python2 1
Name:           python-tomate
Version:        0.12.0
Release:        0
Summary:        A pomodoro timer
License:        GPL-3.0-or-later
Group:          Productivity/Other
URL:            https://github.com/eliostvs/tomate
Source:         tomate-%{version}.tar.gz
# PATCH-FIX-UPSTEAM fix-tests.patch -- https://github.com/eliostvs/tomate/issues/19 https://github.com/eliostvs/tomate/pull/20
Patch0:         fix-tests.patch
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       /usr/bin/aplay
Requires:       python-blinker
Requires:       python-dbus-python
Requires:       python-gobject
Requires:       python-pyxdg
Requires:       python-six
Requires:       python-venusian
Requires:       python-wiring
Requires:       python-wrapt
Requires:       python-yapsy
BuildArch:      noarch
# SECTION tests
BuildRequires:  %{python_module blinker}
BuildRequires:  %{python_module dbus-python}
BuildRequires:  %{python_module gobject}
BuildRequires:  %{python_module pytest-cov}
BuildRequires:  %{python_module pytest-flake8}
BuildRequires:  %{python_module pytest-mock}
BuildRequires:  %{python_module pytest-runner}
BuildRequires:  %{python_module pyxdg}
BuildRequires:  %{python_module venusian}
BuildRequires:  %{python_module wiring}
BuildRequires:  %{python_module wrapt}
BuildRequires:  %{python_module yapsy}
# /SECTION
%python_subpackages

%description
Provides the library for tomate, a Pomodoro timer.

%prep
%setup -q -n tomate-%{version}
%patch0 -p1
touch tests/__init__.py

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest tests

%files %{python_files}
%{python_sitelib}/*.egg-info
%{python_sitelib}/tomate*
%license COPYING
%doc AUTHORS README.md

%changelog
