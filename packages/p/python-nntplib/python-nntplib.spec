#
# spec file for package python-nntplib
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


%define skip_python39 1
%define skip_python310 1
%define skip_python311 1
Name:           python-nntplib
Version:        0.1.3
Release:        0
Summary:        NNTP module from the standard library
License:        BSD-3-Clause
URL:            https://git.cepl.eu/cgit/python/nntplib
Source:         https://files.pythonhosted.org/packages/source/n/nntplib/nntplib-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools >= 61.0}
BuildRequires:  %{python_module testsuite}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
nntplib from Python 3 standard library as an independent module

%prep
%autosetup -p1 -n nntplib-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pyunittest discover -v tests

%files %{python_files}
%doc CHANGES README.md
%license LICENSE
%pycache_only %{python_sitelib}/__pycache__/nntplib.*.pyc
%{python_sitelib}/nntplib.py
%{python_sitelib}/nntplib-%{version}.dist-info

%changelog
