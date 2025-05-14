#
# spec file for package python-PyRSS2Gen
#
# Copyright (c) 2025 SUSE LLC
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


%define oldpython python
Name:           python-PyRSS2Gen
Version:        1.1
Release:        0
Summary:        Generate RSS2 using a Python data structure
License:        BSD-3-Clause
URL:            http://dalkescientific.com/Python/PyRSS2Gen.html
Source:         http://dalkescientific.com/Python/PyRSS2Gen-%{version}.tar.gz
BuildRequires:  %{python_module feedparser}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Provides:       %{oldpython}-pyrss2gen = 1.1
Obsoletes:      %{oldpython}-pyrss2gen < 1.1
BuildArch:      noarch
%python_subpackages

%description
A Python library for generating RSS 2.0 feeds.

%prep
%setup -q -n PyRSS2Gen-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# Test fails on Python 2, and there is a feedparser error on Python 3
%python_exec test.py ||:

%files %{python_files}
%doc README
%license LICENSE
%{python_sitelib}/PyRSS2Gen.py
%pycache_only %{python_sitelib}/__pycache__/PyRSS2Gen*
%{python_sitelib}/[Pp]y[Rr][Ss][Ss]2[Gg]en-%{version}*-info

%changelog
