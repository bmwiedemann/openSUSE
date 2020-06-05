#
# spec file for package python-pytest-sphinx
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
%bcond_without python2
Name:           python-pytest-sphinx
Version:        0.2.2
Release:        0
Summary:        Doctest plugin for pytest with support for Sphinx-specific doctest-directives
License:        BSD-3-Clause
URL:            https://github.com/thisch/pytest-sphinx
Source:         https://github.com/thisch/pytest-sphinx/archive/v0.2.2.tar.gz#/pytest-sphinx-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-pytest >= 3.1.1
BuildArch:      noarch
%ifpython2
Requires:       python-enum34
%endif
# SECTION test requirements
BuildRequires:  %{python_module pytest-mock}
BuildRequires:  %{python_module pytest4 >= 3.1.1}
%if %{with python2}
BuildRequires:  python2-enum34
%endif
# /SECTION
%python_subpackages

%description
Doctest plugin for pytest with support for Sphinx-specific doctest-directives.

%prep
%setup -q -n pytest-sphinx-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/*

%changelog
