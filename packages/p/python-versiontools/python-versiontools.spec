#
# spec file for package python-versiontools
#
# Copyright (c) 2025 SUSE LLC
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


Name:           python-versiontools
Version:        1.9.1
Release:        0
Summary:        Smart replacement for plain tuple used in __version__
License:        LGPL-3.0-or-later
Group:          Development/Languages/Python
URL:            https://launchpad.net/versiontools
Source:         https://files.pythonhosted.org/packages/source/v/versiontools/versiontools-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  python-rpm-macros
Requires:       python-setuptools
BuildArch:      noarch
%python_subpackages

%description
Smart replacement for plain tuple used in __version__.

* Keep a *single version definition* inside your package or module
* Get proper versioning of development snapshots coupled with your
  Version Control System (pluggable support for additional systems
  available)
* Produce nice version strings for released files that are compliant
  with PEP 386
* Remain comparable as tuple of integers

%prep
%setup -q -n versiontools-%{version}
sed -i "1d" versiontools/{git_support,hg_support,bzr_support}.py # Fix non-executable scripts

%build
%pyproject_wheel

%install
%pyproject_install

%files %{python_files}
%doc doc/*
%{python_sitelib}/versiontools
%{python_sitelib}/versiontools-%{version}*-info

%changelog
