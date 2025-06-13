#
# spec file for package python-subscene-api
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


Name:           python-subscene-api
Version:        2.0.0
Release:        0
Summary:        Python wrapper for Subscene subtitle database
License:        GPL-3.0-or-later
Group:          Development/Languages/Python
URL:            https://github.com/mamins1376/Subscene-API
Source0:        https://files.pythonhosted.org/packages/source/s/subscene-api/subscene-api-%{version}.tar.gz
BuildRequires:  %{python_module beautifulsoup4 >= 4.4.1}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  python-rpm-macros
Requires:       python-beautifulsoup4 >= 4.4.1
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
%pyproject_wheel

%install
%pyproject_install

%files %{python_files}
%{python_sitelib}/subscene
%{python_sitelib}/subscene_api-%{version}*-info

%changelog
