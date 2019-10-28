#
# spec file for package python-napalm-exos
#
# Copyright (c) 2019, Martin Hauke <mardnh@gmx.de>
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%define skip_python2 1
Name:           python-napalm-exos
Version:        0.0.0+git.20180925
Release:        0
License:        Apache-2.0
Summary:        NAPALM - Extreme Networks EXOS Driver network driver
Url:            https://github.com/ixaustralia/napalm-exos
Group:          Development/Languages/Python
Source:         napalm-exos-%{version}.tar.xz
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
### SECTION test requirements
#BuildRequires:  %%{python_module napalm >= 2.4.0}
#BuildRequires:  %%{python_module pytest}
# /SECTION
BuildRequires:  fdupes
Requires:       python-napalm >= 2.4.0
Requires:       python-netmiko
Requires:       python-textfsm
BuildArch:      noarch
%python_subpackages

%description
Extreme Networks EXOS Driver implementation for the NAPALM Network
Automation Project.

%prep
%setup -q -n napalm-exos-%{version}
# Fix permission
chmod -x AUTHORS LICENSE

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# There aren't any tests right now.
#%%pytest

%files %{python_files}
%license LICENSE
%doc AUTHORS README.md
%{python_sitelib}/*

%changelog
