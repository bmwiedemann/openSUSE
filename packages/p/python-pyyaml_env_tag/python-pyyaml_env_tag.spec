#
# spec file for package python-pyyaml_env_tag
#
# Copyright (c) 2021 SUSE LLC
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


%define skip_python2 1
%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-pyyaml_env_tag
Version:        0.1
Release:        0
Summary:        A custom YAML tag for referencing environment variables in YAML files
License:        MIT
URL:            https://github.com/waylan/pyyaml-env-tag
Source:         https://files.pythonhosted.org/packages/source/p/pyyaml_env_tag/pyyaml_env_tag-%{version}.tar.gz
BuildRequires:  %{python_module PyYAML}
BuildRequires:  %{python_module flit-core}
BuildRequires:  %{python_module pip}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-PyYAML
BuildArch:      noarch
%python_subpackages

%description
A custom YAML tag for referencing environment variables in YAML files.

%prep
%setup -q -n pyyaml_env_tag-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pyunittest -v

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/pyyaml_env_tag*
%{python_sitelib}/yaml_env_tag*
%{python_sitelib}/__pycache__/yaml_env_tag*

%changelog
