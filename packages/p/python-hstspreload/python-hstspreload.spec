#
# spec file for package python-hstspreload
#
# Copyright (c) 2022 SUSE LLC
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
Name:           python-hstspreload
Version:        2022.12.1
Release:        0
Summary:        Python Chromium HSTS Preload list
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/python-http/hstspreload
Source:         https://files.pythonhosted.org/packages/source/h/hstspreload/hstspreload-%{version}.tar.gz
Source1:        https://raw.githubusercontent.com/python-http/hstspreload/master/test_hstspreload.py
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
Chromium HSTS Preload list as a Python package.

%prep
%setup -q -n hstspreload-%{version}
cp %{SOURCE1} .

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

#%%check depends on httpx, which depends on hstspreload
# Also, depends on the huge static data, and tests seem to fail ATM.
#%%pytest

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/*

%changelog
