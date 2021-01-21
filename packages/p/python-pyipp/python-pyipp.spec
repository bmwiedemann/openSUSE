#
# spec file for package python-pyipp
#
# Copyright (c) 2021 SUSE LLC
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
%define skip_python36 1
Name:           python-pyipp
Version:        0.11.0
Release:        0
Summary:        Asynchronous Python client for Internet Printing Protocol (IPP)
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/ctalkington/python-ipp
Source:         https://github.com/ctalkington/python-ipp/archive/%{version}.tar.gz#/pyipp-%{version}.tar.gz
BuildRequires:  %{python_module aiohttp >= 3.6.2}
BuildRequires:  %{python_module deepmerge >= 0.1.0}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module yarl >= 1.4.2}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-aiohttp >= 3.6.2
Requires:       python-deepmerge >= 0.1.0
Requires:       python-yarl >= 1.4.2
BuildArch:      noarch
%python_subpackages

%description
Asynchronous Python client for Internet Printing Protocol (IPP).

%prep
%setup -q -n python-ipp-%{version}
rm tests/test_client.py  tests/test_interface.py

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/*

%changelog
