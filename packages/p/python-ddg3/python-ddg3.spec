#
# spec file for package python-ddg3
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


Name:           python-ddg3
Version:        0.6.8
%define baseversion %{version}
Release:        0
Summary:        Library for querying the Duck Duck Go API
License:        BSD-3-Clause
URL:            https://github.com/jpetrucciani/python-duckduckgo
Source:         https://github.com/jpetrucciani/python-duckduckgo/archive/refs/tags/%{version}.tar.gz#/ddg3-%{version}-gh.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-requests
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
%python_subpackages

%description
A Python3 library for querying the Duck Duck Go API.

%prep
%setup -q -n python-duckduckgo-%{version}
sed -i -E "s#VERSION#%{version}#g" setup.py ddg3.py

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/ddg3
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%post
%python_install_alternative ddg3

%postun
%python_uninstall_alternative ddg3

%files %{python_files}
%license LICENSE
%python_alternative %{_bindir}/ddg3
%{python_sitelib}/ddg3.py
%pycache_only %{python_sitelib}/__pycache__/ddg3*.pyc
%{python_sitelib}/ddg3-%{baseversion}.dist-info

%changelog
