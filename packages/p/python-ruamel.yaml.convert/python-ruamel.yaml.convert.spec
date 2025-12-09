#
# spec file for package python-ruamel.yaml.convert
#
# Copyright (c) 2025 SUSE LLC and contributors
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


Name:           python-ruamel.yaml.convert
Version:        0.3.2
Release:        0
Summary:        Data format conversion routines to and from YAML
License:        MIT
URL:            https://sourceforge.net/projects/ruamel-yaml-convert/
Source:         https://files.pythonhosted.org/packages/source/r/ruamel.yaml.convert/ruamel.yaml.convert-%{version}.tar.gz
# PATCH-FIX-OPENSUSE Support Python 3.14 ast changes
Patch0:         support-python314.patch
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module ruamel.base >= 1.0.0+post1}
BuildRequires:  %{python_module ruamel.yaml}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
# 1.0.0+post1 needed to depend on revised base namespace technique
Requires:       python-python-dateutil
Requires:       python-ruamel.base >= 1.0.0+post1
Requires:       python-ruamel.yaml
Recommends:     python-beautifulsoup4
BuildArch:      noarch

%python_subpackages

%description
Data format conversion routines to and from YAML.

%prep
%autosetup -p1 -n ruamel.yaml.convert-%{version}
# Remove unnecessary namespace declaration
sed -i '/namespace_packages=/d' setup.py

%build
%pyproject_wheel

%install
export RUAMEL_NO_PIP_INSTALL_CHECK=1
%pyproject_install
%{python_expand rm -r %{buildroot}%{$python_sitelib}/ruamel/__* %{buildroot}%{$python_sitelib}/ruamel/yaml/__*
%fdupes %{buildroot}%{$python_sitelib}
}

%files %{python_files}
%doc README.rst
%license LICENSE
%dir %{python_sitelib}/ruamel/yaml
%{python_sitelib}/ruamel/yaml/convert
%{python_sitelib}/ruamel[_.]yaml[._]convert-%{version}.dist-info

%changelog
