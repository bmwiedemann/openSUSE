#
# spec file for package python-coverage-env-plugin
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

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-coverage-env-plugin
Version:        0.2.0
Release:        0
Summary:        Coverage environment plugin
License:        MIT
Group:          Development/Languages/Python
Url:            https://github.com/jayvdb/coverage_env_plugin
Source:         https://files.pythonhosted.org/packages/source/c/coverage-env-plugin/coverage-env-plugin-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module coverage >= 4.0}
BuildRequires:  %{python_module coverage-config-reload-plugin}
BuildRequires:  %{python_module packaging}
BuildRequires:  %{python_module unittest-mixins}
# /SECTION
BuildRequires:  fdupes
Requires:       python-coverage >= 4.0
Requires:       python-packaging
BuildArch:      noarch

%python_subpackages

%description
Environment plugin for the coverage package.

%prep
%setup -q -n coverage-env-plugin-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_exec setup.py test

%files %{python_files}
%doc CHANGELOG.md README.md
%license LICENSE
%{python_sitelib}/*

%changelog
