#
# spec file for package python-subscene-api
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
%define skip_python2 1
Name:           python-subscene-api
Version:        2.0.0
Release:        0
Summary:        Python wrapper for Subscene subtitle database
License:        GPL-3.0-or-later
Group:          Development/Languages/Python
Url:            https://github.com/mamins1376/Subscene-API
Source0:        https://pypi.io/packages/source/s/subscene-api/subscene-api-%{version}.tar.gz
BuildRequires:  %{python_module beautifulsoup4 >= 4.4.1}
BuildRequires:  %{python_module setuptools}
BuildRequires:  python-rpm-macros
Requires:       python-beautifulsoup4 >= 4.4.1
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch
%python_subpackages

%description
Exposes the Subscene subtitle database API to Python.

%prep
%setup -q -n subscene-api-%{version}
rm -rf subscene_api.egg-info
# remove unwanted shebang
sed -i -e '1d' subscene/__init__.py

%build
%python_build

%install
%python_install

%files %{python_files}
%defattr(-,root,root)
%{python_sitelib}/subscene
%{python_sitelib}/subscene_api-%{version}-py%{python_version}.egg-info

%changelog
