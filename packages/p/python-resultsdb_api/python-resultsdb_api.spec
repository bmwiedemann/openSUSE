#
# spec file for package python-resultsdb_api
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
Name:           python-resultsdb_api
Version:        2.1.5
Release:        0
Summary:        Library for simplifying the communication with ResultsDB
License:        GPL-2.0-or-later
URL:            https://pagure.io/taskotron/resultsdb_api
Source:         https://files.pythonhosted.org/packages/source/r/resultsdb_api/resultsdb_api-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-requests >= 2.2.1
Requires:       python-simplejson >= 3.5.3
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module pytest >= 2.4.2}
BuildRequires:  %{python_module requests >= 2.2.1}
BuildRequires:  %{python_module simplejson >= 3.5.3}
# /SECTION
%python_subpackages

%description
The ResultsDB API module provides a Python API for using ResultsDB's
JSON/REST interface in a more pythonic way. It has functions which match
the JSON/REST methods, but allow the common goodies as named parameters,
and parameters skipping.

%prep
%setup -q -n resultsdb_api-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest --functional testing/

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/resultsdb_api*
%pycache_only %{python_sitelib}/__pycache__/

%changelog
