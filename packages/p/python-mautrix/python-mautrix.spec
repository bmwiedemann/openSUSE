#
# spec file for package python-mautrix
#
# Copyright (c) 2020 SUSE LLC
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
# Python2 is not supported
%define skip_python2 1
Name:           python-mautrix
Version:        0.5.0
Release:        0
Summary:        A Python 3 asyncio Matrix framework
License:        MPL-2.0
URL:            https://github.com/tulir/mautrix-python
Source:         https://files.pythonhosted.org/packages/source/m/mautrix/mautrix-%{version}.tar.gz
Source99:       https://raw.githubusercontent.com/tulir/mautrix-python/master/LICENSE
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-aiohttp >= 3.0.1
Requires:       python-attrs >= 18.1.0
Recommends:     python-python-magic >= 0.4.15
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module aiohttp >= 3.0.1}
BuildRequires:  %{python_module attrs >= 18.1.0}
BuildRequires:  %{python_module commonmark}
BuildRequires:  %{python_module lxml}
BuildRequires:  %{python_module python-magic >= 0.4.15}
BuildRequires:  %{python_module ruamel.yaml}
BuildRequires:  %{python_module sqlalchemy}
# /SECTION
%python_subpackages

%description
A Python 3 asyncio Matrix framework.

%prep
%setup -q -n mautrix-%{version}
cp %{SOURCE99} .
# do not require hardcoded versions
sed -i -e 's:~=:>=:' setup.py

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitelib}/*

%changelog
