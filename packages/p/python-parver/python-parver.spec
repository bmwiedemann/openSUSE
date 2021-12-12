#
# spec file for package python-parver
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
# hypothesis, as a dependency of this, is not python2 compatible anymore
%define skip_python2 1
Name:           python-parver
Version:        0.3.1
Release:        0
Summary:        Module to parse and manipulate version numbers
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/RazerM/parver
Source:         https://files.pythonhosted.org/packages/source/p/parver/parver-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Arpeggio >= 1.7
Requires:       python-attrs >= 19.2
Requires:       python-six >= 1.13
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module Arpeggio >= 1.7}
BuildRequires:  %{python_module attrs >= 19.2}
BuildRequires:  %{python_module hypothesis >= 3.56}
BuildRequires:  %{python_module pretend >= 1.0}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module six >= 1.13}
# /SECTION
%python_subpackages

%description
parver allows parsing and manipulation of `PEP 440`_ version numbers.

%prep
%setup -q -n parver-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest -q

%files %{python_files}
%license LICENSE
%doc CHANGELOG.md README.rst
%{python_sitelib}/*

%changelog
