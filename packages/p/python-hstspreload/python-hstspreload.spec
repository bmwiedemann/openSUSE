#
# spec file for package python-hstspreload
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


Name:           python-hstspreload
Version:        2026.7.1
Release:        0
Summary:        Python Chromium HSTS Preload list
License:        BSD-3-Clause
URL:            https://github.com/sethmlarson/hstspreload
Source:         https://github.com/sethmlarson/hstspreload/archive/refs/tags/%{version}.tar.gz#/hstspreload-%{version}-gz.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
Chromium HSTS Preload list as a Python package.

%prep
%autosetup -p1 -n hstspreload-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

#%%check depends on httpx, which depends on hstspreload
# Also, depends on the huge static data, and tests seem to fail ATM.
#%%pytest

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/hstspreload
%{python_sitelib}/hstspreload-%{version}.dist-info

%changelog
