#
# spec file for package python-coverage-config-reload-plugin
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
Name:           python-coverage-config-reload-plugin
Version:        0.3.0
Release:        0
Summary:        Coverage hack plugin to reload the coverage configuration
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/jayvdb/coverage_config_reload_plugin
Source:         https://files.pythonhosted.org/packages/source/c/coverage-config-reload-plugin/coverage-config-reload-plugin-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-coverage >= 4.0
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module coverage >= 4.0}
BuildRequires:  %{python_module unittest-mixins}
# /SECTION
%python_subpackages

%description
Placed as the last plugin to be loaded, this plugin will reloads the
configuration files after other plugins have been loaded.

%prep
%setup -q -n coverage-config-reload-plugin-%{version}

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
