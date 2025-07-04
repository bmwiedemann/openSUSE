#
# spec file for package python-j2gen
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


%bcond_without libalternatives
Name:           python-j2gen
Version:        0.1.0
Release:        0
Summary:        Jinja2 template renderer with yaml input files
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://github.com/toabctl/j2gen
Source:         https://files.pythonhosted.org/packages/source/j/j2gen/j2gen-%{version}.tar.gz
BuildRequires:  %{python_module pbr}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  alts
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       alts
Requires:       python-Jinja2
Requires:       python-PyYAML
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module Jinja2}
BuildRequires:  %{python_module PyYAML}
BuildRequires:  %{python_module ddt}
BuildRequires:  %{python_module flake8}
BuildRequires:  %{python_module pytest}
# /SECTION
%python_subpackages

%description
Jinja2 template renderer with yaml input files

%prep
%setup -q -n j2gen-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/j2gen
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pyunittest discover -v

%pre
# removing old update-alternatives entries
%python_libalternatives_reset_alternative j2gen

%files %{python_files}
%doc AUTHORS ChangeLog README.rst
%license LICENSE
%python_alternative %{_bindir}/j2gen
%{python_sitelib}/j2gen
%{python_sitelib}/j2gen-%{version}*-info

%changelog
