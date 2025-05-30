#
# spec file for package python-ifconfig-parser
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


Name:           python-ifconfig-parser
Version:        0.0.5
Release:        0
Summary:        Python package for parsing raw output of ifconfig
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/KnightWhoSayNi/ifconfig-parser
Source:         https://files.pythonhosted.org/packages/source/i/ifconfig-parser/ifconfig-parser-%{version}.tar.gz
Source1:        https://raw.githubusercontent.com/KnightWhoSayNi/ifconfig-parser/master/LICENSE
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
Python package for parsing raw output of ifconfig.

%prep
%setup -q -n ifconfig-parser-%{version}
cp %{SOURCE1} .
sed -i -e '/^#!\//, 1d' ifconfigparser/*.py
rm -f ifconfig_parser.egg-info/.gitignore

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

#%%check
#Upstream does not ship any tests

%files %{python_files}
%license LICENSE
%doc README.md
%{python_sitelib}/ifconfig*

%changelog
