#
# spec file for package python-duckduckgo2
#
# Copyright (c) 2024 SUSE LLC
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


Name:           python-duckduckgo2
Version:        0.242
Release:        0
Summary:        Library for querying the DuckDuckGo API
License:        BSD-3-Clause
URL:            https://github.com/crazedpsyc/python-duckduckgo/
Source:         https://files.pythonhosted.org/packages/source/d/duckduckgo2/duckduckgo2-%{version}.tar.gz
Patch0:         add-python3-support.patch
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
%python_subpackages

%description
A Python library for querying the DuckDuckGo API.

%prep
%autosetup -p1 -n duckduckgo2-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/ddg
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%post
%python_install_alternative ddg

%postun
%python_uninstall_alternative ddg

%files %{python_files}
%doc README.rst
%license LICENSE
%python_alternative %{_bindir}/ddg
%{python_sitelib}/duckduckgo.py
%pycache_only %{python_sitelib}/__pycache__/duckduckgo.*.py*
%{python_sitelib}/duckduckgo2-%{version}.dist-info

%changelog
