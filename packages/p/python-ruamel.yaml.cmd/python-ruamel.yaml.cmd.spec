#
# spec file for package python-ruamel.yaml.cmd
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
Name:           python-ruamel.yaml.cmd
Version:        0.5.5
Release:        0
Summary:        Command line utility to manipulate YAML files
License:        MIT
Group:          Development/Languages/Python
URL:            https://bitbucket.org/ruamel/yaml.cmd
Source:         https://bitbucket.org/ruamel/yaml.cmd/downloads/ruamel.yaml.cmd-%{version}.tar.xz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-configobj
Requires:       python-ruamel.std.argparse >= 0.8
Requires:       python-ruamel.yaml >= 0.16.1
Requires:       python-ruamel.yaml.convert >= 0.3
Requires(post): update-alternatives
Requires(postun): update-alternatives
Suggests:       python-configobj
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module configobj}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module ruamel.std.argparse >= 0.8}
BuildRequires:  %{python_module ruamel.yaml >= 0.16.1}
BuildRequires:  %{python_module ruamel.yaml.convert >= 0.3}
# /SECTION
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
%{python_expand mkdir -p %{buildroot}%{$python_sitelib}
cp -r %{$python_sitelib}/ruamel* %{buildroot}%{$python_sitelib}
}
export RUAMEL_NO_PIP_INSTALL_CHECK=1
%python_install
%python_clone -a %{buildroot}%{_bindir}/yaml
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export LANG=en_US.UTF-8
%{python_expand export PATH=${PWD}/build/bin/:$PATH
mkdir -p build/bin
cp %{buildroot}/%{_bindir}/yaml-%{python_version} build/bin/yaml
export PYTHONPATH=%{buildroot}%{$python_sitelib}:%{$python_sitelib}:%{$python_sitearch}
$python -Sm pytest _test/test_*.py
}

%{python_expand # Remove other ruamel packages
rm -r %{buildroot}%{$python_sitelib}/ruamel/__*
rm -r %{buildroot}%{$python_sitelib}/ruamel/base/
rm -r %{buildroot}%{$python_sitelib}/ruamel.base*
rm -r %{buildroot}%{$python_sitelib}/ruamel/std/
rm -r %{buildroot}%{$python_sitelib}/ruamel.std*
rm -r %{buildroot}%{$python_sitelib}/ruamel.yaml-*
rm %{buildroot}%{$python_sitelib}/ruamel/yaml/*.py* %{buildroot}%{$python_sitelib}/ruamel/yaml/py.typed
rm -rf %{buildroot}%{$python_sitelib}/ruamel/yaml/__*
rm -r %{buildroot}%{$python_sitelib}/ruamel/yaml/convert/
rm -r %{buildroot}%{$python_sitelib}/ruamel.yaml.convert-*
rm -rf %{buildroot}%{$python_sitelib}/ruamel/ordereddict/
rm -rf %{buildroot}%{$python_sitelib}/ruamel.ordereddict*
rm -rf %{buildroot}%{$python_sitelib}/ruamel.yaml.clib*
}

%post
%python_install_alternative yaml

%postun
%python_uninstall_alternative yaml

%files %{python_files}
%doc README.rst
%license LICENSE
%python_alternative %{_bindir}/yaml
%{python_sitelib}/ruamel/yaml/cmd/
%{python_sitelib}/ruamel.yaml.cmd-*.egg-info

%changelog
