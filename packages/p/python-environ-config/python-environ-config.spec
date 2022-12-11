#
# spec file for package python-environ-config
#
# Copyright (c) 2022 SUSE LLC
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
Name:           python-environ-config
Version:        22.1.0
Release:        0
Summary:        Boilerplate-free configuration with env variables
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/hynek/environ_config
Source:         https://files.pythonhosted.org/packages/source/e/environ-config/environ-config-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-attrs >= 17.4.0
Conflicts:      python-django-environ
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module attrs >= 17.4.0}
BuildRequires:  %{python_module boto3}
BuildRequires:  %{python_module moto}
BuildRequires:  %{python_module pytest}
# /SECTION
%python_subpackages

%description
Boilerplate-free configuration with env variables.

%prep
%setup -q -n environ-config-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%license LICENSE
%doc README.rst CHANGELOG.rst
%{python_sitelib}/*

%changelog
