#
# spec file for package python-ifconfig-parser
#
# Copyright (c) 2020 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-ifconfig-parser
Version:        0.0.5
Release:        0
License:        MIT
Summary:        Python package for parsing raw output of ifconfig
Url:            https://github.com/KnightWhoSayNi/ifconfig-parser
Group:          Development/Languages/Python
Source:         https://files.pythonhosted.org/packages/source/i/ifconfig-parser/ifconfig-parser-%{version}.tar.gz
Source1:        https://raw.githubusercontent.com/KnightWhoSayNi/ifconfig-parser/master/LICENSE
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
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
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

#%%check
#Upstream does not ship any tests

%files %{python_files}
%license LICENSE
%doc README.md
%{python_sitelib}/ifconfig*

%changelog
