#
# spec file for package python-pass_python_keyring
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


%define mod_name pass_python_keyring
%{!?python_sitelib: %global python_sitelib %(python -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}
%{!?python_sitearch: %global python_sitearch %(python -c "from distutils.sysconfig import get_python_lib; print get_python_lib(1)")}
%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-pass_python_keyring
Version:        1.1
Release:        0
Summary:        Pass backend for python-keyring lib
License:        Python-2.0
Group:          Productivity/Other
URL:            http://github.com/notandy/pass_python_keyring
Source:         http://github.com/notandy/%{mod_name}/archive/v%{version}.tar.gz
Source1:        keyringrc.cfg
Patch0:         python3.patch
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-keyring
Recommends:     password-store
%if 0%{?suse_version}
BuildArch:      noarch
%endif
%python_subpackages

%description
A pass-powered backend for Python Keyring lib.

%prep
%setup -q -n %{mod_name}-%{version}
%patch0 -p1
install -m0644 %{SOURCE1} .

%build
%python_build

%install
%python_install --skip-build
%python_expand %fdupes %{buildroot}%{$python_sitelib}

# no tests available

%files %{python_files}
%doc README.md keyringrc.cfg
%dir %{python_sitelib}/%{mod_name}-%{version}-py*.egg-info/
%{python_sitelib}/%{mod_name}-%{version}-py*.egg-info/*
%pycache_only %{python_sitelib}/__pycache__/*
%{python_sitelib}/pass.py*

%changelog
