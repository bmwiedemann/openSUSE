#
# spec file for package python-arviz
#
# Copyright (c) 2026 SUSE LLC and contributors
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


%{?sle15_python_module_pythons}
# Upstream supports Python 3.12+
%define skip_python311 1
Name:           python-arviz
Version:        1.0.0
Release:        0
Summary:        Exploratory analysis of Bayesian models
License:        Apache-2.0
URL:            http://github.com/arviz-devs/arviz
Source:         https://github.com/arviz-devs/arviz/archive/v%{version}.tar.gz#/arviz-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.12}
BuildRequires:  %{python_module flit-core >= 3.4}
BuildRequires:  %{python_module pip}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module arviz-base >= 1.0.0}
BuildRequires:  %{python_module arviz-plots >= 1.0.0}
BuildRequires:  %{python_module arviz-stats >= 1.0.0}
BuildRequires:  %{python_module pytest}
# /SECTION
Requires:       python-arviz-base >= 1.0.0
Requires:       python-arviz-plots >= 1.0.0
Requires:       python-arviz-stats >= 1.0.0
BuildArch:      noarch
%python_subpackages

%description
ArviZ is a Python package for exploratory analysis of Bayesian models. Includes
functions for posterior analysis, data storage, model checking, comparison and
diagnostics.

%prep
%setup -q -n arviz-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc CHANGELOG.md README.md
%license LICENSE
%{python_sitelib}/arviz
%{python_sitelib}/arviz-%{version}.dist-info

%changelog
