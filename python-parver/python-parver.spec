#
# spec file for package python-parver
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
Name:           python-parver
Version:        0.2.1
Release:        0
Summary:        Module to parse and manipulate version numbers
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/RazerM/parver
Source:         https://files.pythonhosted.org/packages/source/p/parver/parver-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module Arpeggio >= 1.7}
BuildRequires:  %{python_module attrs >= 17.4.0}
BuildRequires:  %{python_module hypothesis >= 3.56}
BuildRequires:  %{python_module pretend >= 1.0}
BuildRequires:  %{python_module pytest >= 3.5}
BuildRequires:  %{python_module six >= 1.9}
# /SECTION
BuildRequires:  fdupes
Requires:       python-Arpeggio >= 1.7
Requires:       python-attrs >= 17.4.0
Requires:       python-six >= 1.9
BuildArch:      noarch

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
%{python_expand  #
export PYTHONPATH=%{buildroot}%{$python_sitelib}
$python -m pytest
}

%files %{python_files}
%license LICENSE
%doc CHANGELOG.md README.rst
%{python_sitelib}/*

%changelog
