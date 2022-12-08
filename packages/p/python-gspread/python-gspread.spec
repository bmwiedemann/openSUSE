#
# spec file for package python-gspread
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
Name:           python-gspread
Version:        5.7.2
Release:        0
Summary:        Google Spreadsheets Python API
License:        MIT
URL:            https://github.com/burnash/gspread
Source:         https://github.com/burnash/gspread/archive/v%{version}.tar.gz
BuildRequires:  %{python_module betamax}
BuildRequires:  %{python_module google-auth-oauthlib >= 0.4.1}
BuildRequires:  %{python_module xml}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-google-auth >= 1.12.0
Requires:       python-google-auth-oauthlib >= 0.4.1
BuildArch:      noarch
%python_subpackages

%description
A Python module to access Google Spreadsheets.

Features
--------

* Google Sheets API v4.
* Open a spreadsheet by its *title*, *url* or *key*.
* Select cells by labels, e.g. 'A1'.
* Extract range, entire row or column values.
* Python 3 support.

%prep
%setup -q -n gspread-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# needs betamax-json-body-serializer that does not exist on pypi anywhere
#%%python_expand PYTHONPATH=%{buildroot}%{$python_sitelib} nosetests-%{$python_bin_suffix} -v

%files %{python_files}
%doc README.md
%license LICENSE.txt
%{python_sitelib}/*

%changelog
