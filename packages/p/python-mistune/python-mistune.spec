#
# spec file for package python-mistune
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
Name:           python-mistune
Version:        0.8.4
Release:        0
Summary:        A markdown parser in pure Python
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/lepture/mistune
Source0:        https://files.pythonhosted.org/packages/source/m/mistune/mistune-%{version}.tar.gz
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
A markdown parser in pure Python, inspired by marked.

%prep
%setup -q -n mistune-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%license LICENSE
%doc CHANGES.rst README.rst
%{python_sitelib}/mistune.py*
%pycache_only %{python_sitelib}/__pycache__/*
%dir %{python_sitelib}/mistune-%{version}-py*.egg-info
%{python_sitelib}/mistune-%{version}-py*.egg-info/*

%changelog
