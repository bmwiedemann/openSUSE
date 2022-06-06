#
# spec file for package python-pydrive2
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
Name:           python-pydrive2
Version:        1.10.1
Release:        0
Summary:        A wrapper library for google-api-python-client
License:        Apache-2.0
URL:            https://github.com/iterative/PyDrive2
Source:         https://files.pythonhosted.org/packages/source/P/PyDrive2/PyDrive2-%{version}.tar.gz
# PATCH-FIX-UPSTREAM https://github.com/iterative/PyDrive2/commit/2e43e4561d965ce78dc158a02fbdb75ba6c38105 pydrive2: modernise to python 3.7+
Patch0:         modernize.patch
# PATCH-FIX-UPSTREAM https://github.com/iterative/PyDrive2/pull/180 Migrating to Google Auth Library
Patch1:         migrate-to-google-auth.patch
BuildRequires:  %{python_module setuptools}
BuildRequires:  python-rpm-macros
## tests fail in OBS environment
# SECTION test requirements
#BuildRequires:  %{python_module google-api-python-client >= 1.12.5}
#BuildRequires:  %{python_module PyYAML >= 3.0}
#BuildRequires:  %{python_module black}
BuildRequires:  %{python_module filelock >= 3.7.0}
#BuildRequires:  %{python_module flake8-docstrings}
#BuildRequires:  %{python_module flake8}
#BuildRequires:  %{python_module fsspec}
#BuildRequires:  %{python_module funcy >= 1.14}
BuildRequires:  %{python_module google-auth-oauthlib >= 0.5.1}
BuildRequires:  %{python_module google-auth >= 2.6.6}
BuildRequires:  %{python_module google-auth-httplib2 >= 0.1.0}
#BuildRequires:  %{python_module pyOpenSSL >= 19.1.0}
#BuildRequires:  %{python_module pytest-mock}
#BuildRequires:  %{python_module pytest}
#BuildRequires:  %{python_module six >= 1.13.0}
#BuildRequires:  %{python_module timeout-decorator}
#BuildRequires:  %{python_module tqdm}
# /SECTION
BuildRequires:  fdupes
Requires:       python-PyYAML >= 3.0
Requires:       python-filelock >= 3.7.0
Requires:       python-google-api-python-client >= 1.12.5
Requires:       python-google-auth >= 2.6.6
Requires:       python-google-auth-httplib2 >= 0.1.0
Requires:       python-google-auth-oauthlib >= 0.5.1
Requires:       python-pyOpenSSL >= 19.1.0
Requires:       python-six >= 1.13.0
BuildArch:      noarch
%python_subpackages

%description
PyDrive2 is a wrapper library of google-api-python-client that simplifies many
common Google Drive API V2 tasks. It is an actively maintained fork of PyDrive.
By the authors and maintainers of the Git for Data - DVC project.

%prep
%setup -q -n PyDrive2-%{version}
%autopatch -p1

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# The pydrive2 tests require network connectivity and a Google service account

%files %{python_files}
%doc CHANGES README.rst
%license LICENSE
%{python_sitelib}/*

%changelog
