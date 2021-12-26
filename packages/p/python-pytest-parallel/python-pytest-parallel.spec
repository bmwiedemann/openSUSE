#
# spec file for package python-pytest-parallel
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
%define skip_python2 1
Name:           python-pytest-parallel
Version:        0.1.1
Release:        0
Summary:        Pytest plugin for parallel and concurrent testing
License:        MIT
URL:            https://github.com/browsertron/pytest-parallel
Source:         https://github.com/browsertron/pytest-parallel/archive/%{version}.tar.gz#/pytest-parallel-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.6}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-pytest5 >= 3.0.0
Requires:       python-tblib
BuildArch:      noarch
# SECTION test requirements
# Pytest5 because of gh#browsertron/pytest-parallel#91
BuildRequires:  %{python_module pytest5 >= 3.0.0}
BuildRequires:  %{python_module pytest-html}
BuildRequires:  %{python_module tblib}
# /SECTION
%python_subpackages

%description
A pytest plugin for parallel and concurrent testing.

%prep
%autosetup -p1 -n pytest-parallel-%{version}

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
