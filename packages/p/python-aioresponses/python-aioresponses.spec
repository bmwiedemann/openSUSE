#
# spec file for package python-aioresponses
#
# Copyright (c) 2023 SUSE LLC
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


%{?!python_module:%define python_module() python3-%{**}}
%define skip_python2 1
Name:           python-aioresponses
Version:        0.7.4
Release:        0
Summary:        Python module for mocking out requests made by ClientSession from aiohttp
License:        MIT
URL:            https://github.com/pnuckowski/aioresponses
Source:         https://files.pythonhosted.org/packages/source/a/aioresponses/aioresponses-%{version}.tar.gz
BuildRequires:  %{python_module aiohttp >= 2.0.0}
BuildRequires:  %{python_module ddt >= 1.1.0}
BuildRequires:  %{python_module pbr}
BuildRequires:  %{python_module pytest >= 3.8.1}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module typing}
BuildRequires:  %{python_module yarl}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  (python3-asynctest if python3-base < 3.8)
BuildRequires:  (python36-asynctest if python36-base)
Requires:       python-aiohttp >= 2.0.0
BuildArch:      noarch
%python_subpackages

%description
This is a Python module for mocking out requests made by ClientSession
from the aiohttp package.

%prep
%setup -q -n aioresponses-%{version}

%build
export LC_ALL=en_US.UTF-8
%python_build

%install
export LC_ALL=en_US.UTF-8
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export LC_ALL=en_US.UTF-8
# disable tests which try to access external network
skiptests+="test_address_as_instance_of_url_combined_with_pass_through"
skiptests+=" or test_pass_through_with_origin_params"
%pytest -k "not ($skiptests)"

%files %{python_files}
%doc AUTHORS AUTHORS.rst ChangeLog README.rst
%license LICENSE
%{python_sitelib}/aioresponses
%{python_sitelib}/aioresponses-%{version}-py*.egg-info

%changelog
