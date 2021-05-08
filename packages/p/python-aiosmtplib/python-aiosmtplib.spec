#
# spec file for package python-aiosmtplib
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
Name:           python-aiosmtplib
Version:        1.1.5
Release:        0
Summary:        Python asyncio SMTP client
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/cole/aiosmtplib
Source:         https://files.pythonhosted.org/packages/source/a/aiosmtplib/aiosmtplib-%{version}.tar.gz
# PATCH-FIX-UPSTREAM failing_smtpd_tests.patch  gh#cole/aiosmtplib#171 mcepl@suse.com
# fix tests/smtpd.py
Patch0:         failing_smtpd_tests.patch
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Suggests:       python-aiosmtpd
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module aiosmtpd}
BuildRequires:  %{python_module hypothesis}
BuildRequires:  %{python_module pytest-asyncio}
# /SECTION
%python_subpackages

%description
Python asyncio SMTP client.

%prep
%autosetup -p1 -n aiosmtplib-%{version}

%build
%python_build

%install
%python_install
%python_expand rm -r %{buildroot}%{$python_sitelib}/{tests,docs}
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest -rs -k 'not (test_qq_login or test_starttls_gmail)'

%files %{python_files}
%doc README.rst docs/*.rst
%license LICENSE.txt
%{python_sitelib}/*

%changelog
