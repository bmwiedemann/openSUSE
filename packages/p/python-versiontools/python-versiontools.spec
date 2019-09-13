#
# spec file for package python-versiontools
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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
Name:           python-versiontools
Version:        1.9.1
Release:        0
Summary:        Smart replacement for plain tuple used in __version__
License:        LGPL-3.0-or-later
Group:          Development/Languages/Python
Url:            https://launchpad.net/versiontools
Source:         https://files.pythonhosted.org/packages/source/v/versiontools/versiontools-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  python-rpm-macros
Requires:       python-setuptools
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
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
%python_build

%install
%python_install

%files %{python_files}
%defattr(-,root,root,-)
%doc doc/*
%{python_sitelib}/*

%changelog
