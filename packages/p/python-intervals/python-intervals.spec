#
# spec file for package python-intervals
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-intervals
Version:        0.8.1
Release:        0
Summary:        Python tools for handling intervals
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/kvesteri/intervals
Source:         https://files.pythonhosted.org/packages/source/i/intervals/intervals-%{version}.tar.gz
BuildRequires:  %{python_module flake8 >= 2.4.0}
BuildRequires:  %{python_module infinity >= 0.1.3}
BuildRequires:  %{python_module isort >= 4.2.2}
BuildRequires:  %{python_module pytest >= 2.2.3}
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
%python_expand py.test-%{$python_bin_suffix}

%files %{python_files}
%doc CHANGES.rst README.rst
%license LICENSE
%{python_sitelib}/*

%changelog
