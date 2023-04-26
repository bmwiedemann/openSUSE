#
# spec file for package python-bidict
#
# Copyright (c) 2023 SUSE LLC
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


%define skip_python2 1
%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-bidict
Version:        0.22.1
Release:        0
Summary:        Bidirectional map implementation for Python
License:        MPL-2.0
URL:            https://github.com/jab/bidict
Source:         https://github.com/jab/bidict/archive/refs/tags/v%{version}.tar.gz#/bidict-%{version}-gh.tar.gz
BuildRequires:  %{python_module base >= 3.7}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module hypothesis >= 3.6.1}
BuildRequires:  %{python_module pytest >= 3.0.7}
BuildRequires:  %{python_module pytest-benchmark >= 3.1.0a1}
BuildRequires:  %{python_module pytest-xdist}
BuildRequires:  %{python_module sortedcollections >= 0.4.2}
BuildRequires:  %{python_module sortedcontainers >= 1.5.5}
# /SECTION
BuildArch:      noarch

%python_subpackages

%description
Bidirectional map implementation and related functionality.

%prep
%autosetup -p1 -n bidict-%{version}

%build
export LANG=en_US.UTF-8
%pyproject_wheel

%install
%pyproject_install
export LANG=en_US.UTF-8
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export LANG=en_US.UTF-8
%pytest

%files %{python_files}
%doc CHANGELOG.rst README.rst docs/*.rst
%license LICENSE
%{python_sitelib}/*

%changelog
