#
# spec file for package python-pytest-cookies
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
%if %{?python3_version_nodots} == 38
%define pythons python3 python38
%else
%define pythons python3
%endif
Name:           python-pytest-cookies
Version:        0.5.1
Release:        0
Summary:        Cookiecutter template pytest plugin
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/hackebrot/pytest-cookies
Source:         https://github.com/hackebrot/pytest-cookies/archive/%{version}.tar.gz#/pytest-cookies-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       cookiecutter >= 1.4.0
Requires:       python-pytest >= 3.3.0
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module pytest >= 3.3.0}
BuildRequires:  cookiecutter >= 1.4.0
# /SECTION
%python_subpackages

%description
The pytest plugin for your Cookiecutter templates.

%prep
%setup -q -n pytest-cookies-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/*

%changelog
