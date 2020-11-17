#
# spec file for package python-intervals
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
%define skip_python2 1
Name:           python-intervals
Version:        0.9.0
Release:        0
Summary:        Python tools for handling intervals
License:        BSD-3-Clause
URL:            https://github.com/kvesteri/intervals
Source:         https://files.pythonhosted.org/packages/source/i/intervals/intervals-%{version}.tar.gz
BuildRequires:  %{python_module infinity >= 0.1.3}
BuildRequires:  %{python_module isort >= 4.2.2}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-infinity >= 0.1.3
BuildArch:      noarch
%python_subpackages

%description
Python tools for handling intervals (ranges of comparable objects).

%prep
%setup -q -n intervals-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc CHANGES.rst README.rst
%license LICENSE
%{python_sitelib}/*

%changelog
