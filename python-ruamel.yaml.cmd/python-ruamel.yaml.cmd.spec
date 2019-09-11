#
# spec file for package python-ruamel.yaml.cmd
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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
Name:           python-ruamel.yaml.cmd
Version:        0.5.4
Release:        0
License:        MIT
Summary:        Command line utility to manipulate YAML files
Url:            https://bitbucket.org/ruamel/yaml.cmd
Group:          Development/Languages/Python
Source:         https://files.pythonhosted.org/packages/source/r/ruamel.yaml.cmd/ruamel.yaml.cmd-%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module setuptools}
# SECTION test requirements
BuildRequires:  %{python_module configobj}
BuildRequires:  %{python_module ruamel.std.argparse >= 0.8}
BuildRequires:  %{python_module ruamel.yaml >= 0.15.71}
BuildRequires:  %{python_module ruamel.yaml.convert >= 0.3}
# /SECTION
BuildRequires:  fdupes
Requires:       python-configobj
Requires:       python-ruamel.std.argparse >= 0.8
Requires:       python-ruamel.yaml >= 0.15.71
Requires:       python-ruamel.yaml.convert >= 0.3
Suggests:       python-configobj
BuildArch:      noarch

%python_subpackages

%description
Command line utility to manipulate YAML files.

%prep
%setup -q -n ruamel.yaml.cmd-%{version}
# Remove unnecessary namespace declaration
sed -i '/namespace_packages=/d' setup.py

%build
%python_build

%install
export RUAMEL_NO_PIP_INSTALL_CHECK=1
%python_install
%{python_expand rm -r %{buildroot}%{$python_sitelib}/ruamel/__* %{buildroot}%{$python_sitelib}/ruamel/yaml/__*
%fdupes %{buildroot}%{$python_sitelib}
}

%files %{python_files}
%doc README.rst
%license LICENSE
%python3_only %{_bindir}/yaml
%{python_sitelib}/*

%changelog
